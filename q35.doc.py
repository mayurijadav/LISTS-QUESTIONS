# 5. Count unique values inside a list.
list = [1, 2, 2, 5, 8, 4, 4, 8]
i=0
a=[]
while i<len(list):
    if (list[i]) not in a:
        a.append(list[i])
    i+=1
print(a)