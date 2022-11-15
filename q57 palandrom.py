a=["mom","dad","simi","ritu"]
i=0
count=0
while i<len(a):
    if a[i]==a[i][::-1]:
        count+=1
    i+=1
print(count,"palendrom hai")
