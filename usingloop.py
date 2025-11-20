def print_patle(height):
    for i in range(height):
        for j in range(height):
            if i == j:
                print("*",end = "")
            else:
                print(" ",end = "")
    print()
height = 5
print_patle(5)