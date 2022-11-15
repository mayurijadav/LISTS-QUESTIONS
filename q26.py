a=[[23,34,45,],89,[45,56,67],[67,78,89]]
b=[]
i=0
while i<len(a):
        if type(a[i])==(list):
            b.extend(a[i])
        else:
            b.append(a[i])
        i+=1
print(b)

















# sum=0
# while i<len(a):
#     j=0
#     while i<len(a[i]):
#         sum=sum+(a[i][j])
#         j+=1
#     print(sum)
#     # j+=1
#     i+=1
# # print(sum)