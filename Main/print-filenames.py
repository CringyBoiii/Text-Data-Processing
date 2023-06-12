import os
path = r"E:\new2\text_acad"
dir_list = os.listdir(path)
list_ID = []
for i in dir_list:
    list_ID.append (i)

with open('all.txt','w') as f:
    for i in list_ID:
        f.writelines (i)
        f.write('\n')

 
    
