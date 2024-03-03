#  Strings ==> string is data type that stores a sequence of characters.

"""
Basic operations
1) Concatenation ==> "hello"+"world" --->"helloworld"
2) length of str ==>  len(str)
*Escape sequence character \n,\t etc.
"""

# str1 = "This is a string.\t We are creating it in python"
# print(str1)
# str2 = 'Apna college'
# str3 = """This is a string"""

"this is a apnacollege's tutorial"


str1 ="apna"  
print(len(str1))          #length of string
str2  ="college"
len2 = len(str2)
print(len2)
final_str=str1+" "+str2        #concatenation
print(final_str)
print(len(final_str))

                            # ....Indexing....#

"""
  APNA COLLEGE               | str = "Apna_college"
  01234567891011             | str[0] is 'A', str[1] is 'p'...
                             | str[0] = 'B' #not allowed

"""
str = "apna college"
print(str[2])
ch = str[2]
print(ch)
  
                        #...Slicing...#
"""
Accessing parts of a string
str[starting_idx:ending_idx]  #ending idx is not included
str = "ApnaCollege"
str[1:4]is "pna"
str[ :4]is same as str[0:4]
str[1:]is same as str[1:len(str)]

                # Negative index #
    A  P P L E                        |  str = "Apple"
   -5 -4-3-2-1                        |  str[-3:-1] is "pl"
"""
str = "apna college"
print(str[0:4])
print(str[1:5])
print(str[5:len(str)])
print(str[5:]) #[5:len(str)]
print(str[:4])

str = "apple"
print(str[-3:-1])
print(str[-5:-2])

                    #  String function  #

"""
1. str = "I am a coder."
2. str.endswith("er.")   #returns true if string ends with substr
3. str.capitalize()      #capitalizes 1st char
4. str.replace(old,new)  #replaces all occurrences of old with new
5. str.find(word)        #returns 1st index of 1st Occurrence
6. str.count("am")       #counts the occurence of substr in string

"""
str = "i am studying python"
print(str.endswith("app"))
print(str.capitalize())
print(str.replace("python","javascript"))
print(str.find("o"))
print(str.count("i"))













































































