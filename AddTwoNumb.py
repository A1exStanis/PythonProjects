
def addTwoNumbers(l1:list, l2:list) ->list:
    l3 = []
    cur = 0
    for i, il in enumerate(l1):
        if il+l2[i]>=10:
            l3.append((il+l2[i])%10+cur)
            cur = 1
        else:
            l3.append(il+l2[i]+cur)
            cur = 0
    return l3

addTwoNumbers([2,4,3], [5,6,4])