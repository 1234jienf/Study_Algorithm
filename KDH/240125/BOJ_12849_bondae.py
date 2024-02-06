sungsil = [[],[2,3],[1,3,4],[1,2,4,5],[2,3,5,6],[3,4,6,8],[4,5,7],[6,8],[5,7]]
sungsil2 = [[],[2,3],[3,4],[2,4,5],[2,3,5,6],[3,4,6,8],[4,5,7],[6,8],[5,7]]

# ddddddddd = 0    1       2       3          4         5        6      7     8  

D = int(input())

DP = [0]*(D+1)

for i in range(D+1):
    for j in range(i):
        DP[i] += DP[j]
        if i <9:
            for k in sungsil2[i]:
                DP[i] += len(sungsil2[k])
        else:
            mok = i//8
            namuji = 8-(i%8)
            for k in sungsil2[namuji]:
                DP[i] += len(sungsil2[k])



print(DP[D])