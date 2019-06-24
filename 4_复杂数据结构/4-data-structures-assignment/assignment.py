# 1) Create a list of “person” dictionaries with a name, age and 
# list of hobbies for each person. Fill in any data you want.
persons =  [
    {'姓名': '张三',
     '年龄': 37,
     '兴趣': ['足球', '游泳']
    },
    {'姓名': '李四',
     '年龄': 44,
     '兴趣': ['自行车']
    },
    {'姓名': '王五',
     '年龄': 25,
     '兴趣': ['画画', '听音乐']
    }
]

# 2) Use a list comprehension to convert this list of persons into
# a list of names (of the persons).
person_names = [p['姓名'] for p in persons]
print(persons)
print(person_names)
print()

# 3) Use a list comprehension to check whether all persons are older than 20.
are_all_older_than_20 = all([p['年龄'] > 20 for p in persons])
print(are_all_older_than_20)
print()

# 4) Copy the person list such that you can safely edit 
# the name of the first person (without changing the original list).
# copied_persons = persons[:] this copy doesn't solve this problem.
copied_persons = [p.copy() for p in persons]
copied_persons[0]['姓名'] = '赵六'
print(copied_persons)
print(persons)
print()

# 5) Unpack the persons of the original list into different variables 
# and output these variables.
p1, p2, p3 = persons
print(p1)
print(p2)
print(p3)

