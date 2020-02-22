# 상품명으로 검색을 하면, 유사군코드별로 지정상품을 보여줌
# 보여지는 지정상품을 선택하면, 유사군코드가 선택됨

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import kiprisPlus


# 상표 상세 검색한 정보를 가져옴
def trademarkInfoSearchService(query):
    api = kiprisPlus.api_trademarkInfoSearchService
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 출원번호에 대한 지정상품/유사군코드 정보를 가져옴
def trademarkDesignationGoodsinfo(appNumber):
    api = kiprisPlus.api_trademarkDesignationGoodsinfo
    service_key = kiprisPlus.service_key
    query = {"applicationNumber": appNumber.text}
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 지정상품-유사군코드 dict 만들기
def goodCode(soup):
    trademarkdesignationgoodstinfos = soup.select("trademarkdesignationgoodstinfo")
    goodCode = {}
    for k in trademarkdesignationgoodstinfos:
        goodCode[k.select_one("designationgoodshangeulname").text] = k.select_one("similargroupcode").text
    return goodCode

# 유사군코드별 지정상품 딕셔너리 만들기
def codeGood(dict):
    codeGood = {}
    for k, v in dict.items():
        codeGood.setdefault(v, set()).add(k)
    return codeGood


query = {
    "trademarkName" : "",
    "classification" : "",
    "asignProduct" : "의자",
    # "applicationNumber" : "4120060014133",
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
soup = trademarkInfoSearchService(query)
# applicationnumber를 뽑기
appNumbers = soup.select("applicationnumber")
goodCodeTotal = {}
for appNum in appNumbers:
    soup = trademarkDesignationGoodsinfo(appNum)
    goodCodeDict = goodCode(soup)
    # print(goodCodeDict)
    goodCodeTotal.update(goodCodeDict)
    codeGoodDict = codeGood(goodCodeTotal)
print(codeGoodDict)