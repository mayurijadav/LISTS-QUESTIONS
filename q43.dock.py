# a=[3,3,4,5,6,7,8,5,8]
# b=[]
# i=0
# while i<len(a):
#     if a[i] not in b:
#         b.append (a[i])
#     i+=1
# print(b)

# a=[23,34,56,78,98]
# i=0
# max=0
# smax=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif a[i]>smax and smax!=max:
#         smax=a[i]
#     i+=1
# print(max)
# print(smax)



# a=[9,1,1,9]
# i=0
# while i<len(a):
#     print(a[i]*a[i],end=" ")
#     i+=1

# a=["mayu","rani","ketu"]
# i=0
# while i<len(a):
#     print(i,a[i])
#     i+=1

# a=[1,2,34,45,34,23,13,67,45,40,35]
# i=0
# b=[]
# while i <len(a):
#     if a[i]>20 and a[i]<40:
#         b.append (a[i])
#     i+=1
# print(b)


# a=["mayu","rani","toto"]
# i=0
# b=-1
# while i<len(a):
#     print(a[b],end=" ")
#     b-=1
#     i+=1

# a=[23,34,54,56,67]
# count=0
# i=0
# while i<len(a):
#     i+=1
# print(i)

# a=[23,34,54,56,67]
# count=0
# i=0
# while i<len(a):
#     count+=a[i]
#     # count+=1
#     i+=1
# print(count)

# a=[2,3,42,3,73,8,9,6,8]
# i=0
# m=0
# sm=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[j]>m:
#             m=a[j]
#         elif a[j]>sm and a[j]!=m:
#             sm=a[j]
#         j+=1
#     i+=1
# print(sm)


# a=[34,45,6,67,7,56,79]
# i=0
# max=0
# smax=0
# tmax=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         if a[j]>max:
#             max=a[j]
#         elif a[j]>smax and a[j]!=max:
#             smax=a[j]
#         elif a[j]>tmax and a[j]!=max and a[j]!=smax:
#             tmax=a[j]
#         j+=1
#     i+=1
# print(max)
# print(smax)
# print(tmax)


# a=["n","i","t","i","n"]
# i=0
# b=""
# while i<len(a):
#     b=b+a[i]
#     i+=1
# print(b)
# c=b[::-1]
# if b==c:
#     print(" Its palendrom no.")
# else:
#     print("Its not palendrom no.")


# a=["1","2","1"]
# i=0
# b=""
# while i<len(a):
#     b=b+a[i]
#     i+=1
# print(b)
# c=b[::-1]
# if b==c:
#     print("its palendrom")
# else:
# #     print("its not palendrom")

# a=["n","i","t","i","n"]
# i=0
# b=""
# while i<len(a):
#     b=b+a[i]
#     i+=1
# print(b)
# c=b[::-1]
# if b==c:
#     print("its palendrom")
# else:
#     print("its not palendrom")

# i=0
# while i<=10:
#     print(i+1)
#     i+=2

# print(4 or 5)
# a=[102,120,1040,]
# i=0
# b=[]
# while i<len(a):
#     if a[i]!=0:
#         b.append(a[i])
#     else:
#         print("nathing")
#     i+=1
# print(b)




# a=[102,120,1040]
# i=0
# c=str(a[i])
# k=[]
# while i<len(a):
#     j=0
#     b=[]
#     # c=str(a[i])
#     while j<len(c):
#         if c[j]!="0":
#             b.append (c[j])
#         j+=1
#     k.append(b)
#     i+=1
# print(b)



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




 
 

 
 