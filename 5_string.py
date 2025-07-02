# string ordered, immutable, iterable
my_string = "I'm Hello, World!"
my_string = 'I\'m a Python programmer'
my_string = """I'm a Python programmer
I love coding in Python!"""
my_string = """I'm a Python programmer \
hello world!"""
print(my_string)

my_string = "Hello, World!"
char=my_string[0]
print(char)
# my_string[0]='h'  # TypeError: 'str' object does not support item assignment
substring=my_string[0:5]
print(substring)
print(my_string[:5])  # prints from index 7 to the end
print(my_string[7:])  # prints from index 7 to the end

my_string="Hello World"
substring=my_string[::-1]
print(substring)
name="Tom"
greet="Hello"
sentence=greet+" "+name
print(sentence)
for i in sentence:
    print(i,end="")
if "e" in greet:
    print("\nyes")
my_string = "  Hello, World!  "
print(my_string)
my_string = my_string.strip()  # removes leading and trailing whitespace
print(my_string)
print(my_string.lower())  # converts to lowercase
print(my_string.upper())  # converts to uppercase
print(my_string.startswith("Hello"))  # checks if string starts with "Hello"
print(my_string.endswith("World!"))  # checks if string ends with "World!"
print(my_string.replace("World", "Universe"))  # replaces "World" with "Python"
print(my_string)
print(my_string.find('o'))
print(my_string.find('lo'))
print(my_string.count('o'))  # counts occurrences of 'o'

my_string="how are you ?"
# by default, split() splits by whitespace
my_list=my_string.split() 
print(my_list)  # splits the string into a list of words
my_list = my_string.split('o')  # splits by 'o'
print(my_list)  # splits the string into a list of words
new_string='o'.join(my_list)  # joins the list back into a string with 'o' as separator
print(new_string)  # prints the joined string
new_string=''.join(my_string)  # joins the list back into a string with ' ' as separator
print(new_string)  # prints the joined string

from timeit import default_timer as timer
mylist=['a']*100000
start=timer()
my_string=''
for i in mylist:
    my_string += i  # concatenates each element to the string  # prints the concatenated string
stop=timer()
print(f"Time taken: {stop-start} seconds")
start=timer()
my_string=''.join(mylist)
stop=timer()
print(f"Time taken: {stop-start} seconds")

# String formatting
name = "Alice"
my_string=" the name is %s" %name
print(my_string)  # prints the formatted string
age=23
gpa=7.6
my_string=" the name is %s and age is %d with gpa %.2f" %(name,age,gpa)
print(my_string)  # prints the formatted string
my_string=" the name is {} and age is {} with gpa {:.2f}".format(name,age,gpa)
print(my_string)  # prints the formatted string
print(f" the name is {name} and age is {age*2} with gpa {gpa:.2f}")  # f-string formatting efficient