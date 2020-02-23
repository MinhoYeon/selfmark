import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import kiprisPlus


# 상표 단어 검색
def getWordSearch(query):
    api = kiprisPlus.api_getWordSearch
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 상표 전체 검색
def getAdvancedSearch(query):
    api = kiprisPlus.api_getAdvancedSearch
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup


# 상표 자유 검색
def freeSearchInfo(query):
    api = kiprisPlus.api_freeSearchInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 상표 출원번호 검색
def applicationNumberSearchInfo(query):
    api = kiprisPlus.api_applicationNumberSearchInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 상표 완전일치 검색
def trademarkNameMatchSearchInfo(query):
    api = kiprisPlus.api_trademarkNameMatchSearchInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup


# 상표 서지사항 검색
def getBibliographyDetailInfoSearc(query):
    api = kiprisPlus.api_getBibliographyDetailInfoSearc
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup



# 지정상품 검색
def trademarkDesignationGoodstInfo(query):
    api = kiprisPlus.api_trademarkDesignationGoodstInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 유사군코드 검색
def trademarkSimilarityCodeInfo(query):
    api = kiprisPlus.api_trademarkSimilarityCodeInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# 서지요약정보 검색
def trademarkBiblioSummaryInfo(query):
    api = kiprisPlus.api_trademarkBiblioSummaryInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup


# 지정상품 조회
def trademarkAsignProductSearchInfo(query):
    api = kiprisPlus.api_trademarkAsignProductSearchInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup


# 유사군코드 조회
def trademarkSimilarCodeSearchInfo(query):
    api = kiprisPlus.api_trademarkSimilarCodeSearchInfo
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding="UTF-8", errors=None)
    url = api + "?" + params + "&accessKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup



