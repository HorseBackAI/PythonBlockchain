# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        # 若链是空的，则返回 None
        return None
    # 链不是空的，则返回链中最后一个区块
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('交易额: '))
    return user_input


def get_user_choice():
    user_input = input('你的选择是: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('输出区块')
        print(block)
        

while True:
    # 提示用户输入选择
    print('请选择')
    print('1: 添加新交易额')
    print('2: 输出区块链中的所有区块')
    print('q: 退出')
    # 获取用户选择
    user_choice = get_user_choice()
    # 根据用户选择，执行不同任务
    if user_choice == '1':
        # 1）获取 2）添加：新交易额
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        # 输出区块链中的所有区块
        print_blockchain_elements()
    elif user_choice == 'q':
        # 退出循环
        break
    else:
        print('输入不正确，请从上面列表选择一个值！')
    print('选择被记录了！')

print('完成!')
