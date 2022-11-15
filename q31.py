a=[2,3,1,4,4,5,6,7,8,9,]
b=[2,3,4,5,6]
i=0
c=[]
while i<len(a):
    if a[i]not in(b):
        c.append(a[i])
    i+=1
print(c)


