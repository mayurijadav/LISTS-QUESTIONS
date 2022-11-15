# a=["mayuri","pooja","divya","megha"]
# i=0
# count="0"
# b=str(input("enter alfabate"))
# while i<len(a):
#     j=0
#     while i<len(a[i]):
#         if (a[i][i])==b:
#             count=count+a[i][j]
#         count+=1
#     i+=1
# print(count)
 

# a=["teena"]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]=="n":
#             print("n")
#         j+=1
#     i+=1


# a=[10,20,30,40]
# b=[400,300,200,100]
# i=0
# while i<len(a):
#     print(a[i],b[i])
#     i+=1


# a=[10,20,30,40]
# b=[100,200,300,400]
# # c=b(-i)
# i=0
# c=b(-i)
# while i<len(a):
#     print(a[i],c)
#     i+=1


# a="teena"
# i=3
# while i<len(a):
#     print(a[i])
#     i=i+2




d1={"a":1,"b":2,"c":3,"d":4}
# methods in dictnory
# methods for removing kye and value


# d1.pop("b")
# print(d1)
# pop delet the given kye and its values

# d1.popitem()
# print(d1)
# popitem delet the last kye and value

# del d1["c"]
# print(d1)

# del d1
# print(d1)
# delet method delets all things from dictionary keys and values also dictionary name 

# d1.clear()
# print(d1)
# clear just clear the dictionry and gives the empty {} curlybracets

# print (d1.get("c"))
# get only access the kye and give the value

# print(d1.keys())
# kye methods gives the list of kyes only


# print (type(d1.keys()))

# a2=d1.copy
# d1.update({"x":80})
# print(d1)

d1.setdefault("b",7)
print(d1)
# 
d1.setdefault("g",7)
print(d1)

d1.setdefault("z")
print(d1)

