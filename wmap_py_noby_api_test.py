import urllib.request,urllib.parse
import json
import os

params = {
    "appkey": "xxxxxxxxxxxxxxxxxxxxxxxxxx",
    "text": "めかぶは体にいいって本当ですか？",
    "persona": "0",
    "study": "1",
    }
p = urllib.parse.urlencode(params)
url = "https://www.cotogoto.ai/webapi/noby.json?" + p
print(url)

with urllib.request.urlopen(url) as res:
    html = res.read().decode("utf-8")
    print(html)
    
    data = json.loads(html)

    print(data["text"])
    print(data["commandId"])
    
if data["commandId"] == "ipconfig_exe":
    cmd = "ipconfig /all > C:/Users/hogehoge/Desktop/ipconfig.txt"
    os.system(cmd)
    