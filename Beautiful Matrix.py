row = 0
col = 0
for i in range(1,6):
    j = input().split(" ")
    for m in range(0,5):
        if j[m] == '1':
            col = m+1
            row = i
print(abs(3-row)+abs(3-col))