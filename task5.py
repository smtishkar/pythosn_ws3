my_list = [1, 2, 3, 2, 1, 5, 7, 3, 2]
new_list =[]

for i, elem in enumerate(my_list, start=1):
    if elem % 2 != 0:
        new_list.append(i)

print(new_list)