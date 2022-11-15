a=[23,34,45,[56,[67,45],45],45,89,78]
i=0
count=0
while i<len(a):
    if type(a[i])==(list):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==(list):
                k=0
                while k<len(a[i][j]):
                    count+=1
                    k+=1
            else:
                count+=1
            j+=1
    else:
        count+=1
    i+=1
print(count)




# a=[23,34,45,[56,[67,45],45],78]
# c=0
# for i in a:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 for k in j:
#                     c=c+1
#             else:
#                 c=c+1
#     else:
#         c=c+1
# print(c)



