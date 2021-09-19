f1 = open('s-1.txt','r')
f2 = open('s-2.txt','r')
a = f1.read()
b = f2.read()
if a == b:
    print('В файлах одинаковая информация')

elif a != b:
    print('Разные')
    a1 = list(str(a))
    b1 = list(str(b))
    print(a1)
    print(b1)
for i,b in zip(a1,b1):
    if i != b:
        print()
        print('Первое встречающееся отличие в файле 1:',i,'Первое встречающееся отличие в файле 2:',b, sep='\n')
