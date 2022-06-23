#Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#входные и выходные данные хранятся в отдельных текстовых файлах

with open('/Users/ekaterina/Desktop/Desktop/Python/lesson6/file1.txt', 'r') as data:
    data1 = data.read()

str1 = ' '
count = 0
temp = 0
for i in range(len(data1)+1):

    if i == len(data1):
        str1 = str1+str(temp)+data1[count]
    elif data1[i] == data1[count]:
        temp += 1
    else:
        str1 = str1+str(temp)+data1[count]
        count += temp
        i+=count
        temp = 1

print(str1)
with open('/Users/ekaterina/Desktop/Desktop/Python/lesson6/file1result.txt', 'w') as result:
    result.write(str1)