x = int(input())

list1 = []
n = 0
for i in range(0,x):
    y = input()
    list1.append(y)

for i in list1:
    num1 = 0
    num0 = 0
    for j in i:
        if j == '1':
            num1 = num1 + 1
        elif j == '0':
            num0 = num0 + 1
    if num1 > 1:
        n += 1

print(n)