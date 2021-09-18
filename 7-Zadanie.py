#Дан файл и две строки. Все вхождения первой строки в файл (в том числе в качестве подстроки) заменить второй строкой.
with open('test3.txt','r') as a:
    a = a.read().split()
print(a)
a1 = a[0]
a2 = a[1]
m = ' '.join(a)
zamena = (m.replace(a1, a2))
print(zamena)

