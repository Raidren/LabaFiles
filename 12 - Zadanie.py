#Имеются два файла (размеры файлов могут не совпадать).
# Переписать элементы первого файла во второй, второго – в первый. Использовать вспомогательный файл.
with open('test5.txt','r') as f1:
    f1=f1.read()

with open('test6.txt','r') as f2:
    f2=f2.read()

a = f1
b = f2
with open('test56.txt','w') as f3:
    f3 = f3.write(a+','+b)
with open('test56.txt','r') as f4:
    f4 = f4.read().split(',')
c = []
for i in f4:
    c.append(i)

with open('test5.txt','w') as f5:
    f5=f5.write(c[1])
with open('test6.txt','w') as f6:
    f6=f6.write(c[0])