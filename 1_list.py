myList=["banana","cherry","apple","orange"]
print(myList)
mylist2=list()
print(mylist2)
mylist3=[5,True,False,"apple","apple",5,5]
print(mylist3)
print(mylist3[0])
print(mylist3[1:4])
print(mylist3[-1])
for i in mylist3:
    print(i,end=" ")
print(end="\n")
if "banana" in mylist3:
    print("yes")
else:
    print("no")
print(len(mylist3))

mylist3.append("lemon")
print(mylist3)
mylist3.insert(1,"blueberry")
print(mylist3)
mylist3.pop()
print(mylist3)
mylist3.remove("apple")
print(mylist3)
mylist2.clear()
print(mylist2)
mylist3.reverse()
print(mylist3)
mylist4=[i for i in range(4)]
print(mylist4)
# sort inplace
mylist4.sort(reverse=True)
print(mylist4)

# sort via newlist
newlist=sorted(mylist4)
print(newlist)

mylist6=[0]*5
print(mylist6)
mylist7=[i for i in range(5)]
mylist8=[i for i in range(5,10)]
new_list=mylist7+mylist8
print(new_list)

a=new_list[1:5]
print(a)
print(new_list[1:])
# all the way to list with 2nd item
a=new_list[::2]
print(a)
# reverse your list
a=new_list[::-1]
print(a)
# original list changed both list refer same object
lst_copy=new_list
lst_copy[0]=100
print(new_list)
# copying the list
lst_cpy=new_list.copy()
lst_cpy[0]=200  
print(new_list)
lst_cpy2=list(new_list)
lst_cpy2[0]=300 
print(new_list)
# copy using slicing
lst_cpy3=new_list[:]
lst_cpy3[0]=400
print(new_list)

# list comprehension
mylist9=[i*i for i in range(10)]
print(mylist9)
mylist10=[i*i for i in mylist9 if i%2==0]
print(mylist10)