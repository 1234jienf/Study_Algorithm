def solution(sequence, k):
    # 초기 길이 체크
    length = len(sequence)
    # 끝지점 체크
    end = 0
    # 합을 계산할 변수
    total = 0
    # 길이를 저장해둘 변수
    check = length
    # 정답
    answer = []

    for i in range(length):
        # 총합이 목표값보다 작고 길이가 끝이 아닌 경우
        while total < k and end < length:
            # 합을 계속 더해나감
            total += sequence[end]
            # end 값 1씩 더해감
            end += 1
        # 반복문이 끝났을때 총합이 k 보다 같거나 클 경우이며 
        # 총합이 k 와 같고 index 가 check 값보다 작은 경우
        # 끝 부분 값을 계속해서 check 에 덮어 씌워주기 때문에 answer 에 값 저장
        if total == k and end-1-i < check:
            answer = [i, end-1]
            check = end-1-i
        total -= sequence[i]
    
    return answer