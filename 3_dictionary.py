# key value pair, mutable, unordered, indexed
# as python version 3.7 dictionaries are ordered, but in earlier versions they were unordered
mydict={"name":"max", "age":28, "city":"boston"}
print(mydict)
mydict2=dict(name="Mary",age=27,city="New York")
print(mydict2)
value=mydict["name"]
print(value)
mydict["email"]="max@xyz.com"
print(mydict)
mydict["email"]="coolmax@xyz.com"
print(mydict)
mydict.pop("email")
print(mydict)
del mydict["age"]
print(mydict)
# this removes the last item in the dictionary
mydict.popitem()
print(mydict)

print(mydict2)
if 'name' in mydict2:
    print(mydict2["name"])
try:
    print(mydict2["nalme"])
except:
    print("key not found")

for key in mydict2:
    if key == "city":
        print(key)
        break
    print(key,end=",")

values=[]
for value in mydict2.values():
    values.append(value)

print(",".join(str(v) for v in values))

for key,value in mydict2.items():
    print(f"{key}={value}")

# this will not modify original dictionary
mydict_cpy=mydict2.copy()

mydict_cpy["name"]="John"   
print(mydict_cpy)
print(mydict2)

mydict_cpy=dict(mydict2)
mydict_cpy["name"]="John"   
print(mydict_cpy)
print(mydict2)
mydict["email"]="max@xyz.com"
print(mydict)
print(mydict2)
mydict.update(mydict2)
print(mydict)

mydict={2:9,6:36,9:81,4:16,5:25}
print(mydict)
value=mydict[2]
print(value)
# list is not possible as key, since list is mutable, not hashable as can be changed
mytuple=(8,7)
mdict={mytuple:49}
print(mdict)