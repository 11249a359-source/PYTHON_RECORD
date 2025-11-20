AIM:
To write a Python program that accepts a sentence and find the number of words, digits,
uppercase letters and lowercase letters.

ALGORITHM:
1. Start
2. Input a sentence from the user and store it in a variable sentence
3. Initialize counters:
a. word_count = 0
b. digit_count = 0
c. uppercase_count = 0
d. lowercase_count = 0
4. Count words using:
a. word_count = len(sentence.split())
(splits the sentence by whitespace)
5. Iterate through each character ch in the sentence:
a. If ch.isdigit() → increment digit_count
b. If ch.isupper() → increment uppercase_count
c. If ch.islower() → increment lowercase_count
6. Display the values of:
a. word count
b. digit count
c. uppercase letter count
d. lowercase letter count
7. Stop

PROGRAM:

# Input
sentence = input("Enter a sentence: ")

# Initialize counters
word_count = len(sentence.split())
digit_count = 0
uppercase_count = 0
lowercase_count = 0

# Iterate over characters
for ch in sentence:
    if ch.isdigit():
        digit_count += 1
    elif ch.isupper():
        uppercase_count += 1
    elif ch.islower():
        lowercase_count += 1

# Output the results
print(f"\nWord Count: {word_count}")
print(f"Digit Count: {digit_count}")
print(f"Uppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")

output:
Enter a sentence: helloWorld

Word Count: 1
Digit Count: 0
Uppercase Letters: 1
Lowercase Letters: 9
