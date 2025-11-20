AIM:To write a Python program to generate and display the Fibonacci series 
       up to a specified number of terms, using user input for the 
                                                                                                                              first two numbers of the series.
ALGORITHM: Fibonacci Series Program
1.Start
2.Input the first number (First_Number), the second number (Second_Number), and
the total number of terms (Limit) from the user.
3.Print the first number and the second number.
4.Initialize a loop from 1 to Limit - 2(since the first two numbers are already printed).
5.Inside the loop:
a. Calculate the next number:
  sum = First_Number + Second_Number
  b. Print the sum.
  c. Update First_Number to Second_Number.
  d. Update Second_Number to sum.
6.Repeat step 5 until the loop ends.
7.End

program:
First_Number = int(input("Enter the first number of the Fibonacci series: "))
Second_Number = int(input("Enter the second number of the Fibonacci series: "))
Limit = int(input("Enter the total number of Fibonacci numbers to display: "))
print("\nFibonacci Series:")
print(First_Number, end=" ")
print(Second_Number, end=" ")
for i in range(Limit - 2):  # Already printed first two numbers
    next_number = First_Number + Second_Number
    print(next_number, end=" ")
    First_Number = Second_Number
    Second_Number = next_number

output:
Enter the first number of the Fibonacci series: 2
Enter the second number of the Fibonacci series: 6
Enter the total number of Fibonacci numbers to display: 3
Fibonacci Series:
2 6 8 
