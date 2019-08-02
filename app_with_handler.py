# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
from flask import Blueprint, request, render_template, flash, redirect, url_for
import os
import sys
import logging
import requests
from argparse import ArgumentParser
import time
import hmac
import hashlib
import binascii
import base64
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

@app.route("/main",methods=['GET'])
def display_main() -> 'html':
    return render_template('test.html',title='main')

@app.route("/main",methods=['POST'])
def test():
     ptr = request.form['학번']
     txt = request.form['이름']
     testReply(ptr,txt)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# 암호화, manager API 실행
def create_sha256_signature(message, key):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    return hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()

url = "http://58306d29.ngrok.io/automateone/api/v1/runProcessWithDataset"
accessToken = "test"
secretKey = "098F6BCD4621D373CADE4E832627B4F6"
contents = '{"projectId": 1, "processId": 2, "dataset":{"ID":"Uce275b6ee9ce7f001a4540c74e1304fa","Message":"success" }}'
nonce = str(time.time())
payload = url + '\n' + accessToken + '\n' + nonce + '\n' + contents + '\n'
signatureBytes = create_sha256_signature(payload, secretKey)
#signatureBase64String = base64.b64encode(signatureBytes)
authorization = accessToken + ":" + nonce + ":" + signatureBytes
headers = {"content-type": "application/json; charset=UTF-8"}

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    logging.error(body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OKs'


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    logging.error(event.reply_token)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="예약 진행중입니다")
    )
    r = requests.post(url, data=contents, headers=headers)

def testReply(RP,txt):
    line_bot_api.push_message(
        RP,
        TextSendMessage(text = txt)
        )
    """line_bot_api.reply_message(
        RP,
        TextSendMessage(text="success")
    )"""

if  __name__  ==  "__main__" :
    #app.run ()
    port  =  int ( os . getenv ( "PORT" ))
    app . run ( host = "0.0.0.0" ,  port = port)