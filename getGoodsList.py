import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#
# api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getAdvancedSearch"
# service_key = "8bpZj9hNBYcxmcZmZOTb0Fyuw2pOrYz7KI116PcAyI8="
# query = {
#     "trademarkName" : "",
#     "classification" : "",
#     "asignProduct" : "폰케이스",
#     # "applicationNumber" : "4120060014133",
#     "registerNumber" : "",
#     "publicationNumber" : "",
#     "registrationPublicNumber" : "",
#     "internationalRegisterNumber" : "",
#     "priorityNumber" : "",
#     "applicationDate" : "20200212~20200212",
#     "registerDate" : "",
#     "publicationDate" : "",
#     "registrationPublicDate" : "",
#     "priorityDate" : "",
#     "internationalRegisterDate" : "",
#     "applicantName" : "",
#     "agentName" : "",
#     "viennaCode" : "",
#     "regPrivilegeName" : "",
#     "freeSearch" : "",
#     "similarityCode" : "",
#     "application" : "true",
#     "registration" : "true",
#     "refused" : "true",
#     "expiration" : "true",
#     "withdrawal" : "true",
#     "publication" : "true",
#     "cancel" : "true",
#     "abandonment" : "true",
#     "trademark" : "true",
#     "serviceMark" : "true",
#     "trademarkServiceMark" : "true",
#     "businessEmblem" : "true",
#     "collectiveMark" : "true",
#     "internationalMark" : "true",
#     "character" : "true",
#     "figure" : "true",
#     "compositionCharacter" : "true",
#     "figureComposition" : "true",
#     "numOfRows" : "20",
#     "pageNo" : "1"
# }
#
# # values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
# # "UTF-8"은 대문자로 써야함.
# params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
# url = api + "?" + params + "&ServiceKey=" + service_key
# # print("url: ", url)
#
# request = urllib.request.urlopen(url)
#
# # text로 읽어들임
# xml = request.read()
# # print(xml)

xml = """
b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><response><header><requestMsgID></requestMsgID><responseTime>2020-02-17 23:42:03.423</responseTime><responseMsgID></responseMsgID><successYN>Y</successYN><resultCode>00</resultCode><resultMsg>NORMAL SERVICE.</resultMsg></header><body><items><item><agentName>\xec\x98\xa4\xec\xa2\x85\xea\xb7\xbc</agentName><appReferenceNumber></appReferenceNumber><applicantName>\xec\xa0\x95\xec\x9d\x98\xec\x88\x98</applicantName><applicationDate>20200212</applicationDate><applicationNumber>4020200023447</applicationNumber><applicationStatus>\xec\xb6\x9c\xec\x9b\x90</applicationStatus><bigDrawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ad7a17eeeef6e4ea4b5e22ef00dd3e29df616987ef7331e91117c922c6e054c1341f86bb32d7454cf30614925974cc16ef2767013f1f5d47</bigDrawing><classificationCode>09</classificationCode><drawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e251697a9d72a91344f20ce8245b099a8a3fe34ea28dcde802acd308f4afc103e011b0dcde2765c7eabee2b76812b5dc0b</drawing><fullText>N</fullText><indexNo>1</indexNo><internationalRegisterDate></internationalRegisterDate><internationalRegisterNumber></internationalRegisterNumber><priorityDate></priorityDate><priorityNumber></priorityNumber><publicationDate></publicationDate><publicationNumber></publicationNumber><regPrivilegeName></regPrivilegeName><regReferenceNumber></regReferenceNumber><registrationDate></registrationDate><registrationNumber></registrationNumber><registrationPublicDate></registrationPublicDate><registrationPublicNumber></registrationPublicNumber><title></title><viennaCode></viennaCode></item><item><agentName></agentName><appReferenceNumber></appReferenceNumber><applicantName>\xec\x84\x9c\xea\xb2\xbd\xed\x9b\x88</applicantName><applicationDate>20200212</applicationDate><applicationNumber>4020200022900</applicationNumber><applicationStatus>\xec\xb6\x9c\xec\x9b\x90</applicationStatus><bigDrawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ad7a17eeeef6e4ea4b5e22ef00dd3e29df616987ef7331e9cc13bc018a985a4a8e771203f27c4b53a6b1d0681c4580e24d1009008eccbf1d</bigDrawing><classificationCode>09</classificationCode><drawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e251697a9d72a91344f20ce8245b099a8a21ad5636c95bb71b804290e0e290e97b0ca57c1fdfed0ab6a00291267bfff004</drawing><fullText>N</fullText><indexNo>2</indexNo><internationalRegisterDate></internationalRegisterDate><internationalRegisterNumber></internationalRegisterNumber><priorityDate></priorityDate><priorityNumber></priorityNumber><publicationDate></publicationDate><publicationNumber></publicationNumber><regPrivilegeName></regPrivilegeName><regReferenceNumber></regReferenceNumber><registrationDate></registrationDate><registrationNumber></registrationNumber><registrationPublicDate></registrationPublicDate><registrationPublicNumber></registrationPublicNumber><title></title><viennaCode></viennaCode></item><item><agentName>\xed\x99\xa9\xeb\xb3\xb4\xec\x9d\x98</agentName><appReferenceNumber></appReferenceNumber><applicantName>\xec\x9c\xa0\xed\x95\x9c\xed\x9a\x8c\xec\x82\xac \xec\x95\x84\xec\x9d\xb4\xec\x97\xa0\xec\x9c\x84\xec\xa6\x88</applicantName><applicationDate>20200212</applicationDate><applicationNumber>4020200022888</applicationNumber><applicationStatus>\xec\xb6\x9c\xec\x9b\x90</applicationStatus><bigDrawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ad7a17eeeef6e4ea4b5e22ef00dd3e29df616987ef7331e9cc13bc018a985a4ab617f3e63ca00553c5c80c7b45fe90c52f353276b5ad0857</bigDrawing><classificationCode>09</classificationCode><drawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e251697a9d72a91344f20ce8245b099a8a21ad5636c95bb71bc0663ca0a2871b2cf916c3c812ead9bb49fad6b16d648bfb</drawing><fullText>N</fullText><indexNo>3</indexNo><internationalRegisterDate></internationalRegisterDate><internationalRegisterNumber></internationalRegisterNumber><priorityDate></priorityDate><priorityNumber></priorityNumber><publicationDate></publicationDate><publicationNumber></publicationNumber><regPrivilegeName></regPrivilegeName><regReferenceNumber></regReferenceNumber><registrationDate></registrationDate><registrationNumber></registrationNumber><registrationPublicDate></registrationPublicDate><registrationPublicNumber></registrationPublicNumber><title></title><viennaCode></viennaCode></item><item><agentName>\xec\xb5\x9c\xed\x9a\xa8\xec\x84\xa0</agentName><appReferenceNumber></appReferenceNumber><applicantName>\xec\xa1\xb0\xeb\x82\xa8\xec\x9b\x85</applicantName><applicationDate>20200212</applicationDate><applicationNumber>4020200023190</applicationNumber><applicationStatus>\xec\xb6\x9c\xec\x9b\x90</applicationStatus><bigDrawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ad7a17eeeef6e4ea4b5e22ef00dd3e29df616987ef7331e91117c922c6e054c1666df0f80adc2487fccd8bf96f9b7090307492dc26de48b9</bigDrawing><classificationCode>09</classificationCode><drawing>http://plus.kipris.or.kr/kiprisplusws/fileToss.jsp?arg=ed43a0609e94d6e251697a9d72a91344f20ce8245b099a8a3fe34ea28dcde8025433392d4b0abfdea5533a3a995f8644ccd5210b3196c77d</drawing><fullText>N</fullText><indexNo>4</indexNo><internationalRegisterDate></internationalRegisterDate><internationalRegisterNumber></internationalRegisterNumber><priorityDate></priorityDate><priorityNumber></priorityNumber><publicationDate></publicationDate><publicationNumber></publicationNumber><regPrivilegeName></regPrivilegeName><regReferenceNumber></regReferenceNumber><registrationDate></registrationDate><registrationNumber></registrationNumber><registrationPublicDate></registrationPublicDate><registrationPublicNumber></registrationPublicNumber><title></title><viennaCode></viennaCode></item></items></body><count><numOfRows>20</numOfRows><pageNo>1</pageNo><totalCount>4</totalCount></count></response>'
"""
# text를 태깅 가능한 xml으로 변환
soup = BeautifulSoup(xml, 'html.parser')
# print(soup)

# # 응답파라미터리스트를 추출하기
# firstItem = soup.find("item")
# listResponseParameter = []
# for tag in firstItem.find_all(True):
#     listResponseParameter.append(tag.name)
# # print(listResponseParameter)

# # 응답파라미터 값 출력하기
# items = soup.select("item")
# for item in items:
#     # print(item)
#     # 응답파라미터를 받아서 하나씩 출력하기
#     print("--------------------------------------")
#     for i in range(len(listResponseParameter)):
#         responseParameter = listResponseParameter[i]
#         print("%s : " % (responseParameter), item.select_one(responseParameter).text)

# applicationnumber를 뽑기
applicationnumbers = soup.select("applicationnumber")
for applicationnumber in applicationnumbers:
    #trademarkDesignationGoodsinfo의 코드
    api = "http://plus.kipris.or.kr/openapi/rest/trademarkInfoSearchService/trademarkDesignationGoodstInfo"
    service_key = "8bpZj9hNBYcxmcZmZOTb0Fyuw2pOrYz7KI116PcAyI8="
    query = {"applicationNumber" : applicationnumber.text}

    # values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')

    # 유사군코드를 집합으로 모으기
    similarGroupCodeSet = set([])
    similargroupcodes = soup.select("similargroupcode")
    for similargroupcode in similargroupcodes:
        similarGroupCodeSet.add(similargroupcode.text)
    similarGroupCodeList = list(similarGroupCodeSet)

    # 유사군코드별 지정상품 딕셔너리 만들기
    trademarkdesignationgoodstinfos = soup.select("trademarkdesignationgoodstinfo")
    goodsSimlilarGroupCode = {}
    goodsSimilar = set([])
    for i in range(len(similarGroupCodeList)):
        goodsSimilar = set([])
        for trademarkdesignationgoodstinfo in trademarkdesignationgoodstinfos:
            if similarGroupCodeList[i] == trademarkdesignationgoodstinfo.select_one("similargroupcode").text:
                goodsSimilar.add(trademarkdesignationgoodstinfo.select_one("designationgoodshangeulname").text)
        goodsSimlilarGroupCode[similarGroupCodeList[i]] = list(goodsSimilar)
    print(goodsSimlilarGroupCode)





