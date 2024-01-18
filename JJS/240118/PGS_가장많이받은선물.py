import numpy as np

def solution(friends, gifts):
    # 각 친구의 인덱스를 빠르게 조회하기 위한 사전 생성
    dic = {f: i for i, f in enumerate(friends)}
    
    # 선물 교환 횟수를 저장할 2차원 테이블 초기화
    table = [[0] * len(friends) for _ in range(len(friends))]
    
    # 각 친구가 준 선물의 총 횟수를 추적하기 위한 리스트 초기화
    presents = [0] * len(friends)
    
    # 입력을 기반으로 선물 교환 테이블 작성 
    for gift in gifts:
        giver, taker = gift.split()
        table[dic[giver]][dic[taker]] += 1
    
    # NumPy 배열로 변환하여 편리하게 합을 계산
    array = np.array(table)
    
    # 각 친구가 받은 선물과 준 선물의 총 횟수 계산
    t_given = array.sum(axis=1)
    t_taken = array.sum(axis=0)
    
    # 각 친구의 "순" 선물 주고 받은 횟수 계산
    jisu = list(t_given - t_taken)
    
    # 친구 쌍에 대해 반복하며 더 많은 선물을 준 친구를 갱신
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]:  # 만약 i가 j에게 더 많은 선물을 줬다면
                presents[i] += 1
            elif table[j][i] > table[i][j]:  # 만약 j가 i에게 더 많은 선물을 줬다면
                presents[j] += 1
            else:  # 만약 선물 교환이 동일하다면
                if jisu[i] > jisu[j]:  # 만약 i의 순 선물 주고 받은 횟수가 더 높다면
                    presents[i] += 1
                if jisu[j] > jisu[i]:  # 만약 j의 순 선물 주고 받은 횟수가 더 높다면
                    presents[j] += 1
    
    # 어떤 친구가 최대로 선물을 준 횟수를 반환
    return max(presents)

