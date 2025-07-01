myset={}
myset = {1, 2, 3, 4, 5,1}
print(myset)
myset2=set("hello")
print(myset2)
myset3=set([1, 2, 3, 4, 5])
print(myset3)
myset4={}
print(type(myset4))  # this is a dictionary, not a set
myset5=set()
print(type(myset5))  # this is a set
myset.add(6)
# remove if not present raises KeyError
myset.remove(1) 
# removes if present, does nothing if not present
myset.discard(2)
print(myset)
print(myset.pop())
print(myset)

for x in myset:
    print(x, end=" ")

if 5 in myset:
    print("\nyes")

# union and intersection
odds={i for i in range(1, 10, 2)}
even={i for i in range(0, 10, 2)}
primes={2,3,5,7}
u=odds.union(even)
print(u)
i=odds.intersection(even)
print(i)
i=odds.intersection(primes)
print(i)
i=even.intersection(primes)
print(i)

setA={1,2,3,4,5}
setB={4,5,6,7,8}
diff=setA.difference(setB)
print(diff)
diff=setB.difference(setA)
print(diff)
diff=setA.symmetric_difference(setB)
print(diff)
setA.update(setB)
print(setA)
setA.intersection_update(setB)
print(setA)
setA.difference_update(setB)
print(setA)
setA.symmetric_difference_update(setB)
print(setA)
print(setB)
print(setA.issubset(setB))
setA={1,2,3,4,5}
setB={4,5}
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))
setC={7,8}
print(setA.isdisjoint(setC))

# you only copy the reference
setA={1,2,3,4,5}
setB=setA
setB.add(6)
print(setA)

setC=setA.copy()
setC=set(setA)  # another way to copy

# frozenset is immutable
frozen_set=frozenset([1, 2, 3, 4, 5])
print(frozen_set)
# a.add(6)  # this will raise an AttributeError
# a.remove(1)  # this will raise an AttributeError