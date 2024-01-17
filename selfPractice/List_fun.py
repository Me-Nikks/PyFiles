# append
# adds at last
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  

# extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  

# insert()
# (index,valu)
my_list = [1, 2, 3]
my_list.insert(2, 5)
print(my_list) 

# remove()
#removes the value
my_list1 = [1, 2, 3, 2, 4]
my_list1.remove(4)
print(my_list1)  

# pop()
# Removes and returns the element at a specified index (default is the last element).
my_list2 = [1, 2, 3, 4]
popped_element = my_list2.pop(2)
print(popped_element)  
print(my_list2)  

# sort()
# Sorts the list in ascending order

my_list3 = [3, 1, 4, 2]
my_list3.sort()
print(my_list3)  

# reverse()
# Reverses the elements of the list in place.

my_list4 = [1, 2, 3, 4]
my_list4.reverse()
print(my_list4)  

# copy()
# Returns a shallow copy of the list.

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(copied_list)  



number_list = [1,2,3,4,5,6,7,8,9]
print(number_list[1:4:2])




