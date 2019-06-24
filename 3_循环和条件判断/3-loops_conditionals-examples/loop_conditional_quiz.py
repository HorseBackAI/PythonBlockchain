# 求：1 到 100 的和
# for 循环 和 while 循环各实现一个

n = 100

# for loop
sum = 0
for i in range(1, n+1):
    # sum = sum + i
    sum += i
print('for loop result:', sum)

# while loop
sum = 0
i = 1
while i <= n:
    sum += i # sum = sum + i
    i += 1
print('\nwhile loop result:', sum) 
# '\' escape next letter 跳过下一个字符，即下一个字符不作为字符串
# 而有新意义 '\n' new line 换行


# 求：1 到 100 偶数的和
# for 循环 和 while 循环各实现一个

print('\n偶数一共有：' + str(len(range(2, n+1, 2))) + '个')
# range(): 指定一个值的范围，给出这个范围内的值的列表，这个列表可循环
# len(): 给出列表的长度

# for loop
sum = 0
for i in range(2, n+1, 2):
    sum += i
print('\nfor loop 偶数 result:', sum)

# while loop
sum, i = 0, 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print('\nwhile loop 偶数 result:', sum)
