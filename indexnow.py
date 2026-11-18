# Tell Bing/Naver/Yandex (IndexNow) about every URL in sitemap.xml. Run after a push is live: python3 indexnow.py
import json, re, urllib.request
KEY = "51ae0c249833ebfc7f0563535bb48c5e"
urls = re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml", encoding="utf-8").read())
body = json.dumps({"host": "emotionvault.net", "key": KEY, "keyLocation": f"https://emotionvault.net/{KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", body, {"Content-Type": "application/json; charset=utf-8"})
print(len(urls), "urls ->", urllib.request.urlopen(req).status)
