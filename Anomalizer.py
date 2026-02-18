from collections import Counter
f=open('C:/Users/Admin/Desktop/temp/log.txt')
l=f.read()
f.close()
l=l.split('\n')
print(l)

# print(l)
d={}
for i in l:
    t=i.split()
    for j in t:
        
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
print(d.values())