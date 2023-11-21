a, b = map(int, input().split())
bl = []
for q in range(a):
    list_ = list(map(str, input().split()))
    bl.append(list_)
for i in bl:
    if ('Y' or 'M' or 'C') in i:
        print('Color')
    else:
        print('Black&White')
