# 입력
# 첫째 줄에 두 정수 N, M(1 ≤ N, M ≤ 300)이 주어진다.

# 처리
# 초콜릿을 최소 횟수로 자른다.
# count = N-1 + N(M-1)개로 최소 횟수로 나눈다.

# 출력
# 첫째 줄에 답을 출력한다.


N, M = map(int, input().split()) 
print( N-1 + (N * (M-1)) ) 
