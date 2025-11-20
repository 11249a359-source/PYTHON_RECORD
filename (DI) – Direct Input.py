AIM:To write a Python program to generate and display the Fibonacci series up to a specified number of terms using pre-defined (directly assigned)
     values for the first two numbers and the total number of terms.

ALGORITHM: 
ibonacci Series Program (Direct Input)
Step 1: Directly assign the first two numbers and the limit
Step 2: Print the first two numbers
Step 3: Generate the remaining Fibonacci numbers

program:
First_Number = 0
Second_Number = 1
Limit = 10  # Number of Fibonacci numbers to print
print("Fibonacci Series:")
print(First_Number, end=" ")
print(Second_Number, end=" ")
for i in range(Limit - 2):  # Already printed first two numbers
    next_number = First_Number + Second_Number
    print(next_number, end=" ")
    First_Number = Second_Number
    Second_Number = next_number

output:
Fibonacci Series:
0 1 1 2 3 5 8 13 21 34 
