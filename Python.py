n = input()
s = n.count('9')
m = n.count('0')
if m >= s:
    print(0)
else:
    print(9)