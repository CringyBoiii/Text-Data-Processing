t = []

#lookup file ID, year and genre in dataset# 

def init():
    with open('new_sources.txt','rb') as f: #new_source.txt is sources file from COCA reformmated to ID#YEAR#GENRE; code not included due to data copyrights
        lines = f.readlines()
    a = []
    for l in lines:
        a.append(l.decode().split("\n")[0])
    for i in a:
        t.append(i.split("#"))
    for m in range(len(t)):
        t[m][2] = t[m][2].split("\r")[0].lower()

init()

# find, copy, and write file into new folder 

b = 0
g = ""
for j in t [0:]:                                #change value in square brackets if code breaks due to formatting errors, to line number in new_source where code breaks]
    if g != f'text_{j[2]}/text_{j[2]}_{j[1]}.txt':
        g = f'text_{j[2]}/text_{j[2]}_{j[1]}.txt'
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
