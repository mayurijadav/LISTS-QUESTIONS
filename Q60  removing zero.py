
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

            
            
