# IF it is divisible by the sum of digit

# ex  156
# 156= 1+5+6 = 12
# 156%12==0 
# 156 is a harshad no
  



a=int(input("enter no"))
i=0
s=0
while i>0:
    s=s+i%10
    i=i//10

if a%5==0:
    print("yes")

else:
    print("no")
