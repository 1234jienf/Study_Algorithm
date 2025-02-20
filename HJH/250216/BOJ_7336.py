# 실제 idx를 바꾸며 작업한다.
# 검사할 idx로 시작하여 검사 끝난 다음 idx로 값을 설정한다.
def retNoSpace() -> str:
    global s, idx
    ans = ''
    while s[idx[0]] != ')':
        if s[idx[0]] == '(':
            idx[0] += 1
            whatIsInHere = retNoSpace()
            if len(whatIsInHere) == 1:
                ans = ans + whatIsInHere
            else:
                if ans != '' and ans[-1] == '-':
                    ans = ans + '(' + whatIsInHere + ')'
                else:
                    ans = ans + whatIsInHere
        elif s[idx[0]] == ' ':
            pass
        else:
            ans = ans + s[idx[0]]
        idx[0] += 1

    return ans

n = int(input())
ans = ''
for _ in range(n):
    s = input() + ')'
    idx = [0]
    ans = ans + retNoSpace() + '\n'
print(ans)