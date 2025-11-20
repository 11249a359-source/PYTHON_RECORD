Aim:To write a Python program that reads a text file, displays a specified number of lines, and counts the
   occurrences of a given word in the file.
ALGORITHM: Display Lines and Count Word Occurrences in a File

1.Start
2.Input the filename from the user.
3.Check if the file exists using os.path.isfile().
  If the file does not exist, display an error message and exit.
4.Open the file in read mode.
5.Read all lines of the file into a list called lineList.
6.Input the number of lines (lineCount) the user wants to display.
7.Display the first lineCount lines from lineList with line numbers.
8.Input a word from the user whose occurrences need to be counted.
9.Initialize a counter variable cnt to 0.
10.Loop through each line in lineList and count occurrences of the word using line.count(word), adding to cnt.
11.Display the total count of the word in the file.
12.End

progrm:
import os.path
import sys
fname = input("Enter the filename : ")
if not os.path.isfile(fname):
print("File", fname, "doesn't exists")
sys.exit(0)
infile = open(fname, 'r')
lineList = infile.readlines()
lineCount = int(input("Enter the number of lines you want to display : "))
for i in range(lineCount):
print(i+1, ":", lineList[i], end="")
word = input("Enter a word : ")
cnt = 0
for line in lineList:
cnt += line.count(word)
print("The word", word, "appears", cnt, "times in the file")

output:
Enter the filename :gg
Enter the number of lines you want to display :2
hello
world
Enter a word :l
The word L appears 3 times in the file
