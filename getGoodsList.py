# 상품명으로 검색을 하면, 유사군코드별로 지정상품을 보여줌
# 보여지는 지정상품을 선택하면, 유사군코드가 선택됨

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import getInfoFromApi
import kiprisPlus



# # 상표 상세 검색한 정보를 가져옴
# def trademarkInfoSearchService(query):
#     api = kiprisPlus.api_trademarkInfoSearchService
#     service_key = kiprisPlus.service_key
#     params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
#     url = api + "?" + params + "&ServiceKey=" + service_key
#     request = urllib.request.urlopen(url)
#     xml = request.read()
#     soup = BeautifulSoup(xml, 'html.parser')
#     return soup

# # 출원번호에 대한 지정상품/유사군코드 정보를 가져옴
# def trademarkDesignationGoodsinfo(appNumber):
#     api = kiprisPlus.api_trademarkDesignationGoodsinfo
#     service_key = kiprisPlus.service_key
#     query = {"applicationNumber": appNumber.text}
#     params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
#     url = api + "?" + params + "&accessKey=" + service_key
#     request = urllib.request.urlopen(url)
#     xml = request.read()
#     soup = BeautifulSoup(xml, 'html.parser')
#     return soup

# {지정상품 : 유사군코드}_ 지정상품-유사군코드 dict 만들기
def goods_code_dict(soup):
    list = soup.select("trademarkdesignationgoodstinfo")
    good_code_dict = {}
    for k in list:
        good_code_dict[k.select_one("designationgoodshangeulname").text] = k.select_one("similargroupcode").text
    return good_code_dict

# {유사군코드 : {지정상품1, 지정상품2}}_유사군코드별-지정상품들의 dict 만들기
def code_goods_dict(dict):
    code_goods_dict = {}
    for k, v in dict.items():
        code_goods_dict.setdefault(v, set()).add(k)
    return code_goods_dict

# 출원번호의 리스트를 뽑아서 리턴
def get_appNum(soup):
    return soup.select("applicationnumber")

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

soup = getInfoFromApi.getAdvancedSearch(query)
appNums = get_appNum(soup)

code_goods_output = {}
for appNum in appNums:
    # 출원번호의 지정상품 정보
    soup = getInfoFromApi.trademarkDesignationGoodstInfo({"applicationNumber": appNum.text})
    goods_code_for_one_appNum = goods_code_dict(soup)
    code_goods_output.update(goods_code_for_one_appNum)
# 유사군코드별 상품들로 바꿔줌
code_Goods_Dict = code_goods_dict(code_goods_output)
print(code_Goods_Dict)