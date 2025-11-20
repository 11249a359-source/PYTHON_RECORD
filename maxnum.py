list1 =[100,200,300,400,500]
max_number = list1[0]

for i in list1:
    if max_number<i:
        max_number = i
print(list1)
print(f"max nnumber in list:{max_number}")