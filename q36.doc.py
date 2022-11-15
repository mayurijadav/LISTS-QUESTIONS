# 9. Find the First Maximum, Second maximum, Third maximum number from the List.
a=[23,34,56,58,89,67]
i=0
max=0
smax=0
tmax=0
while i<len(a):
    if (a[i])>max:
        max=(a[i])
    elif (a[i])>smax and (a[i])!=max:
        smax=(a[i])
    i+=1
print(max)
print(smax)
# print(tmax)