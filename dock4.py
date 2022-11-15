# 4. List product excluding duplicates.
#  Output: 60
list = [6,1,3,5,6,3,1]
k=[]
i=0
while i<len(list):
    if list[i] not in k:
        k.append (list[i])
    i+=1
print(len(k))
print(k)


a=[1,2,2,3,4,5,5,8,9,6,4,9,7,7,8]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append (a[i])
    i+=1
print(b)
print(len(b))




