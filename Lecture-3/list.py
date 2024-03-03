                     # Lists in python

"""
A built-in data type that stores set of values  
It can store elements of different types(integer,float,string,etc.)

marks = [87,64,33,95,76]    #marks[0],marks[1]..
student = ["karan",85,"Delhi"]  #student[0],student[1]..
student[0] = "Arjun"  #followed in python
len(student)   #returns length 

"""

marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1

marks = [94.4,87.5,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["Karan",95.4,17,"Delhi"]
print(student[0])
student[0] = "arjun"
print(student)     # list are mutable in python we can change the value

# str = "hello"    # strings are immutable we cant change
# print(str[0])
# str[0] = "Y"

                 # List Slicing #

"""
similar to string slicing..

list_name[starting_idx:ending_idx] #ending idx is not included 
marks = [87,64,33,95,76]
marks[1:4]is[64,33,95]
marks[:4]is same as marks[0:4]
marks[1:]is same as marks[1:len(marks)]
marks[-3:-1]is[33,95]

"""
marks = [85,94,76,63,48]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

         # List Methods  #

"""
list = [2,1,3]
list.append(4)  #adds one element at the end  [2,1,3,4]
list.sort()    #sorts in ascending order  [1,2,3]
list.sort(reverse=True)  #sorts in descending order [3,2,1]
list.reverse()   #reverse list  [3,1,2]
list.insert(idx,el)   #insert element at index
list.remove(1)   #removes first occurrence of element
list.pop(idx)   #removes element at idx

Search python documentation...

"""
list = [2,1,3]
list.append(4)
print(list)
print(list.sort())

# print(list)
# print(list.append(4))

print(list.sort(reverse=True))
print(list) # descending order

list =  ["banana","litchi","apple"]
print(list.sort(reverse=True))
print(list)

list = ['a','d','e','f','c','b']
list.reverse()
print(list)

list = [2,1,3]
list.insert(1,5)
print(list)

list = [2,1,3,1]
list.pop(2)
print(list)






