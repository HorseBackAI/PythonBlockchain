#1 Create two variables – one with your name and one with your age
name = input("请输入你的名字：")
age = input("你的年龄：")

#2 Create a function which prints your data as one string
def print_your_data():
    print("你的名字是 " + name + ", 你的年龄是 " + str(age))

#3 Create a function which prints ANY data (two arguments) as one string
def print_any_data(data1, data2):
    print("你的名字是 " + str(data1) + ", 你的年龄是 " + str(data2))

#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def decades(age):
    return int(age) // 10

print_your_data()
print_any_data(name, age)
print(decades(age))
