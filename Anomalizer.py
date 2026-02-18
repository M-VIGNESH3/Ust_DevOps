from collections import Counter
f=open('C:/Users/Admin/Desktop/temp/log.txt')
l=f.read()

f.close()
ll=l.split('\n')
l=l.split()
# print(l)

# print(l)
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
s=sum(d.values())
rl=[]
print(s)
for i in d.keys():
    t=d[i]
    
    if round((t/s)*100,3) < 1:
        
        rl.append(i)

print(d)
print(rl)
c=1
for i in ll:
    for j in rl:
        if j in i:
            print(c)
    c+=1

