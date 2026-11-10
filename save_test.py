import json

data = [{"task":"学字典","done":False}]

with open("test.json","w",encoding="utf-8")as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

print("写完了")