s1 = {5,7,8,9,4}
s2 = {1,2,3,4,5}
print(s1.union(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s1.pop()
s1.add(10)
s1.remove(5)
print(s1)
print(s2)