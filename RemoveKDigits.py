
# 5/13
#num = "1432219"
#num = "1431199" #1119
#num = "1001211"
num = "102300"
k = 2
def removekdigits(num: str, k: int) -> str:
    '''
    remove k digits from num so that the new num is the smallest possible.
    idea:
    remove the digit when its next is smaller.
    remove last digit if in increasing order.
    '''
    if len(num) == k:
        return '0'
    for _ in range(k):
        i = 0
        while i < len(num) - 1 and num[i] <= num[i+1]:
            i += 1
        # remove the digit when its next is smaller
        num = num[:i] + num[i+1:]
    # remove leading zeros
    while len(num) > 1 and num[0] == '0':
        num = num[1:]
    if len(num) == 0:
        return '0'
    return num

print(removekdigits(num, k))
