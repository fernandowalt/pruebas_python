mi_set = set({1, 2, 3, 4, 5})
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3, 4}
print(type(otro_set))
print(len(mi_set))
print(otro_set)

s1 = {1, 2, 3, }
s2 = {4, 5, 6}

s3 = s1.union(s2)

s3.add(10)
s3.remove(1)
s3.discard(1)
s3.pop()
s3.clear()

print(s3)
