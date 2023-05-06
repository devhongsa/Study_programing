import requests
from urllib.parse import urlencode

res = requests.get("http://openAPI.seoul.go.kr:8088/7275616250676d7233317868675579/json/IndividualServiceChargeService/1/5/").json()

print(res)