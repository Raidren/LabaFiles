#В файле подсчитать количество строк, которые начинаются и оканчиваются один и тем же символом.
string="GDFGDFLKHFGKHLBNVBLKLYHRTKHGKITLERKGLBVCLKLGDFLIY"
string_char=list(string)
string_length=len(string_char)

char_first="G"
char_second="G"

with open('test4.txt','w') as f:
    for i in range(0,string_length):
        for b in range(i,string_length):
            if(string_char[i]==char_first and string_char[b]==char_second):
                list=[]
                for z in range(i,b+1):
                    list.append(string_char[z])
                t = ''.join((list))
                f.write(str(list))
                print(t)

with open('test4.txt','r') as f1:
    f1 = f1.read()
    kolvo = f1.count('[')
    print('Количество строк, которые начинаются и оканчиваются один и тем же символом: ',kolvo)