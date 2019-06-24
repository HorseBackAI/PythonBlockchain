data = [{'name': 'Michael', 'age': 24, 'hobby':['read_books', 'play_toys']}, 
        {'name': 'Alex', 'age': 24, 'hobby':['read_books', 'play_basketball']}, 
        {'name': 'pz', 'age': 250, 'hobby':['read_children_comics', 'play_babytoys']}
       ]

names = [p['name'] for p in data]
print(names)

are_older_than_20 = [p['age'] > 20 for p in data]
print(are_older_than_20)
print(all(are_older_than_20))

copied_data = 