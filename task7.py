my_str = 'Заходим в свой канал и проверяем сообщение'
my_str = my_str.replace(' ','')

my_dict ={}

for element in my_str:
    if element not in my_dict.keys():
        my_dict[element] = 1
    else:
        my_dict[element] = my_dict[element]+1
print(my_dict)