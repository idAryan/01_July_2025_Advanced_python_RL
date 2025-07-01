mytuple=()
mytuple = (1, 2, "3", 4, 5)
print(mytuple)
# Tuple with parentheses
mytuple1=1,"boston",3.14
print(mytuple1)

mytuple=tuple(["max", "boston", 3.14])
print(mytuple)
item=mytuple[0]
print(item) 
item=mytuple[1:3]
print(item)
item=mytuple[-1]
print(item)
# We could not change the value in the tuple , typeError

for i in mytuple:
    print(i, end=" ")

# checking element in tuple
if "boston" in mytuple:
    print("\nyes")

mytuple2=('a', 'b', 'c', 'd','a')
print(len(mytuple2))
print(mytuple2.count('a'))
print(mytuple2.index('c'))
print(mytuple2.index('a'))
print(mytuple2.index('a', 1))  # start from index 1
my_list=list(mytuple2)
print(my_list)
mytuple2=tuple(mytuple2) 

# slicing tuple
a=tuple([i for i in range(10)])
print(a)
print(a[2:5])
print(a[::-1])
my_tuple4="Max",28,"boston"
name,age,city=my_tuple4
print(name)
my_tuple=tuple(i for i in range(10))
print(my_tuple)
i1,*i2,i3=my_tuple
print(i1)
print(i2)
print(i3)

import sys
import timeit
my_list=[0,1,2,"hello",True]
my_tuple=(0,1,2,"hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(mytuple),"bytes")
print(timeit.timeit(stmt="[0,1,2,'hello',True]",  number=1000000))
print(timeit.timeit(stmt="(0,1,2,'hello',True)", number=1000000))