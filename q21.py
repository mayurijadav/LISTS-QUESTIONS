# Write a Code that finds second maximum element from the list and print it.
num=[20,30,40,50,70,80]
i=0
max=0
secondmax=0
while i<len(num):
    if num[i]>max:
        max=num[i]
    elif  num[i]>secondmax and num[i]!=max:
        secondmax=num[i]
    i+=1
print(secondmax)



# num[i]>secondmax and max!=secondmax:
#         secondmax=num[i]