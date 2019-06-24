import json, pickle

waiting_for_input = True
input_list = []
while waiting_for_input:
        print('1: Add a value ')
        print('2: Read the value')
        print('q: quit')
        user_choice = input('Please entre your choice: ')
        if user_choice == '1':
                add_value = input('Please enter your value: ')
                input_list.append(add_value)
                with open('value.txt', mode='w') as f:
                        value = json.dumps(input_list)
                        print(value)
                        f.write(value)
        elif user_choice == '2':
                with open('value.txt', mode='r') as f:
                        value = json.loads(f.read())
                        print(value)
                        print('Type which I read: ', type(value))
        elif user_choice == 'q':
                waiting_for_input = False
print('Done!')

