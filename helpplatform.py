re={}
al={}

while(True):
    print("select 1 for request")
    print("select 2 for skills avaible")
    print("enter any other number to exit")
    i = int(input())
    if i ==1:
        n=input("enter ur name")
        r=input("enter ur request")
        re[r]=n
        if r in al:
            print(al[r] , "can help u")
    elif i==2:
        s=input("enter ur skill ")
        n= input("enter ur name")
        al[s]=n
        if s in re:
            print("u can help ", re[s])

    else:
        break


