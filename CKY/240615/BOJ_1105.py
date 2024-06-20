L, R = map(str,input().split())
# 인풋 값의 길이 측정
L_length = len(L)
R_length = len(R)
# 각 인풋에서 들어온 값들에 8 이 있는지 체크하고 없으면 무조건 0 이 나오게 된다.
# 또한 각각 길이를 비교하여 두 길이가 다른경우도 무조건 0이 나오게된다.
if L.count("8") == 0 or R.count("8") == 0 or L_length != R_length:
    print(0)
# 외의 경우
else:
    # cnt 변수를 선언해주고
    cnt = 0
    # 길이가 같기 때문에 두 인덱스의 값을 비교하며 같은경우 8인지 확인하고 8인 경우 cnt 를 증가
    for i in range(L_length):
        if L[i] == R[i]:
            if L[i] == "8":
                cnt += 1
        # 같지 않은 경우 cnt 를 출력하고 break를 시행
        else:
            print(cnt)
            break
    # break가 걸리지 않을 경우 cnt 출력
    else:
        print(cnt)