array = [1, 2, 3]
array2 = [4, 5]

for i in range(len(array2)):
  item = array2.pop(0)
  array.insert(i, item)

print(array)
print(array2)