AIM:
To develop a program to backing up a given Folder (Folder in a current working directory)
into a ZIP File by using relevant modules and suitable methods.

ALGORITHM:
1. Start
2. Import the required modules: os, zipfile
3. Get the folder name from the user (it should be a folder in the current working directory)
4. Create a valid ZIP file name using the folder name (e.g., foldername_backup.zip)
5. Create a new ZIP file using zipfile.ZipFile() in write mode
6. Use os.walk() to iterate over all files and subfolders inside the folder
7. For each file:
o Create a relative path for the file inside the ZIP
o Write the file to the ZIP using .write()
8. Close the ZIP file
9. Display a message that the folder has been successfully backed up
10. End

PROGRAM:
import os
import zipfile

def backup_folder_to_zip(folder_name):
# Step 1: Construct ZIP file name
zip_filename = folder_name + &#39;_backup.zip&#39;

# Step 2: Create the ZIP file
with zipfile.ZipFile(zip_filename, &#39;w&#39;) as backup_zip:
# Step 3: Walk through the folder
for folderpath, subfolders, filenames in os.walk(folder_name):
for filename in filenames:

39 | P a g e

file_path = os.path.join(folderpath, filename)
# Store the file with relative path
relative_path = os.path.relpath(file_path, folder_name)
backup_zip.write(file_path, arcname=os.path.join(folder_name, relative_path))

print(f&quot;Folder &#39;{folder_name}&#39; has been successfully backed up to &#39;{zip_filename}&#39;.&quot;)

# Main Program
folder = input(&quot;Enter the folder name to backup (must be in current directory): &quot;)
if os.path.isdir(folder):
backup_folder_to_zip(folder)
else:
print(&quot;The specified folder does not exist in the current directory.&quot;)

OUTPUT:

Enter the folder name to backup (must be in current directory): myproject
Folder &#39;myproject&#39; has been successfully backed up to &#39;myproject_backup.zip&#39;.
