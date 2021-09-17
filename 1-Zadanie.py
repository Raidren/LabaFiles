#Распечатать все строки данного файла, содержащие заданную строку в качестве подстроки.
#Содержимое test.txt :
# word words worm warm
# wordsen words word warm
# wirds words worm warm
# wordem words worm warm
f = open('test.txt',"r")
f1 = f.readlines()
word = 'word'

s = f1[0].split().count(word)
s1 = f1[1].split().count(word)
s2 = f1[2].split().count(word)
s3 = f1[3].split().count(word)

if s == 1:
    print(f1[0])
if s1 == 1:
    print(f1[1])
if s2 == 1:
    print(f1[2])
if s3 == 1:
    print(f1[3])

