a = input('Введите название 1 текстого документа: ')
b = input('Введите содержимое текстого документа: ')

a1 = input('Введите название 2 текстого документа: ')
b1 = input('Введите содержимое текстого документа: ')

a2 = input('Введите название 3 текстого документа: ')
b2 = input('Введите содержимое текстого документа: ')

x1=len(b)
x2=len(b1)
x3=len(b2)
t = b # Содержимое 1 файла
r = b1 # Содержимое 2 файла
x = b2 #  Содержимое 3 файла

if (x1>x2 and x1>x3 and x2>x3):
    with open(a+'.txt','wt') as f4:
        f4.write(x)
    with open(a1+'.txt','wt') as f4:
        f4.write(r)
    with open(a2+'.txt','wt') as f4:
        f4.write(r)
if (x2>x1 and x2>x3 and x1>x3):
    with open(a + '.txt', 'wt') as f4:
        f4.write(t)
    with open(a1 + '.txt', 'wt') as f4:
        f4.write(x)
    with open(a2 + '.txt', 'wt') as f4:
        f4.write(x)
if (x3>x1 and x3>x2 and x1>x2):
    with open(a+'.txt','wt') as f4:
        f4.write(t)
    with open(a1+'.txt','wt') as f4:
        f4.write(r)
    with open(a2+'.txt','wt') as f4:
        f4.write(r)
if (x1>x2 and x1>x3 and x3>x2):
    with open(a + '.txt', 'wt') as f4:
        f4.write(r)
    with open(a1 + '.txt', 'wt') as f4:
        f4.write(r)
    with open(a2 + '.txt', 'wt') as f4:
        f4.write(x)
if (x2>x1 and x2>x3 and x3>x1):
    with open(a + '.txt', 'wt') as f4:
        f4.write(t)
    with open(a1 + '.txt', 'wt') as f4:
        f4.write(t)
    with open(a2 + '.txt', 'wt') as f4:
        f4.write(x)
if (x3>x1 and x3>x2 and x2>x1):
    with open(a + '.txt', 'wt') as f4:
        f4.write(t)
    with open(a1 + '.txt', 'wt') as f4:
        f4.write(r)
    with open(a2 + '.txt', 'wt') as f4:
        f4.write(t)