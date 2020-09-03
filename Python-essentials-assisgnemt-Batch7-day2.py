#list and its functions

s=[1,2,3,4,5,6,7,8]
print(s.append(9)) #1
print(s)

print(s.insert(1,7)) #2
print(s)

print(s.remove(2))  #3
print(s)

print(s.pop(0))   #4
print(s)

print(s.clear())   #5
print(s)


print("\n")
#dictonary and its functions

a={0:0,1:1,2:2,3:3,4:4,5:5,6:6}
print(a.pop(1))  	#1
print(a)

print(a.update({7:7}))   #2
print(a)

print(a.keys())   	#3
print(a.values()) 	#4
print(a.popitem()) 	#5
print(a)


print("\n")
#Sets and its functions
d={1,2,3,4,5}
t={5,6,7,8,9}

print(d.union(t))		#1
print(d.intersection(t))	#2
print(d.difference(t))		#3
print(d.update(t))		#4
print(d)
print(t.pop())		#5
print(t)

print("\n")

#tuples and its functions
print("\n")

tuple=(1,2,3,4,6,6,6,8,9)
x=tuple.count(6)		#1
print(x)

x=tuple.index(8)		#2
print(x)


print("\n")

#string and its functions

print("\n")

string="wakarewaka"
w="hEllO"
u="hello123"
print(string.upper())		#1
print(string.lower())		#2
print(w.title())		#3
print(u.swapcase())		#4
print(string.count("a"))	#5