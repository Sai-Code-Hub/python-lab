# Lists can be thought of the most general version of a sequence in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
# In this section we will learn about:
# 1.) Creating lists
# 2.) Indexing and Slicing Lists
# 3.) Basic List Methods
# 4.) Nesting Lists
# 5.) Introduction to List Comprehensions
import time

# 1. Creating Lists
my_list = [1, 2, 3]
print("my_list:", my_list)
print(len(my_list))
print(my_list[:-2])


my_list = ['A string', 23, 100.232, 'o']
print("my_list with mixed types:", my_list)
print("Length of my_list:", len(my_list))

# 2. Indexing and Slicing
my_list = ['one', 'two', 'three', 4, 5]
print("Element at index 0:", my_list[0])
print("From index 1 onward:", my_list[1:])
print("Up to index 3 (exclusive):", my_list[:3])

#2.1 Indexing & Slicing
my_list1 = ['one', 'two', 'three']
print("Element at index 0:", my_list1[0])
another_list = ['four', 'five', 'six']
print(my_list1 + another_list)
new_list=my_list1+another_list
print("new_list:", new_list)
new_list[0]='ONE ALL CAP'
print("new_list:", new_list)
new_list.append('append-seven')
print("new_list:", new_list)
removed_item=new_list.pop()
timestamp=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(f"'pop item:::{removed_item}' was removed at {timestamp}")
#print("removed_items:::", removed_item)

# Concatenation
print("Concatenated list:", my_list + ['new item'])
print("Original list (unchanged):", my_list)

# Reassignment to make change permanent
my_list = my_list + ['add new item permanently']
print("After reassignment:", my_list)

# Duplication
print("Duplicated list:", my_list * 2)
print("Original list (still unchanged):", my_list)

# 3. Basic List Methods
list1 = [1, 2, 3]
list1.append('append me!')
print("After append:", list1)

print("Pop index 0:", list1.pop(0))
print("After popping index 0:", list1)

popped_item = list1.pop()
print("Popped last item:", popped_item)
print("Remaining list:", list1)

# IndexError example (commented to avoid crash)
# print(list1[100])  # Would raise IndexError

# Sorting and Reversing
new_list = ['a', 'e', 'x', 'b', 'c']
print("Original new_list:", new_list)
new_list.sort()
print("Sorted list:", new_list)
my_sorted_list = new_list.sort() #sorting
print("Original new_list:", my_sorted_list)

new_list.sort()
my_sorted_list = new_list
print("Sorted new_list:", my_sorted_list)

new_list.reverse()
print("Reversed list:", new_list)

#numlist-->>
num_list = [4,2,3,1,6,5]
num_list.sort()
print("Original num_list:", num_list)


num_list.reverse()
print("Reversed list:", num_list)

# new_list.sort()
# print("Sorted list:", new_list)

# 4. Nesting Lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]
print("Matrix:", matrix)

print("First row of matrix:", matrix[0])
print("second row of matrix:", matrix[1])
print("First element of first row:", matrix[0][0])

# 5. List Comprehensions
first_col = [row[0] for row in matrix]
print("First column via list comprehension:", first_col)

#append, pop, sort, reverse