n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))

# a = 0b111111111111111
# print(a)
def getbits(choice) -> list:
    ans = []
    bit = 0
    while choice != 0:
        if choice % 2 == 1:
            ans.append(bit)
        choice //= 2
        bit += 1
    return ans


def check(choice) -> bool:
    bits = getbits(choice)
    if len(bits) < 2:
        return False
    
    maximum = -1
    minimum = 10000000
    total = 0
    for bit in bits:
        maximum = max(maximum, arr[bit])
        minimum = min(minimum, arr[bit])
        total += arr[bit]
        
    if l <= total <= r and maximum - minimum >= x:
        return True
    return False
    

top = 1 << n
ans = 0
for choice in range(top):
    if check(choice):
        ans += 1

print(ans)