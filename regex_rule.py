import re

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
	message = "목적 도시, 출발 도시, 출발 날짜(월 일), 가격, 인원수를 알려주세요."
	return message

def scenario2(text):
	message = "이름(한국),이름(영어), 성별, 생년월일, 휴대폰 번호, 요청사항을 알려주세요."
	return message

def checkInfo(text):
	arr = re.split(" ",text)
	info = ["홍길동", "Hong Kil Dong", "남", "950101", "01012341234", "요청사항..."]
	message = "이름(한국): "+info[0]+'\n'+"이름(영어): "+info[1]+'\n'+"성별: "+info[2]+'\n'+"생년월일: "+info[3]+'\n'+"휴대폰 번호: "+info[4]+'\n'+"요청사항: "+info[5]+'\n'+ "이 맞습니까?"
	return message

def checkReservation(text):
	reservation = ["방콕","서울","10월10일","100","4"]
	message = "목적 도시: " + reservation[0] + '\n' + "출발 도시: " + reservation[1] + '\n' + "출발 날짜: " + reservation[2] + '\n' + "가격: " + reservation[
		3]+"만원" + '\n' + "인원수: " + reservation[4] + "명" '\n' + "이 맞습니까?"
	return message

def startRPA(text):
	message = "입력하신 정보를 바탕으로 예약을 진행하겠습니다."