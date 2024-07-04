N, K = map(int,input().split())

one_pos = 9
pos = 1
ans = 0
while K > one_pos*pos:
    K -= pos*one_pos
    ans += one_pos
    one_pos *= 10
    pos += 1
# K 번쨰 자리 숫자가 무엇인지 파악
print((K-1)//pos + 1, ans)
ans += ((K-1)//pos)+1
# K 번쨰 자리에서 몇번쨰 숫자를 가리키는지 출력
print(str(ans)[(K-1)%pos])

if ans > N:
    print(-1)
else:
    print(str(ans)[(K-1)%pos])

# 1~9 9자리 
# 10~99 180 자리 * 20
# 100~999 2700 자리 * 30
# 1000~999 36000 자리  * 40
# 자리수 * 9 * 10**(자리수-1) 이런 식으로 증가함
