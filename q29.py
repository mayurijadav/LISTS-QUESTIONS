l=[[23,34,45,[34],34],[34,56,[23]]]
i=0
c=0
while i<len(l):
    if type(l[i])==(list):
        j=0
        while j<len(l[i]):
            if type(l[i][j])==(list):
                k=0
                while k<len(l[i][j]):
                    c+=1
                    k+=1
            else:
                c+=1
            j+=1
    else:
        c+=1
    i+=1
print(c)

# a=[[23,45,34,],[34,56],[34,67,67]]
# c=0
# for i in a:
#     if type(i)==(list):
#         for j in i:
#             if type (j)==(list):
#                 for k in j:
#                     c+=1
#             else:
#                 c+=1
#     else:
#         c+=1
# print(c)
       






