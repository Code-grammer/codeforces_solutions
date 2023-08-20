x = list(map(int,input().split("+")))

x.sort()
out = ''
for i in x:
    if out == '':
        out = str(i)
    else:
        out = out + '+' +str(i)
print(out)