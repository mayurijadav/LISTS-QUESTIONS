# a=[103,406,10120,304]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b)
# print(c)



# a=[2,0,3,0,5,0,1,0]
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]==0:
#         b.append(a[i])
#     else:
#         c.append(a[i])
#     i=i+1
# print(b)
# print(c)
# print(b+c)
    


 


a=[103,406,10120,304]
i=0
l=[]
while i <len(a):
    b=str(a[i])
    j=0
    s=" "
    while j <len(b):
        if b[j]!="0":
            s+=b[j]
        j+=1
    i+=1
    l.append(int(s))
print(l)

            
            


 
