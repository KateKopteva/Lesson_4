a, b = 1, 1
l = list()
for i in range(15):
    l.append(a)
    a, b = b, a+b
print(l)

#a = 1
#b = 1
#n = 15
#i = 0
#l = [1, 1]
#while i < n-2:
#    a, b = b, a+b
#    i += 1
#    l.append(b)
#print(l)