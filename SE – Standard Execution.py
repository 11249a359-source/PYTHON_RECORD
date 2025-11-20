AIm:To write a Python program to generate and display the Fibonacci series up to a specified number of terms using standard
execution with user-provided first two numbers.

ALGORITHM: Fibonacci Series (SE Version)
1.Start
2.Input the first number (First_Number), the second number (Second_Number), and 
 the total number of terms (Limit) from the user.
3.Define a function fibonacci_series(first, second, n) to generate the Fibonacci
 series.
4.Inside the function:
  a. Print the first number.
  b. Print the second number.
  c. Loop from 1 to n - 2 (since first two numbers are already printed):
  i. Calculate the next number: next_number = first + second
  ii. Print next_number.
  iii. Update first = second and second = next_number.
5.Call the function with the user inputs (First_Number, Second_Number, Limit).
6.End

program:
def fibonacci_series(first, second, n):
    """Generate and print Fibonacci series up to n terms."""
    print("Fibonacci Series:")
    print(first, end=" ")
    print(second, end=" ")
    for i in range(n - 2):
        next_number = first + second
        print(next_number, end=" ")
        first = second
        second = next_number
First_Number = int(input("Enter the first number of the Fibonacci series: "))
Second_Number = int(input("Enter the second number of the Fibonacci series: "))
Limit = int(input("Enter the total number of Fibonacci numbers to display: "))
fibonacci_series(First_Number, Second_Number, Limit)

output:
Enter the first number of the Fibonacci series: 6
Enter the second number of the Fibonacci series: 3
Enter the total number of Fibonacci numbers to display: 5
Fibonacci Series:
6 3 9 12 21 
