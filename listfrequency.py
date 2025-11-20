l=[13,4,5,3,4]
l1=[]  # 2,2 , 1
l2=[]  # 3  4   5
print("Element \t \t frequency")
for i in l:
    if i not in l2:
        x=l.count(i)  # i= 3
        l1.append(x)
        l2.append(i)
for i in range (len(l1)):
    print(l2[i],"\t \t \t " , l1[i])
