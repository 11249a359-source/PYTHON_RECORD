def main():
    obj1 = open("filenum.txt","w")
    for i in range(1,21):
         i =str(i)
         obj1.write(i)
         obj1.write(" ")
         obj1.close()
main()
