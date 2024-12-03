import re

tot = 0
def mul(a, b):
    return a * b

with open ("day-3/input.txt") as f:
    list = re.findall('mul\('r'[0-9]{1,3}'','r'[0-9]{1,3}''\)', f.read())
    print(list)
    for i in list:
        tot += eval(i)

print(tot)
