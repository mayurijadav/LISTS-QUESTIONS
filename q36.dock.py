a=[102,120,1040]
i=0
c=[]
while i<len(a):
    n=str(a[i])
    j=0
    b=""
    while j<len(n):
        if n[j]!="0":
            b=b+n[j]
        j=j+1
    c.append(b)
    i+=1
print(c)