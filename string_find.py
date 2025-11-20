str1 = "python is a programming language"
str2 = str1.find("is")
str3 = str1.find("java")
str4 = str1.find("n",5)
str5 = str1.find("i",5,25)
print(str2,str3,str4,str5)

sentence = (
     "The rocket, who was named Ted, came back "
     "from Mars because he missed his friends."  )
def is_consonant(letter):
     vowels = "aeiou"
     return letter.isalpha() and letter.lower() not in vowels


print( [char for char in sentence if is_consonant(char)])

