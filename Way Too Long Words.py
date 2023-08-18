x = int(input())

list1 = []
list2 = []
for i in range(0,x):
    y = str(input())
    list1.append(y)

for i in list1:
    if len(i) <= 10:
        list2.append(i)
    else:
        abr = i[0]+str(len(i)-2)+i[len(i)-1]
        list2.append(abr)

for x in list2:
    print(x)