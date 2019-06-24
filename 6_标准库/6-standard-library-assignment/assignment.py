import random
import datetime

# 1) Import the random function and generate both a random number
#  between 0 and 1 as well as a random number between 1 and 10.
rn1 = random.random()
rn2 = random.randint(1, 10)
print(rn1, rn2)
print()

# 2) Use the datetime library together with the random number 
# to generate a random, unique value.
now = datetime.datetime.now()
print(now)
rv = str(rn1) + str(now)
print(rv)
