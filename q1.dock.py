# 1. Iterate over both the values in a list and their indices
a= ['flour','cheese','carrots']
# print(a[0],a[1],a[2])
# print(0,a[0])
# print(1,a[1])
# print(2,a[2])
i=0
while i<=3:
    j=0
    while j==i:
        print(j,a[i])
        j+=1
        i+=1

