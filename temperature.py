tem = [32,34,29,31,28,35,36,30,28,31,32,34,25,29,30]
a = sum(tem)/len(tem)
above_average = 0
for t in tem:
    if t >a:
        above_average +=1

b = max(tem) - min(tem)
print("average temperature =", a)
print("above average =", above_average)
print("temperature difference =", b)