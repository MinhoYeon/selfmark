import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getWordSearch"
service_key = '서비스키'
query = {
    "searchString": "solev",
    "searchRecentYear": "0"
}

# values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding=None, errors=None)
url = api + "?" + params + "&ServiceKey=" + service_key

request = urllib.request.urlopen(url)
xml = request.read()

# instance 생성
soup = BeautifulSoup(xml, 'html.parser')

items = soup.select("item")
for item in items[:1]:
    listResponseParameter = [
    "agentname", "appreferencenumber", "applicantname", "applicationdate", "applicationnumber",\
    "applicationstatus", "bigdrawing", "classificationcode", "drawing", "fulltext", "indexno",\
    "internationalregisterdate", "internationalregisternumber", "prioritydate", "prioritynumber",\
    "publicationdate", "publicationnumber", "regprivilegename", "regreferencenumber", "registrationdate",\
    "registrationnumber", "registrationpublicdate", "registrationpublicnumber", "title", "viennacode"
    ]
    for i in range(len(listResponseParameter)):
        responseParameter = listResponseParameter[i]
        print("%s : " % (responseParameter), soup.select_one(responseParameter).text)









