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
from argparse import ArgumentParser

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
    r = requests.post("http://8147edb6.ngrok.io:8080/automateone/api/v1/runProcess", {'projectId': 1, 'processId': 1})
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
    """line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.reply_token)
    )"""

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