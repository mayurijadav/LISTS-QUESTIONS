# Let's say you have two lists of the same length. How will you iterate through both the lists together ?
# Code Example

students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
i=0
while i<len(students):
    print(students[i]+(str(marks[i])))
    i+=1
