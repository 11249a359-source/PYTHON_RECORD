class PalindromeChecker:
    def is_palindrome(self, value):
        pass

class StringPalindrome(PalindromeChecker):
    def is_palindrome(self, value):
        value = value.lower()
        return value == value[::-1]

class NumberPalindrome(PalindromeChecker):
    def is_palindrome(self, value):
        value = str(value)
        return value == value[::-1]

str_checker = StringPalindrome()
num_checker = NumberPalindrome()

string_input = input("Enter a string: ")
num_input = int(input("Enter an integer: "))

if str_checker.is_palindrome(string_input):
    print(f"'{string_input}' is a palindrome string.")
else:
    print(f"'{string_input}' is not a palindrome string.")

if num_checker.is_palindrome(num_input):
    print(f"{num_input} is a palindrome number.")
else:
    print(f"{num_input} is not a palindrome number.")
