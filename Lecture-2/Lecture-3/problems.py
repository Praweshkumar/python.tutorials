# Ques1) WAP to ask the user to enter names of their 3 favourite movies & store them in a list.

movies = []
movies.append(input("enetr the 1st movie:"))
# mov1 = input("enter the 1st movie: ")
movies.append(input("enetr the 2nd movie:"))
# mov2 = input("enter the 2nd movie: ")
movies.append(input("enetr the 3rd movie:"))
# mov3 = input("enter the 3rd movie: ")  

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

print(movies)


# Que2) WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
# eg "maam","racecar" we can read from starting and last that is same.

list1 = [1,2,3]
list2 = [1,2,3]

copy_list1 =list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
   print("palindrome")
else:
    print("not a palindrome")


# Que3) WAP to count the number of students with the "A"grade in the following tuple.
 # ["C","D","A","A","B","B","A"]

grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))


# Que4) Store the above values in a list & sort them from "Ascending" to "Descending".

grade =["C","D","A","A","B","B","A"]
grade.sort()
print(grade)








