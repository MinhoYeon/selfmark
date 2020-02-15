import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch"
service_key = "서비스키="
query = {
    "trademarkName" : "",
    "classification" : "",
    "asignProduct" : "폰케이",
    "applicationNumber" : "",
    "registerNumber" : "20200212~20200212",
    "publicationNumber" : "",
    "registrationPublicNumber" : "",
    "internationalRegisterNumber" : "",
    "priorityNumber" : "",
    "applicationDate" : "",
    "registerDate" : "",
    "publicationDate" : "",
    "registrationPublicDate" : "",
    "priorityDate" : "",
    "internationalRegisterDate" : "",
    "applicantName" : "",
    "agentName" : "",
    "viennaCode" : "",
    "regPrivilegeName" : "",
    "freeSearch" : "",
    "similarityCode" : "",
    "application" : "true",
    "registration" : "true",
    "refused" : "true",
    "expiration" : "true",
    "withdrawal" : "true",
    "publication" : "true",
    "cancel" : "true",
    "abandonment" : "true",
    "trademark" : "true",
    "serviceMark" : "true",
    "trademarkServiceMark" : "true",
    "businessEmblem" : "true",
    "collectiveMark" : "true",
    "internationalMark" : "true",
    "character" : "true",
    "figure" : "true",
    "compositionCharacter" : "true",
    "figureComposition" : "true",
    "numOfRows" : "20",
    "pageNo" : "1"
}

# values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding='utf-8', errors=None)
url = api + "?" + params + "&ServiceKey=" + service_key
request = urllib.request.urlopen(url)

# text로 읽어들임
xml = request.read()

# text를 태깅 가능한 xml으로 변환
soup = BeautifulSoup(xml, 'html.parser')

# 응답파라미터리스트
item = soup.find("item")

listResponseParameter = []
for tag in item.find_all():
    listResponseParameter.append(tag.name)
# print(listResponseParameter)

# item이 한 사건을 의미함
items = soup.select("item")
for item in items[:1]:
    # print(item)
    # 응답파라미터를 받아서 하나씩 출력하기
    for i in range(len(listResponseParameter)):
        responseParameter = listResponseParameter[i]
        print("%s : " % (responseParameter), soup.select_one(responseParameter).text)









