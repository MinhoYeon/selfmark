import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import kiprisPlus


query = {
    "searchString": "solev",
    "searchRecentYear": "0"
}
def trademarkInfoSearchService(query):
    api = kiprisPlus.api_trademarkInfoSearchService
    service_key = kiprisPlus.service_key
    params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding=None, errors=None)
    url = api + "?" + params + "&ServiceKey=" + service_key
    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, 'html.parser')
    return soup

# item이 한 사건을 의미함
soup = trademarkInfoSearchService(query)
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









