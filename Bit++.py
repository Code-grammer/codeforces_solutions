x = int(input())
val = 0

for i in range(0,x):
    inp = input()
    if '--' in inp:
        val -= 1
    elif '++' in inp:
        val += 1
print(val)