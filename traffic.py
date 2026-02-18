import psutil
allowed_port =[62270,62440,49666,5353,445]
sus_list=[]
p=psutil.net_connections()
for i in p:
    # print(i)
    # print(i.pid,"-->",i.laddr.port)
    if i.laddr.port not in allowed_port:
        # print(i.pid,"-->", i.laddr.port)
        sus_list.append((i.pid,i.laddr.port))

print(sus_list)