a = input().count('1')
b = input().count('1')
a += a % 2
if a >= b:
    print('VICTORY')
else:
    print('DEFEAT')