file = open('file1.txt', 'r')
print(file.read())
file.close()
elif selection_input == 3:
file = open('file1.txt', 'a')
subject_name = str(input("Enter school subject name to add into file :"))
file.write(subject_name + '\n')
file.close()
count = count + 1
 