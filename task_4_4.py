a = [1, 2, 3, 4, 5]
for i in range(1):
    a.append(a.pop(0))
print(a)

# a = [1, 2, 3, 4, 5]
# n = 1
# result = []
# while (n<len(a)):
#     result.append(a[n])
#     n+=1
# result.append(a[0])
# print(result)
