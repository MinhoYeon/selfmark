import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import kiprisPlus

# 상표 상세 검색한 정보를 가져옴
def trademarkInfoSearchService(query):
    api = kiprisPlus.api_getAdvancedSearch
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

query = {
    "trademarkName" : "가가가가",
    "classification" : "",
    "asignProduct" : "",
    "applicationNumber" : "",
    "registerNumber" : "",
    "publicationNumber" : "",
    "registrationPublicNumber" : "",
    "internationalRegisterNumber" : "",
    "priorityNumber" : "",
    "applicationDate" : "20200103~20200103",
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
    "similarityCode" : "G2601",
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
soup = trademarkInfoSearchService(query)

# 응답파라미터리스트
item = soup.find("item")
listResponseParameter = []
for tag in item.find_all(True):
    listResponseParameter.append(tag.name)

# item이 한 사건을 의미함
items = soup.select("item")
for item in items[:1]:
    # 응답파라미터를 받아서 하나씩 출력하기
    for i in range(len(listResponseParameter)):
        responseParameter = listResponseParameter[i]
        print("%s : " % (responseParameter), soup.select_one(responseParameter).text)









