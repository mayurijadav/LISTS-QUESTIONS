# 9. Find the First Maximum, Second maximum, Third maximum number from the List.
a=[2,3,4,5,8,9,78,54,34]
i=0
max=0
secmax=0
thirdmax=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    if a[i]>secmax and a[i]!=max:
        secmax=a[i]
    if a[i]>thirdmax and a[i]!=secmax and a[i]!=max:
        thirdmax=a[i]
    i+=1
print(max)
print(secmax)
print(thirdmax)
   


# list=[23,33,56,78,90,45,67,98]
# max=0
# secondmax=0
# thirdmax=0
# i=0
# while i<len(list):
#     if list[i]>max:
#         max=list[i]
#     elif list[i]>secondmax and list[i]!=max:
#         secondmax=list[i]
#     elif list[i]>thirdmax and list[i]!=max and list[i]!=secondmax:
#         thirdmax=list[i]
#     i+=1
# print(max)
# print(secondmax)
# print(thirdmax)

# a=[2,3,45,5,6,9]
# del a[2:4]
# print(id(a))
# a.append(99)
# print(id(a))