import re

def parseWorld(text):
	regex = re.compile("(여행예약|예약|여기로)(\s|\S)[^안]해?")
	mo = regex.search(text)
	if(mo != None):
		return "예약 해드리겠습니다."

	regex = re.compile("(종료|그만|꺼)(\s|\S)[^안](줘?|주?)")
	mo = regex.search(text)
	if(mo != None):
		return "시스템을 종료합니다. "

	regex = re.compile("(추천|좋은것|관광|코스)(\s|\S)(해?|(알려|말해)줘?)")
	mo = regex.search(text)
	if(mo != None):
		return "관광 코스를 추천해 드리겠습니다. "

	regex = re.compile("(기능|도움말|도움)(\s|\S)(알려줘?|뭐야?)")
	mo = regex.search(text)
	if(mo != None):
		return "***도움말***\n1.예약 기능 : 원하시는 패키지를 예약해 드립니다.\n2.추천 기능 : 고객님의 요구에 맞게 패키지 추천해드립니다.\n3.종료 기능 : 프로그램을 종료합니다.\n4.도움말 기능 : 도움말을 출력합니다.\n"

	if(mo == None):
		return "요청하신 기능은 저희가 지원 안합니다. 도움말 요청해주세요" + "향후 학습을 위해 사용자의 입력 데이터 저장"


def parseSentence(text):
	arr = re.findall("\d+", text)
	if(arr is None):
		return "다시 입력해 주세요"
	else:
		return arr[0]+"월"+arr[1]+"일 맞습니까?"



