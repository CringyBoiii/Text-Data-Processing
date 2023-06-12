t = []
def init():
    with open('mov.txt','rb') as f:  #manually copied into mov.txt
        lines = f.readlines()
    a = []
    for l in lines:
        a.append(l.decode().split("\n")[0])
    for i in a:
        t.append(i.split("#"))
    for m in range(len(t)):
        t[m][2] = t[m][2].split("\r")[0].lower()
init()
b = 8095 #line in datafile that marks movies from tvm in sources
g = ""
for j in t[8095:]:
    if g != f'text_tvm/text_tvm_{j[1]}.txt':
        g = f'text_tvm/text_tvm_{j[1]}.txt'
        with open(g, 'rb') as k:
            o = k.readlines()
        b = 0
    m = o[b].decode()
    b += 1
    p = []
    for i in m:
        if i == " ":
            break
        else:
            p.append(i)
    p = "".join(p[2:])
    with open(f'new/{j[2]}/text_{j[2]}_{j[1]}_{p}.txt', 'w',encoding="utf-8") as f:
        f.write(m)
    print(p)