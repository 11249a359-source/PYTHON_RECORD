AIM:
To Write a function called isphonenumber () to recognize a pattern 415-555-4242 without using
regular expression and also write the code to recognize the same pattern using regular expression.

ALGORITHM:
Without using Regular Expressions
1. Define a function isphonenumber(s)
2. Check if the length of s is exactly 12
3. Check:
1. Characters at index 3 and 7 are -
2. All other characters are digits
4. If all conditions are true, return True; else return False
Using Regular Expressions
1. Import the re module
2. Define the pattern: ^\d{3}-\d{3}-\d{4}$
1. \d{3}: 3 digits
2. -: hyphen
3. \d{4}: 4 digits
3. Use re.fullmatch() to match the string against the pattern
4. Return True if matched, else False

PROGRAM WITHOUT USING REGULAR EXPRESSION
def isphonenumber(s):
if len(s) != 12:
return False
if s[3] != &#39;-&#39; or s[7] != &#39;-&#39;:
return False
if not (s[0:3].isdigit() and s[4:7].isdigit() and s[8:12].isdigit()):
return False
return True

29 | P a g e

# Sample test
print(&quot;Without regex:&quot;)
print(isphonenumber(&quot;415-555-4242&quot;)) # True
print(isphonenumber(&quot;415-55A-4242&quot;)) # False
print(isphonenumber(&quot;415-5555-242&quot;)) # False

PROGRAM USING REGULAR EXPRESSION
import re
def isphonenumber_regex(s):
pattern = r&quot;^\d{3}-\d{3}-\d{4}$&quot;
return bool(re.fullmatch(pattern, s))
# Sample test
print(&quot;\nWith regex:&quot;)
print(isphonenumber_regex(&quot;415-555-4242&quot;)) # True
print(isphonenumber_regex(&quot;415-55A-4242&quot;)) # False
print(isphonenumber_regex(&quot;4155554242&quot;)) # False

OUTPUT:

Without regex:
True
False
False

With regex:
True
False
False
