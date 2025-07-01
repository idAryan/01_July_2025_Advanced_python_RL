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