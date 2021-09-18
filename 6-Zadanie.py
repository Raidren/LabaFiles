#Создать файл, являющийся результатом конкатенации (слияния) других файлов.
with open('test.txt','r') as f:
    f1 = f.read()
with open('test1.txt','r') as a:
    f2 = a.read()
c = [f1,f2]
with open('testsli9nie.txt','w') as d:
    for i in c:
        d.write(i)