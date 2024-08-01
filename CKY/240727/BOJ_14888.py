def backtracking(index):
    global N
    global min_value
    global max_value
    # 백트래킹 마지막 도달
    if index == N-1:
        # 추가되지 않은 마지막 숫자 추가
        ans.append(num_list[index])
        # 초기 계산값으로 0번 인덱스 숫자
        check = num_list[0]
        # 현재 리스트 길이 측정
        list_length = len(ans)
        # 총 길이가 숫자 리스트 + 연산자로 구성됐기 때문에 N + N-1 까지 비교
        if list_length == (N+N-1):
            # 총 길이가 될 경우 반복문에서 연산자 이후 값을 비교
            for k in range(0,list_length,2):
                # 이전 연산자의 기호에 따라서 연산 방법을 적용
                if ans[k-1] == "+":
                    check += ans[k]
                elif ans[k-1] == "-":
                    check -= ans[k]
                elif ans[k-1] == "*":
                    check *= ans[k]
                #  음수 연산의 경우 - 부호 제거 후 계산 다음 - 붙임
                elif ans[k-1] == "//":
                    if check < 0:
                        check = abs(check)
                        check //= ans[k]
                        check = -check
                    else:
                        check //= ans[k]
            # 최대, 최소값 갱신
            if check > max_value:
                max_value = check
            
            if check < min_value:
                min_value = check
        ans.pop()
        return
    
    for i in range(index,N):
        ans.append(num_list[i])
        for j in operator_list:
            # 연산자 개수가 사용이 가능한지 체크
            if operator_dict[j] != 0:
                operator_dict[j] -= 1
                ans.append(j)
                backtracking(i+1)
                ans.pop()
                operator_dict[j] += 1
        ans.pop()

N = int(input())

num_list = list(map(int,input().split()))

operator_dict = {
    "+": 0,
    "-": 0,
    "*": 0,
    "//": 0
}
# 연산자 개수 딕셔너리에 저장
plus, minus, multi, div = map(int,input().split())
operator_dict["+"] = plus
operator_dict["-"] = minus
operator_dict["*"] = multi
operator_dict["//"] = div
operator_list = ["+","-","*","//"]
min_value = 10**9
max_value = -(10**9)
ans = []

backtracking(0)

print(max_value,min_value)