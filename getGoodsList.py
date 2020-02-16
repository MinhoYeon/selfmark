import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch"
service_key = "서비스키="
query = {
    "trademarkName" : "",
    "classification" : "",
    "asignProduct" : "폰케이스",
    # "applicationNumber" : "4120060014133",
    "registerNumber" : "",
    "publicationNumber" : "",
    "registrationPublicNumber" : "",
    "internationalRegisterNumber" : "",
    "priorityNumber" : "",
    "applicationDate" : "20200212~20200212",
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
# "UTF-8"은 대문자로 써야함.
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
url = api + "?" + params + "&ServiceKey=" + service_key

request = urllib.request.urlopen(url)

# text로 읽어들임
xml = request.read()

# text를 태깅 가능한 xml으로 변환
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)

# 응답파라미터리스트를 추출하기
firstItem = soup.find("item")
listResponseParameter = []
for tag in firstItem.findChildren():
    listResponseParameter.append(tag.name)
# print(listResponseParameter)

# 응답파라미터 값 출력하기
items = soup.select("item")
for item in items:
    # print(item)
    # 응답파라미터를 받아서 하나씩 출력하기
    print("--------------------------------------")
    for i in range(len(listResponseParameter)):
        responseParameter = listResponseParameter[i]
        print("%s : " % (responseParameter), item.select_one(responseParameter).text)









