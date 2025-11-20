AIM:
To develop a python program to convert binary to decimal, octal to hexadecimal using
functions with algorithm steps and sample output.

ALGORITHM:
1. Start
2. Define a function is_binary(s) to check if all characters in string s are &#39;0&#39; or &#39;1&#39;
3. Define a function binary_to_decimal(binary_str)
a. If is_binary(binary_str) is True:
i. Convert to decimal using int(binary_str, 2)
ii. Display the decimal value
b. Else, print &quot;Invalid binary number&quot;
4. Define a function is_octal(s) to check if all characters in string s are digits from &#39;0&#39; to &#39;7&#39;
5. Define a function octal_to_hexadecimal(octal_str)
a. If is_octal(octal_str) is True:
i. Convert to decimal using int(octal_str, 8)
ii. Convert to hexadecimal using hex(decimal)[2:].upper()
iii. Display the hexadecimal value
b. Else, print &quot;Invalid octal number&quot;
6. Input binary number as string → binary_input
7. Call binary_to_decimal(binary_input)
8. Input octal number as string → octal_input
9. Call octal_to_hexadecimal(octal_input)
10. Stop

PROGRAM:
def is_binary(s):
    return all(char in '01' for char in s)

def binary_to_decimal(binary_str):
    if is_binary(binary_str):
        decimal = int(binary_str, 2)
        print(f"Binary to Decimal: {binary_str} → {decimal}")
    else:
        print("Invalid binary number. Please enter a number containing only 0s and 1s.")

def is_octal(s):
    return all(char in '01234567' for char in s)

def octal_to_hexadecimal(octal_str):
    if is_octal(octal_str):
        decimal = int(octal_str, 8)
        hexadecimal = hex(decimal)[2:].upper()
        print(f"Octal to Hexadecimal: {octal_str} → {hexadecimal}")
    else:
        print("Invalid octal number. Please enter a number containing digits 0 to 7 only.")

# Main program
binary_input = input("Enter a binary number: ")
binary_to_decimal(binary_input)

octal_input = input("Enter an octal number: ")
octal_to_hexadecimal(octal_input)

output:
Enter a binary number: 98
Invalid binary number. Please enter a number containing only 0s and 1s.
Enter an octal number:
