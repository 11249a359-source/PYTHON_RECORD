try:
   n = 0
   res = 100 / n
except ZeroDivisionError:
   print("You can't divide by zero!")
   n = int(input('enter value '))#GIVE INPUT AS a then check the program
   res = 100 / n
   print(res)
except ValueError:
   print("Enter a valid number!")

else:
   print("Result is", res)

finally:
   print("Execution complete.")
