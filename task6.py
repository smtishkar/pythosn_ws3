my_str = 'Заходим в свой канал и проверяем сообщение'
my_list = sorted(my_str.split())
max_len = len(max(my_list, key=len))

for i, elem in enumerate(my_list,start=1):
    print(f"{i} {elem:>{max_len}}")