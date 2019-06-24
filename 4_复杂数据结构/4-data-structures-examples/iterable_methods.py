simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)
del(simple_list[0])
print(simple_list)
print()

d = {'姓名': '张澎', '年龄': 44}
print(d.items())
for k, v in d.items():
    print(k, v)
del(d['姓名'])
print(d)
print()

t = (1, 2, 3)
print(t.index(2))
# del(t[0])
print()

s = {'张澎', 'LMC', '张澎'}
print(s)
# del(s['张澎'])

