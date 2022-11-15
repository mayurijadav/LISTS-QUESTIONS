# # 12. You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'
 
a=[12,23,34,54,33,40,45,56]
i=0
count=0
while i<len(a):
    if a[i]>=20 and a[i]<=40:
        count=count+1
    i+=1
print(count)

 
 