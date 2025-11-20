AIM:
To write a python program to implement insertion sort and merge sort using lists.

ALGORITHM FOR INSERTION SORT
1. Start
2. Input the list of elements
3. Loop from index 1 to end of the list:
o Store the current value in a variable key
o Set j = i - 1
o While j &gt;= 0 and list[j] &gt; key:
 Move list[j] to position j + 1
 Decrease j by 1
o Place key at position j + 1
4. Display the sorted list
5. Stop
ALGORITHM FOR MERGE SORT
1. Start
2. If the list has more than 1 element:
o Find the middle index
o Split the list into left and right halves
o Recursively call merge sort on both halves
o Merge the two sorted halves into a single sorted list
3. Use a helper function merge() to combine two sorted lists
4. Display the sorted list
5. Stop

PROGRAM FOR INSERTION SORT:
def insertion_sort(arr):
for i in range(1, len(arr)):

29 | P a g e

key = arr[i]
j = i - 1

while j &gt;= 0 and arr[j] &gt; key:
arr[j + 1] = arr[j]
j -= 1

arr[j + 1] = key
# Sample input
arr = [34, 8, 64, 51, 32, 21]
print(&quot;Original list:&quot;, arr)
insertion_sort(arr)
print(&quot;Sorted list (Insertion Sort):&quot;, arr)

PROGRAM FOR MERGE SORT:

def merge_sort(arr):
if len(arr) &gt; 1:
mid = len(arr) // 2
left_half = arr[:mid]
right_half = arr[mid:]
merge_sort(left_half)
merge_sort(right_half)
i = j = k = 0
# Merge the sorted halves
while i &lt; len(left_half) and j &lt; len(right_half):
if left_half[i] &lt; right_half[j]:
arr[k] = left_half[i]
i += 1
else:
arr[k] = right_half[j]
j += 1
k += 1
# Check for remaining elements

29 | P a g e

while i &lt; len(left_half):
arr[k] = left_half[i]
i += 1
k += 1
while j &lt; len(right_half):
arr[k] = right_half[j]
j += 1
k += 1
# Sample input
arr = [34, 8, 64, 51, 32, 21]
print(&quot;Original list:&quot;, arr)
merge_sort(arr)
print(&quot;Sorted list (Merge Sort):&quot;, arr)

OUTPUT:

Original list: [34, 8, 64, 51, 32, 21]
Sorted list (Insertion Sort): [8, 21, 32, 34, 51, 64]

Original list: [34, 8, 64, 51, 32, 21]
Sorted list (Merge Sort): [8, 21, 32, 34, 51, 64]
