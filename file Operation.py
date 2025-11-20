AIM:
To write a python program to accept a file name from the user and perform the following
operations 1. Display the first N line of the file 2. Find the frequency of occurrence of the word
accepted from the user in the file.

ALGORITHM:
1. Start
2. Accept the filename from the user.
3. Open the file in read mode.
4. Ask the user to input number of lines (N) to display.
5. Read and display the first N lines.
6. Ask the user to enter a word to search.
7. Read the entire file again.
8. Convert content and word to lowercase.
9. Use .count() to find the number of occurrences of the word.
10. Display the frequency.
11. Close the file.
12. End

PROGRAM:
def main():
# Step 1: Input file name
filename = input(&quot;Enter the filename: &quot;)

# Step 2: Open file and display first N lines
file = open(filename, &#39;r&#39;)
N = int(input(&quot;Enter number of lines to display: &quot;))
print(f&quot;\nFirst {N} lines of the file:&quot;)

for i in range(N):
line = file.readline()

39 | P a g e

if line == &#39;&#39;:
print(&quot;End of file reached.&quot;)
break
print(line.strip())
file.close()

# Step 3: Count word frequency
word = input(&quot;\nEnter the word to find its frequency: &quot;).lower()
file = open(filename, &#39;r&#39;)
content = file.read().lower()
frequency = content.count(word)
file.close()

print(f&quot;\nThe word &#39;{word}&#39; occurred {frequency} times in the file.&quot;)

# Run the function
main()

OUTPUT:

Enter the filename: demo.txt
Enter number of lines to display: 2
Enter the word to find its frequency: data

First 2 lines of the file:
Data is essential in today’s world.
Big data is changing the industry.

The word &#39;data&#39; occurred 2 times in the file.
