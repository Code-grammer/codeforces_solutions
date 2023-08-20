y = str(input()).lower()
l1 = ["a","e","i","o","u","y"]
l2 = ''
for i in y:
    if i in l1:
        pass
    else :
        l2 += "."
        l2 += i
print(l2)

