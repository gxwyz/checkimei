# import urllib, urllib2, sys
# import ssl
import requests
import time
import json
import logging

logger = logging.getLogger(__name__)

host = 'http://api.3023data.com'
path = '/imei/imei'
method = 'GET'
key = 'your key'
headers={
"key": key,
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}

# imei = '356115110999139'

with open('testimei.txt', 'r', encoding='utf-8') as f:
    for imei in f:
        imei = imei.replace('\n', '')
        imei = imei.replace(' ', '')
        querys = 'imei=' + imei
        url = host + path + '?' + querys

        res = requests.get(url,headers=headers)
        time.sleep(3)
        content = res.text
        if (content):
            with open('saveimei.txt', 'a', encoding='utf-8') as f2:
                f2.write(content)
                json_str = json.loads(content)['data']
                print('保存imei：{}，品牌：【{}】，{}，型号：{}'.format(json_str['imei'],json_str['brand'],json_str['name'],json_str['model']))
                # print(CalcImeiChecksum(imei))
                f2.write('\n')
                f2.close()