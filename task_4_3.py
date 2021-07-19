d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
for i in list(d.keys()):
    d[i + str(len(i))] = d.pop(i)
print(d)

# d = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# keys_d = list(d.keys())
# i = 0
# while i < len(keys_d):
#     new_k = keys_d[i] + str(len(keys_d[i]))
#     d[new_k] = d.pop(keys_d[i])
#     i+=1
# print(d)
