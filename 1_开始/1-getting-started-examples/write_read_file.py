name = input('请输入名字：')

f = open('name.txt', 'a')
f.write(name)
f.close()

f = open('name.txt', 'r')
print(f.read())