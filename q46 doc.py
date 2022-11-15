# . Write a program to print the following using while loop
# Puja Na. First 10 Even numbers
# b. First 10 Odd numbers
# c. First 10 Natural numbers
# d. First 10 Whole numbers

i=0
while i<=10:
    if i%2==0:
        print("it is even no")
    if i%2!=0:
        print("odd no")
    if i>=1:
        print(i,"natural no")
    if i>=0:
        print("whole no")
    i+=1