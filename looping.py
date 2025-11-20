Aim: Write a program to print Fibonacci series up to 8.

ALGORITHM: 
1.Start
2.Input the first number, second number, and the total number of Fibonacci numbers to print (Limit) from the user.
Print the first number and the second number.
3.Initialize a loop to run from 1 to Limit - 2 (because first two numbers are already printed).
4.Inside the loop:
a. Calculate the next number as the sum of the first and second numbers:
sum = First_Number + Second_Number
b. Print the sum.
c. Update First_Number to Second_Number.
d. Update Second_Number to sum.
5.Repeat step 5 until the loop ends.
6.End

program:
First_Number = 0
Second_Number = 1
Fibonacii Series = 0 1 1 2 3 5 8 13 21 34 55

First_Number=int(input(“Please enter First Number:”))
Second_Number=int(input(“Please enter First Number:”))
Limit=int(input(“ Number of Fibonacci Numbers to be Print: “))
print(First_Number,end=” “)
print(Second_Number,end=” “)
for i in range(Limit+1):
sum=First_Number+Second_Number
First_Number=Second_Number
Second_Number=sum
print(sum,end=” “)
Output
Please enter First Number:0
Please enter First Number:1
Number of Fibonacci Numbers to be Print: 8
0 1 1 2 3 5 8 13 21 34 55
