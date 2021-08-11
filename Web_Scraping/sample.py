import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
url = "https://www.sephora.com/brands-list"

print(requests.get(url=url, headers=headers).text)
