import random;

#读取文件
fileName = 'data/171160.txt'
test = open(fileName, encoding='utf-8').read()

cnt = range(len(test))
resultList = random.sample(cnt, 5); 
print(resultList)

for i in resultList:
    print(test[i-1] + test[i] + test[i+1])

# 执火, 进兵, 十四