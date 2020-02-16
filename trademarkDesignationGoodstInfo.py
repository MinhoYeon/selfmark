## 유사군코드 별 지정상품을 모으기

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkDesignationGoodstInfo"
service_key = "8bpZj9hNBYcxmcZmZOTb0Fyuw2pOrYz7KI116PcAyI8="

query = {"applicationNumber" : "4020200022888"}

# values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
url = api + "?" + params + "&accessKey=" + service_key
# print("url: ", url)

request = urllib.request.urlopen(url)
# print("request: ", request)

# text로 읽어들임
xml = request.read()
# print("xml: ", xml)

# text를 태깅 가능한 xml으로 변환
soup = BeautifulSoup(xml, 'html.parser')
# print("soup: ", soup)

# # 응답파라미터리스트를 추출하기
# firstItem = soup.find("trademarkdesignationgoodstinfo")
# # print("firstItem: ", firstItem)
# listResponseParameter = []
# for tag in firstItem.find_all(True):
#     listResponseParameter.append(tag.name)
# # print("listResponseParameter: ", listResponseParameter)

# #1 응답파라미터 값 출력하기
# trademarkdesignationgoodstinfos = soup.select("trademarkdesignationgoodstinfo")
# for trademarkdesignationgoodstinfo in trademarkdesignationgoodstinfos:
#     # print(trademarkdesignationgoodstinfo)
#     # 응답파라미터를 받아서 하나씩 출력하기
#     print("--------------------------------------")
#     for i in range(len(listResponseParameter)):
#         responseParameter = listResponseParameter[i]
#         print("%s : " % (responseParameter), trademarkdesignationgoodstinfo.select_one(responseParameter).text)

# #2 같은 유사군코드 별로 지정상품을 모으기_딕셔너리
# trademarkdesignationgoodstinfos = soup.select("trademarkdesignationgoodstinfo")
# j = 0
# main_goodstinfo = {}
# for goodstinfo in trademarkdesignationgoodstinfos:
#     # print("====================================")
#     # print(goodstinfo)
#     sub_goodstinfo = {}
#     for i in range(len(listResponseParameter)):
#         # print(listResponseParameter[i])
#         sub_goodstinfo[listResponseParameter[i]] = goodstinfo.select_one(listResponseParameter[i]).text
#     # print(sub_goodstinfo)
#     main_goodstinfo[j] = sub_goodstinfo
#     j+=1
# # print(main_goodstinfo)
#

# 유사군코드를 집합으로 모으기
similarGroupCodeSet = set([])
similargroupcodes = soup.select("similargroupcode")
for similargroupcode in similargroupcodes:
    similarGroupCodeSet.add(similargroupcode.text)
similarGroupCodeList = list(similarGroupCodeSet)
# print(similarGroupCodeList)

# 유사군코드별 지정상품 딕셔너리 만들기
trademarkdesignationgoodstinfos = soup.select("trademarkdesignationgoodstinfo")
goodsSimlilarGroupCode = {}
goodsSimilar = set([])
for i in range(len(similarGroupCodeList)):
    goodsSimilar = set([])
    for trademarkdesignationgoodstinfo in trademarkdesignationgoodstinfos:
        # print(trademarkdesignationgoodstinfo.select_one("similargroupcode").text)
        # print(trademarkdesignationgoodstinfo.select_one("designationgoodshangeulname").text)
        # print(similarGroupCodeList[1])
        if similarGroupCodeList[i] == trademarkdesignationgoodstinfo.select_one("similargroupcode").text:
            goodsSimilar.add(trademarkdesignationgoodstinfo.select_one("designationgoodshangeulname").text)
    goodsSimlilarGroupCode[similarGroupCodeList[i]] = list(goodsSimilar)
print(goodsSimlilarGroupCode)

