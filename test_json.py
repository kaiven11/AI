#coding=utf-8

import json

f1 = open(r"C:\Users\Admin\Desktop\new.json",'a+',encoding="utf-8")

ribao = set()
count = len(ribao)
with open(r"C:\Users\Admin\Desktop\erciqizhu-xy.json", 'r',encoding="utf-8") as f:
    for i in f:
        m = json.loads(i)
        if (m.get('labels')) == []:
            continue

        
        text = "".join(m.get("text").split(":")[1:])
        ribao.add(text)
        
        if count == len(ribao):
            print(i)
            continue

        else:
            count=len(ribao)
            f1.write(i)


        # f1.write(i)
        

        