# collection provide special data types that allow you to store and manipulate multiple values in a single variable.
from collections import Counter
from collections import namedtuple, OrderedDict, defaultdict, deque
a="aaaaaabbbbccc"
my_counter=Counter(a)
print(my_counter)  # prints the count of each character in the string
print(my_counter.most_common(2))
print(list(my_counter.elements()))  # returns an iterator over elements repeating each as many times as its count
Point=namedtuple('Point', 'x,y')

pt=Point(10,20)
print(pt)  # prints Point(x=10, y=20)
print(pt.x, pt.y)  # prints 10 20

ordered_dict=OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)  # prints OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

d=defaultdict(list)
d=defaultdict(int)
d['a']=1
d['b']=2
print(d)
print(d['a'])
print(d['c'])

d=deque()
d.append(1)
d.append(2)
d.appendleft(0)
print(d)
d.pop()
d.popleft()
print(d)
d.clear()
d.extend([1,2,3])
d.extendleft([4,5,6])
print(d)  # prints deque([6, 5, 4, 1, 2, 3])
d.rotate(1)
print(d)  # rotates the deque by 2 steps to the right
d.rotate(-1)
print(d)