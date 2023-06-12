with open('text_web/text_web_2012.txt', 'rb') as main:
    o = main.readlines()
for i in range(87070,len(o)):
    m = o[i].decode()
    p = []
    for i in m:
        if i == " ":
            break
        else:
            p.append(i) 
    p = "".join(p[2:])
    print(p)
    with open(f'new/web/text_web_2012_{p}.txt', 'w',encoding="utf-8") as f:
        f.write(m)
        