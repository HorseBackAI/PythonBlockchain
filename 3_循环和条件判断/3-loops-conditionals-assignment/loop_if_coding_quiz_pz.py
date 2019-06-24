# 输入
string = input('请输入一组数字，以逗号间隔：')
print(type(string))

# 把输入的字符串转换为数值的列表
# 1. 以逗号分割字符串，得到一个字符串的列表
string_list = string.split(',')
print(string_list)
# 2. 将这个字符串的列表转换成数值的列表
value_list = []
for e in string_list:
    value_list.append(int(e))
# 打印检查：是不是数值的列表
print(value_list)

# 逻辑判断
if 2 in value_list and 5 in value_list:
    print('hiiiihello')
elif 2 in value_list:
    print('hi')
elif 5 in value_list:
    print('hello')
else:
    print('neither 2 nor 5 in list')
    