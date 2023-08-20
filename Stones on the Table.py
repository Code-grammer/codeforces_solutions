x = int(input())
y = input()
l = []
n = y[0]
cnt = 0
for i in range(1,len(y)):
    if y[i] == n:
        cnt += 1
    else :
        n = y[i]

print(cnt)