list = [1, 2, 3, 4, 3, 5]
list.extend([6, 8, 9])
print(list)
list.insert(1, 1.2)
print(list)
list.remove(3)
print(list)
list.sort()
sorted_list = sorted(list)

lst = [1, 2, 3]

a = lst.append(4)
b = lst + [5]
print(a, b, lst)