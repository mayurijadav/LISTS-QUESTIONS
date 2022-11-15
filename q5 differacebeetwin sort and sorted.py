# difference between sort and sorted
#           sort                             sorted 
# 1.sort gives directly sorted list.| 1.sorted gives sortedlist by using another variable
# 2. with using l.sort() .print(l)   |2.with using l1=sorted.l . print(l1)
# example
# a=[1,2,43,82,5,3,6]               |# a=[1,2,43,82,5,3,6]
# a.sort ()                         |# a1=sorted(a)
# print(a)                          |# print(a1)            
# output=[1,2,3,5,6,43,82]          |output=[1,2,3,5,6,43,82]



# a=[1,2,43,82,5,3,6]               |# a=[1,2,43,82,5,3,6]
# a.sort (reverse=True)             | a1=sorted(a)
# print(a)                          | print(a1)
# output=[82,43,6,5,3,2,1]          |# output=[82,43,6,5,3,2,1]
