x = input()
l1 = []
for i in x:
    if i not in l1:
        l1.append(i)
    else:
        pass
if len(l1)%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")