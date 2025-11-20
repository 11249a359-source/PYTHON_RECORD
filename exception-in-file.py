try:
    file = open("example.txt", "r")
    # Code to read from the file
except FileNotFoundError:
    print("File not found!")
else:
    file = open("example.txt", "r")
    print(file.read())
finally:
    try:
        file.close()
    except:
        pass
