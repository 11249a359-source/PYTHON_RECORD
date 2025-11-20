Aim:To write a Python program that performs various list operations such 
   as slicing, inserting elements, sorting, reversing, removing specific
   elements, and finding the largest and smallest values in a list.

Algorithem:
step1: Start
step2: Create a list named my_list containing characters
      ['p','r','o','g','r','a','m','m','e'].

step3: Display slices of the list:
     a. Print elements from index 2 to 4
     b. Print elements from index 5 to end
     c. Print the entire list
step4: Create another list named list1 containing values
     [10, 15, 11, 65, 30].
step5: Insert an element:
     Insert the value 80 at index position 1 in list1.

step 5: Sort the list list1 in ascending order.

step 7: Reverse the list list1.
step8: Remove an element:
      Remove (pop) the element at index 3 and store it.
step9:  Display the removed element and the updated list.

step10: Find the largest element in the list using max().

step11: Find the smallest element in the list using min().

step12: Display all results.

step13: End




1.program:
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e']

print(my_list[2:5])
print(my_list[5:])
print(my_list[:])

list1 = [10, 15, 11, 65, 30]

list1.insert(1, 80)
print('INSERTED ELEMENT IN THE LIST:', list1)

list1.sort()
print('SORTED ELEMENT IN THE LIST:', list1)

list1.reverse()
print('REVERSED LIST IS:', list1)

removed_element = list1.pop(3)
print('REMOVED ELEMENT FROM THE LIST:', removed_element)
print('LIST AFTER REMOVAL:', list1)

print('LARGEST ELEMENT IN THE LIST:', max(list1))
print('SMALLEST ELEMENT IN THE LIST:', min(list1))

outut:
['o', 'g', 'r']
['a', 'm', 'm', 'e']
['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e']
INSERTED ELEMENT IN THE LIST: [10, 80, 15, 11, 65, 30]
SORTED ELEMENT IN THE LIST: [10, 11, 15, 30, 65, 80]
REVERSED LIST IS: [80, 65, 30, 15, 11, 10]
REMOVED ELEMENT FROM THE LIST: 15
LIST AFTER REMOVAL: [80, 65, 30, 11, 10]
LARGEST ELEMENT IN THE LIST: 80
SMALLEST ELEMENT IN THE LIST: 10


2.List Program : 

prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(price):
   		  return price * (1 + TAX_RATE)


final_prices = map(get_price_with_tax, prices)
print( final_prices)
Output : 
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

3.program:

l = [13, 4, 5, 3, 4]
l1 = []  # Frequency list
l2 = []  # Unique elements list
print("Element \tFrequency")
for i in l:
    if i not in l2:
        freq = l.count(i)  # Count occurrences of element i
        l1.append(freq)
        l2.append(i)

# Display element and its frequency
for i in range(len(l1)):
    print(l2[i], "\t\t", l1[i])
output:
Element    Frequency
13         1
4          2
5          1
3          1

4.program
Demonstrate on create and print Dictionaries 

country_capitals = 
{ 
"United States": "Washington D.C.", "England": "London", "Germany": Berlin", "Canada": "Ottawa "  } 
print(len(country_capitals)) 
print(country_capitals) 
country_capitals["Italy"] = "Rome" 
print(country_capitals) 
del country_capitals["Germany"] 
print(country_capitals) 
country_capitals.clear() 
print(country_capitals)

Output: 
Length of Dictonary: 4 
{'United States': 'Washington D.C.', 'England': 'London', 'Germany': 'Berlin', 'Canada': 'Ottawa '} 
{'United States': 'Washington D.C.', 'England': 'London', 'Germany': 'Berlin', 'Canada': 'Ottawa ', 'Italy': 'Rome'} 
{'United States': 'Washington D.C.', 'England': 'London', 'Canada': 'Ottawa ', 'Italy': 'Rome'} 
{} 


6.program:

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
Output : 


['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd',
 'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b',
 'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']



