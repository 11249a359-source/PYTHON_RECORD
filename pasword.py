s = "R@BB@_0MMMHHH9$"
if (len(s) >= 8):
   for i in s:
       if (i.islower()):
           lower += 1
       if (i.isupper()):
           upper += 1
       if (i.isdigit()):
           digit += 1
       if (i == '@' or i == '$' or i == '_'):
           p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(s)):
    print("Password is valid")
else:
   if (u == 0):
       print("upper_case is missing")
   elif (l == 0):
       print("lower_case is missing")
   elif (d == 0):
       print('digit is missing')
   elif (p == 0):
       print('symbol is missing')
print("Invalid Password")
