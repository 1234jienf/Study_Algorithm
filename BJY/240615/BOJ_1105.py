## 문제

## L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 
## 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.

## 입력

## 첫째 줄에 L과 R이 주어진다. 
## L은 2,000,000,000보다 작거나 같은 자연수이고, 
## R은 L보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다.

## 출력

## 첫째 줄에 L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 
## 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.


L, R = map(str,input().split())

answer = 0
cnt = 0
eight = 0
def check_8(L,R):
  global cnt
  global eight
  if "8" not in L or "8" not in R:
    return 0
  else:
    if len(L) != len(R):
      return 0
    else:
      for i in range(len(L)):
        if L[i] == R[i]:
          if L[i] == '8':
            eight += 1
        else:
          break
      return eight

answer = check_8(L,R)
print(answer)