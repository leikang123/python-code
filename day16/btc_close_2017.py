# 只做交易收盘
import requests
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req =requests.get(json_url)
#将数据库写入文件
with open('btc_close_2017_request.json','w')as f:
     f.write(req.text)
file_request = req.json()
