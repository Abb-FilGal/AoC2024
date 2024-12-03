import re

with open("day-3/input.txt") as f:
    mem = f.read()


def fixmem(s):
    return sum((int(x) * int(y) for x, y in re.findall(r"mul\((\d+),(\d+)\)", s)))


print("part one answer:", fixmem(mem))

first, *rest = mem.split("don't()")
print(
    "part two answer:",
    fixmem(first) + sum((fixmem("".join(chunk.split("do()")[1:])) for chunk in rest)),
)
