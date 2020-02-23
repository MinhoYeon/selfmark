#쿼리를 받아서 전체 검색 결과를 보여주기

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import kiprisPlus
import getInfoFromApi

# 응답 파라미터의 리스트 구하기
def getListOfResponsePara(soup):
    listOfResponsePara = []
    for tag in soup.find("item").find_all(True):
        listOfResponsePara.append(tag.name)
    return listOfResponsePara
# 응답 파라미터의 정보를 출력하기
def showInfoResponse(soup, listOfResponsePara):
    for item in soup.select("item"):
        for i in range(len(listOfResponsePara)):
            print("%s : " % (listOfResponsePara[i]), soup.select_one(listOfResponsePara[i]).text)
    return

# 상표 상세 검색한 정보를 가져옴
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
soup = getInfoFromApi.getAdvancedSearch(query)
# 응답 파라미터의 리스트
listOfResponsePara = getListOfResponsePara(soup)
# 상표 전체검색 정보를 보여줌
showInfoResponse(soup, listOfResponsePara)





