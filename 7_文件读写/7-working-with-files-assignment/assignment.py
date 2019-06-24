# 1) Write a short Python script which queries the user for input
#  (infinite loop with exit possibility) and writes the input to a file.

# 2) Add another option to your user interface: The user should
#  be able to output the data stored in the file in the terminal.

# 3) Store user input in a list (instead of directly adding it to the file)
#  and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/json data.
import pickle, json

waiting_for_input = True
input_list = []
while waiting_for_input:
    print("--- 选项说明 ---\n1: 输入具体内容 \n2: 输出到终端 \n3: 操作数据 \nq: 退出")
    user_choice = input("请选择：")
    if user_choice == '1':
        user_input = input("请输入具体内容：")
        input_list.append(user_input)

        with open('用户输入内容.txt', mode='w') as f:
            data = json.dumps(input_list)
            print(data)
            f.write(data)

        # with open('用户输入内容.p', mode='wb') as f:
        #     data = pickle.dumps(input_list)
        #     f.write(data)

    elif user_choice == '2':
        with open('用户输入内容.txt', mode='r') as f:
            data = json.loads(f.read())
            print(data)
            print('读取的数据类型是：', type(data))

        # with open('用户输入内容.p', mode='rb') as f:
        #     data = pickle.loads(f.read())
        #     print(data)
        #     print('读取的数据类型是：', type(data))

    elif user_choice == '3':
        with open('用户输入内容.txt', mode='r') as f:
            data = json.loads(f.read())
            print('输出列表第一个元素：', data[0])

        # with open('用户输入内容.p', mode='rb') as f:
        #     data = pickle.loads(f.read())
        #     print('输出列表第一个元素：', data[0])

    elif user_choice == 'q':
        waiting_for_input = False
else:
    print("用户退出！")