with open('text_blog/text_blog_2012.txt', 'r') as main: # change to your file directory 
    o = main.readlines()
for i in range(0,len(o)):           # adjust range if error in formatting
    m = o[i]
    p = []
    for i in m:
        if i == " ":
            break
        else:
            p.append(i) 
    p = "".join(p[2:])
    print(p)
    with open(f'new/blog/text_blog_2012_{p}.txt', 'w',encoding="utf-8") as f:
        f.write(m)