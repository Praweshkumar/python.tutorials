    #  Conditional statements  # 
"""
if-elif-else(SYNTAX)

if(condition):
Statement1
elif(condition):
Statement2
else:
StatementN

"""
age = 21
if(age>=18):
    print("you can vote")

light = "green"
if(light=="red"):
    print("stop")
elif(light=="green"):
     print("go")
elif(light=="yellow"):
      print("look") 
else:
     print("Light is broken")          

print("end of code")


num = 5
if(num>2):
     print("true")
elif(num>3):
     print("greater than 3")    

age = 24
if(age>=18):
     print("you can drive a car") # Spaces which gives here before print its called indentation.
else:
     print("you can not drive")     

                      # Nesting #

age = 97

if(age>=18):
     if(age>=80):
          print("cannot dive")
     else:
          print("Can drive")
else:
     print("cannot dive")



