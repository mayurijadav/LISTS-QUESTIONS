# 2. Convert Character Matrix to single String;
list =[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
k=""
while i<len(list):
    j=0
    while j<len(list[i]):
        k=k+(list[i][j])
        j+=1
    i+=1
print(k)