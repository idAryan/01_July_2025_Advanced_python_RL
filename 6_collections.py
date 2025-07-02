# collection provide special data types that allow you to store and manipulate multiple values in a single variable.
from collections import Counter
a="aaaaaabbbbccc"
my_counter=Counter(a)
print(my_counter)  # prints the count of each character in the string
print(my_counter.most_common(2))
