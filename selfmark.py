import urllib.request
import urllib.parse


api = "http://plus.kipris.or.kr/kipo-api/kipi/trademarkInfoSearchService/getWordSearch"
service_key = "서비스키"
query = {
    "searchString": "solev",
    "searchRecentYear": "0"
}

# values 안에 한글이 있으므로 기계가 아는 문자(숫자, 알파벳)으로 인코딩
params = urllib.parse.urlencode(query, doseq=False, safe=' ', encoding=None, errors=None)
url = api + "?" + params + "&ServiceKey=" + service_key

response = urllib.request.urlopen(url)
data = response.read()
print(data.decode("utf-8"))

