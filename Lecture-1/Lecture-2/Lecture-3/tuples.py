                                          # Tuples in Python
"""
A built-in data types that lets us create immutable sequences of values.

tup = [87,64,33,95,76]   #tup[0],tup[1]...
tup[0] = 43  # NOT allowed in Python

tup1 = ()
tup2 = (1)
tup3 = (1,2,3)

  Note: Tuples are immutable just like strings.

"""
tup = (2,1,3,11)
print(tup)
print(tup[0],tup[1])
# tup[0] = 5  # we can not change any value at index in tuples.

tup = ()
print(tup)
print(type(tup))

tup = ("hello",)   # we use , within parenthesis acts as a tuples
print(tup)
print(type(tup))

tup = [1,2,3,4]
print(tup[1:3])

                            #  Tuple Methods #
"""
tup = [2,1,3,1]
tup.index(el)     #returns index of first occurrence  tup.index(1) is 1
tup.count(el)     #counts total occurrences      tup.count(1) is 2


"""

tup = [1,2,3,4,2]
print(tup.index(2))
print(tup.count(2))