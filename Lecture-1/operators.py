# Operators=> An operator is a symbol that performs a certain operation between operands

"""
*Types of Operators//
1.Arithmetic operators(+,-,*,/,%,**)
2.Realtional/comparison operators(==,!=,>,<,>=,<=)
3.Assignment operators(=,+=,-=,*=,/=,%=,**=)
4.Logical operators(not,and,or)

"""
# Arithmetic operators
a=5
b=2
sum=a+b
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)   #remainder
print(a**b)  #powera^b

# Relational operators
a=50
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Assignment operators
num=10
num+=20
# num-=5
# num*=10
# num/=2
# num%=2
# num**=7
print(num)

# Logical operators
print(not False)    
print(not True)
a=50
b=30
print(not(a>b))  #not operator

val1=True    
val2=False
print(val1 and val2)  #and operator
print(val1 or val2)   #or operator

"""
Type conversion=> there are two types)
1.Typecoversion->compiler automatically compiles.
2.Typecasting-> manually tells to compiler

"""
# type conversion..//

a=2
b=4.25
sum=a+b  #2.0+4.25 =6.25
print(sum)

# a="3"
# b=4.25
# print(type(a))
# print(a+b) # false we cant cancodinate float values with strings

"""
# Input in python..->

*input()statements is used to accept values (using keyboard) from user
1) input()       //result for input() is always a str
2) int(input())    //int
3) float(input())   //float

"""

# name=input("enter your name")
# print("your name is:" ,name)
# age=input("enter your age")
# print("your age is:",age)

val=input("Enter any value")
print(type(val),val)    #"24","99.23"
val=int(input("Enter any value"))
print(type(val),val)    #"24","99.23"

name=input("enter your name:")
age= int(input("enter your age:"))
marks=float(input("enter your marks"))

print("your name is:",name)
print("your age is :",age)
print("your marks is:",marks)

























