with open('test7.txt','r') as f:
    print("Самая длинная строка в файле: ")
    print(max(f, key = len))