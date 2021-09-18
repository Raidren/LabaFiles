#В данном файле символы каждой строки упорядочить по алфавиту.
with open('test3.txt','r') as f:
    f=f.read()
print(f)
m = ''.join(sorted(f))
print(m)

