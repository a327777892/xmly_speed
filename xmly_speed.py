# -*- coding:utf-8 -*-

import requests
import json

url = "https://jxjkhd.kerlala.com/activity/autographnew/register/31/jmXXMKmd"
headers = {
    'Authorization': 'Bearer',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate, br',
    #下方自己数据
    'X-XSRF-TOKEN': 'eyJpdiI6InNuRDJ2clVydGVUVWhLckNDRFowZWc9PSIsInZhbHVlIjoiU1hkQ29zYXp3Z1Jtam5sYnowc0RcL0hoSW02c0RnNWVyWEQweVZ6dEx3eEhHQld3K1JQU1JCZGRKeXhCNm9hUGsiLCJtYWMiOiJmYjhkZjk0ODUyNjg0MDQ4MWIzMGI4MDU2MjljMmYwY2JkMTZkN2FlMjhkZDNiOGMyOTJlNmZmNTA5MWE0YTUzIn0=',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://jxjkhd.kerlala.com',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 CCBSDK/2.4.0/CloudMercWebView',
    'Referer': 'https://jxjkhd.kerlala.com/a/31/jmXXMKmd/index?cityid=330100&userCityId=110000&u=578749ef-e658-4fba-a40f-e49df50c6050',
    'Content-Length': '0',
    'Connection': 'keep-alive',
    'X-CSRF-TOKEN':'',
    #下方自己数据
    'Cookie': 'XSRF-TOKEN=eyJpdiI6InNuRDJ2clVydGVUVWhLckNDRFowZWc9PSIsInZhbHVlIjoiU1hkQ29zYXp3Z1Jtam5sYnowc0RcL0hoSW02c0RnNWVyWEQweVZ6dEx3eEhHQld3K1JQU1JCZGRKeXhCNm9hUGsiLCJtYWMiOiJmYjhkZjk0ODUyNjg0MDQ4MWIzMGI4MDU2MjljMmYwY2JkMTZkN2FlMjhkZDNiOGMyOTJlNmZmNTA5MWE0YTUzIn0%3D; _session=eyJpdiI6IlNJZHNBbTBFMjFvSmRxaWJPRDUwbFE9PSIsInZhbHVlIjoiNUs1MnVnTG5POWZHXC90MnpibXZna0VSNlFNM1dCZ0hwd0ZwUFZWUXloa3h4VnhZZzh2bkJ6NXAxMWFZbFJLT2wiLCJtYWMiOiIwNmNkNjVhMzljNTdkMzI5ZGI2YTM2OGI4MDNhNmU2ZmMyOTE5YThhMTIyYzA3NDAzZThiODEzNTAwY2FjNGM1In0%3D; acw_tc=0e1d289516149705476963753e40f3fbdd7f8344295cd1493a6484b484; uid=CgIAEWAyjncuYByKAxEeAg=='
}
res = requests.post(url,headers=headers)
result = json.loads(res.content)
headers1 = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    }
if result['code'] == 10002:
    url1 = "https://sc.ftqq.com/SCT4665TFVeeQeY1LPtYlJ8scrnwHroz.send?text="+result['message']
    requests.get(url1,headers=headers1)
elif result['code'] == 20001:
    print('签到成功')
else:
    url1 = "https://sc.ftqq.com/SCT4665TFVeeQeY1LPtYlJ8scrnwHroz.send?text=token失效/领券成功！"
    requests.get(url1, headers=headers1)

#{'status': 'success', 'code': 10002, 'message': '签到成功', 'data': ''}
