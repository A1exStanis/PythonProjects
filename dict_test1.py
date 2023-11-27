string = input('Enter your string: ')
d = {}
for i in string:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
for i in sorted(d):
    print(i,d[i])