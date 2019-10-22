import re

url = "http://9327549e.ngrok.io/automateone/api/v1/runProcessWithDataset"
#accessToken = "test"
#secretKey = "098F6BCD4621D373CADE4E832627B4F6"
contents = {"projectId": 1, "processId": 2, "dataset":{"ID":"Uce275b6ee9ce7f001a4540c74e1304fa","Message":"success" }}
#nonce = str(time.time())
#payload = url + '\n' + accessToken + '\n' + nonce + '\n' + contents + '\n'
#signatureBytes = create_sha256_signature(payload, secretKey)
#signatureBase64String = base64.b64encode(signatureBytes)
#authorization = accessToken + ":" + nonce + ":" + signatureBytes
headers = {'content-type': 'application/json; charset=utf-8'}

def parseWorld(text):
	regex = re.compile("(여행정보)(\s|\S)[^안]해?")
	mo = regex.search(text)
	if(mo != None):
		return scenario2(text)

	regex = re.compile("홍길동")
	mo = regex.search(text)
	if(mo != None):
		return checkInfo(text)

	regex = re.compile("네")
	mo = regex.search(text)
	if(mo != None):
		return scenario1(text)

	regex = re.compile("방콕")
	mo = regex.search(text)
	if(mo != None):
		return checkReservation(text)

	regex = re.compile("60")
	mo = regex.search(text)
	if (mo != None):
		return checkReservation(text)

	regex = re.compile("예")
	mo = regex.search(text)
	if (mo != None):
		return startRPA(text)

	if(mo == None):
		return "다시 입력해 주세요"

# 	re.split('\s+', text) - 공백 여러개 기준 split
# 	re.findall('\d+', text) - 숫자로 이루어진 문자열 리스트 변환
#	re.findall('[A-Z]', text) - 대문자 리스트 변환
#	re.findall('[A-Z][a-z]+', text)

def parseSentence(text):
	arr = re.findall("\d+", text)
	if not arr:
		return "다시 입력해 주세요"
	else:
		return arr[0]+"월 "+arr[1]+"일 맞습니까?"

def scenario1(text):
	message = "목적 도시, 출발 도시, 출발 날짜(월 일), 가격범위(최소-최대 (만원)), 인원수를 알려주세요.\n ex) 제주도, 서울, 11-21, 60 80, 성인 1"
	return message

def scenario2(text):
	message = "이름(한국),이름(영어), 성별, 생년월일, 휴대폰 번호, 요청사항, 이메일을 알려주세요.\n ex) 홍길동, Hong KilDong, 남, 19950101, 01012341234, 요청사항.., example@example.com"
	return message

def checkInfo(text):
	info = ["김형우", "KIM HYOUNGWOO", "남", "19951011", "01057424538", "테스트하기위한 예약 진행중입니다.", "gustjr1259@naver.com"]
	message = "이름(한국): "+info[0]+'\n'+"이름(영어): "+info[1]+'\n'+"성별: "+info[2]+'\n'+"생년월일: "+info[3]+'\n'+"휴대폰 번호: "+info[4]+'\n'+"요청사항: "+info[5]+'\n'+"이메일: "+info[6]+'\n'+"이 맞습니까?"
	return message

def checkReservation(text):
	message=""
	if text=="60 80, 성인 1":
		reservation = ["방콕", "인천", "11월21일", "60만원~80만원", "성인 1"]
		message = "목적 도시: " + reservation[0] + '\n' + "출발 도시: " + reservation[1] + '\n' + "출발 날짜: " + reservation[
			2] + '\n' + "가격범위: " + reservation[
					  3] + '\n' + "인원수: " + reservation[4] + "명" + '\n' + "이 맞습니까?"
		return message

	result = text.split(' ')
	arr = ["0","0","0","0","0"]
	arr[0]=result[0]
	arr[1]=result[1]
	arr[2]=result[2]
	dest = ["방콕","서울"]
	start = ["서울","방콕"]
	date = ["11-21"]
	price = ["60 80"]
	num = ["성인 1"]

	for i in dest:
		if i==arr[0]:
			break
		message+="목적도시, "
	for i in start:
		if i==arr[1]:
			break
		message+="출발도시, "
	for i in date:
		if i==arr[2]:
			break
		message+="출발날짜, "
	for i in price:
		if i==arr[3]:
			break
		message+="가격범위, "
	for i in num:
		if i==arr[4]:
			break
		message+="인원수 "

	if(message!=""):
		return message+"정보를 입력해주세요"


	reservation = ["방콕","인천","11월21일","60만원~80만원","성인 1"]
	message = "목적 도시: " + reservation[0] + '\n' + "출발 도시: " + reservation[1] + '\n' + "출발 날짜: " + reservation[2] + '\n' + "가격범위: " + reservation[
		3]+ '\n' + "인원수: " + reservation[4] + "명" +'\n' + "이 맞습니까?"
	return message

def startRPA(text):
	message = "입력하신 정보를 바탕으로 예약을 진행하겠습니다."
	r = requests.post(url, data=contents, headers=headers)
	return message