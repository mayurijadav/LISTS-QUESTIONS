a=[[23,34,43],23]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if a[i]==a[i][j]:
                b.append(a[i])
            else:
                j+=1
    else:
        i+=1
print(b)
