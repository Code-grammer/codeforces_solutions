entries,benchmark = input().split(" ")
list2 = input().split(" ")
val = int(list2[int(benchmark)])
c = 0
for i in range(0,int(entries)):
    n = int(list2[i])
    if (n > 0) & (n >= val):
        c += 1
print(c)