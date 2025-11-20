number = int(input("Enter a integer  ="))
factorial = 1

if number < 0:
    print("factorial of negative number is not possible")
else:
    for i in range(1,number+1):
        factorial *= i
    print(f"factorial of {number} is {factorial}")
