#Определить, какой символ чаще других встречается в данном файле.
from collections import Counter
f = open('test.txt','r')
f1 = f.read()
print(f1)
cnt = Counter(f1.replace(' ', ''))

print('Часто встречаемый символ в файле это: ',cnt.most_common()[0][0])
