#Определить, сколько строк, состоящих из одного, двух, трех и т.д. символов, содержится в данном файле.
f = open('test1.txt','r')
line = 0
for i in f:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(i,len(i),'симв.',word,'сл.')

print(line,'стр.')
f.close()