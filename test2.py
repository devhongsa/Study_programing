import requests
import dart_fss
from urllib.parse import urlencode

corp = "00258801"

obj = dart_fss.api.info.emp_sttus(corp_code=corp,bsns_year='2022',reprt_code='11011',api_key="7ec1d420ec7fa01a2a1c8edf99125bc6b0a9bdc7")

men = obj['list'][0]['rgllbr_co'].replace(',','')
women =obj['list'][1]['rgllbr_co'].replace(',','')

total = int(men)+int(women)
