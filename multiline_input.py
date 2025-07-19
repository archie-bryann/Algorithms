import sys

# multiline_input = sys.stdin.read().splitlines()

group = []

while True:
    s = input()
    if s != "":
        group.append(s)
    else:
        break

print(group)
# print(list(group))