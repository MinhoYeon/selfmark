import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch"
service_key = "w/X8NRxWUugn=/M/FgwDHmkDKaIKY6WZuERI8aDqT1Y="
query = {
    "trademarkName" : "solev",
    "application": "true",
    "refused": "true",
    "expiration": "true",
    "withdrawal": "true",
    "publication": "true",
    "cancel": "true",
    "abandonment": "true",
    "trademark": "true",
    "serviceMark" : "true",
    "trademarkServiceMark" : "true",
    "businessEmblem": "true",
    "collectiveMark": "true",
    "internationalMark": "true",
    "character" : "true",
    "figure" : "true",
    "compositionCharacter" : "true",
    "figureComposition" : "true"
}

# values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding=None, errors=None)
url = api + "?" + params + "&ServiceKey=" + service_key
request = urllib.request.urlopen(url)

# url = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch?trademarkName=solev&applicantName=&application=true&refused=true&expiration=true&withdrawal=true&publication=true&cancel=true&abandonment=true&trademark=true&serviceMark=true&trademarkServiceMark=true&businessEmblem=true&collectiveMark=true&internationalMark=true&character=true&figure=true&compositionCharacter=true&figureComposition=true&ServiceKey=w/X8NRxWUugn=/M/FgwDHmkDKaIKY6WZuERI8aDqT1Y="
# request = urllib.request.urlopen(url)

# text로 읽어들임
xml = request.read()
# print("xml: ", xml)

# text를 태깅 가능한 xml으로 변환
soup = BeautifulSoup(xml, 'html.parser')
# print("soup: ", soup)

# item이 한 사건을 의미함
items = soup.select("item")
for item in items[:1]:
    # 응답파라미터
    listResponseParameter = [
    "agentname", "appreferencenumber", "applicantname", "applicationdate", "applicationnumber",\
    "applicationstatus", "bigdrawing", "classificationcode", "drawing", "fulltext", "indexno",\
    "internationalregisterdate", "internationalregisternumber", "prioritydate", "prioritynumber",\
    "publicationdate", "publicationnumber", "regprivilegename", "regreferencenumber", "registrationdate",\
    "registrationnumber", "registrationpublicdate", "registrationpublicnumber", "title", "viennacode"
    ]
    # 응답파라미터를 받아서 하나씩 출력하기
    for i in range(len(listResponseParameter)):
        responseParameter = listResponseParameter[i]
        print("%s : " % (responseParameter), soup.select_one(responseParameter).text)









