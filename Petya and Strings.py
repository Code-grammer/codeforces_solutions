first_string = input().lower()
second_string = input().lower()

m = []
for i in range(0,len(first_string)):
    if first_string[i] < second_string[i]:
        m.append('-1')
        break
    elif first_string[i] > second_string[i]:
        m.append('1')
        break
if len(m) == 0:
    print('0')
else:
    print(m[0])