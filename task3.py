attributes = ('str', 1, 3, 111, -200,
              '124134','dssd', True, False,
              1231.23423, 11.43, [1,13,'str'])


res ={}

for attr in attributes:
    res.setdefault(type(attr),[]).append(attr)

print(res)