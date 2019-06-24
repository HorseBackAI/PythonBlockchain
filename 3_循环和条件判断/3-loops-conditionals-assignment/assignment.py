# 1) Create a list of names and use a for loop to output the length of each name (len()).
# 2) Add an if check inside the loop to only output names longer than 5 characters.
# 3) Add another if check to see whether a name includes a “n” or “N” character.
# 4) Use a while loop to empty the list of names (via pop())

names = ['Max', 'Anna', 'Manuel', 'Chris', 'Stephen']

for name in names:
    print(len(name))
    if len(name) > 5:
        print(name)
    if 'n' in name or 'N' in name:
        print('The name includes \'n\' or \'N\'.')
    
while len(names) > 0:
    names.pop()
else:
    print('Length of name list: ', len(names))
    


