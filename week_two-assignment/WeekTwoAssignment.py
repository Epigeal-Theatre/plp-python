"""
submit a github repo link for the assignment below




Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.

"""
my_list =[]#create an empty list
my_list.append(10)#append the values one by one
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)
my_list.insert(1,15)#insert the value 15 in position 2
print(my_list)
my_list.extend([50, 60, 70])#extend the list by the values in another list [50, 60, 70]
print(my_list)
my_list.pop(-1)#remove the last element in the list
print(my_list)
my_list.sort()#sort list in ascending order
print(my_list)
indexOf30=my_list.index(30)#find index of the value 30
print(indexOf30)