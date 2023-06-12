#combine blog files 01 to 34 from COCA to a single file for splitting 

def file(p):
    print(p)
    with open(f'text_blog/text_blog_{p}.txt', 'rb') as f:   #change to your file directory#
        lines = f.readlines()
    with open('text_blog_2012.txt','a') as a:  #drag file into your file directory#
        z = []
        for l in lines:
            z.append(l.decode().split("\n")[0])
        for i in z:
            a.write(i)

for i in range(1,35):
    z = str(i)
    if len(z) == 1:
        z = list(z)
        z.insert(0,"0")
        z = "".join(z)
    file(z)

#change blog to web where appropriate