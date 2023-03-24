# 문제
# 준희는 자기가 팀에서 귀여움을 담당하고 있다고 생각한다. 하지만 연수가 볼 때 그 의견은 뭔가 좀 잘못된 것 같았다. 그렇기에 설문조사를 하여 준희가 귀여운지 아닌지 알아보기로 했다.

# 입력
# 첫 번째 줄에 설문조사를 한 사람의 수 N (1 ≤ N ≤ 101, N은 홀수)가 주어진다.

# 다음 N개의 줄에는 각 줄마다 각 사람이 설문 조사에 어떤 의견을 표명했는지를 나타내는 정수가 주어진다. 0은 준희가 귀엽지 않다고 했다는 뜻이고, 1은 준희가 귀엽다고 했다는 뜻이다.

# 출력
# 준희가 귀엽지 않다는 의견이 더 많을 경우 "Junhee is not cute!"를 출력하고 귀엽다는 의견이 많을 경우 "Junhee is cute!"를 출력하라.


# 1. 조건식 이용
# N = int(input())

# count_0 = count_1 = 0

# for _ in range(N):
#     x = int(input())

#     if x == 1:
#         count_1 += 1
    
#     elif x == 0:
#         count_0 += 1
    

# if count_0 > count_1:
#     print("Junhee is not cute!")
    
# elif count_0 < count_1:
#     print("Junhee is cute!")


# 2. 리스트 이용
N = int(input())
result = [] 

for _ in range(N):
    result.append(int(input()))

    if result.count(1) > result.count(0):
        print("Junhee is cute!")
    
    else: 
        print("Junhee is not cute!")  