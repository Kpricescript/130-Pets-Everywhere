#Square
my_list = [1, 4, 9]

print(list(map(lambda item: item**2, my_list)))

#List Sorting
a = [(10, -1), (0, 2), (5, 2), (9, 9)]
print(sorted(a, key=lambda item: item[1]))