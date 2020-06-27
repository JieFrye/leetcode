def getMin(s):
    '''
    ideas: if (, then we need ) (cancel)
    if ), add ( (count)
    '''
    count = 0
    stack = []
    # )()
    dic = {'(':')'} #cancel
    for p in s:
        if stack and p == stack[-1]:
            stack.pop()
        else:
            if p in dic:
                stack.append(dic[p])
            else: # add (
                count += 1
    return len(stack) + count


print(getMin('))()))'))
