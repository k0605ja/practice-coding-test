# 문제
# 두 숫자 R1과 R2가 있을 때, 두 수의 평균 S는 (R1 + R2) / 2와 같다. 
# R2가 몇 인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 정수 R1과 S가 주어진다. 두 수는 -1000보다 크거나 같고, 1000보다 작거나 같다.

# 출력
# 첫째 줄에 R2를 출력한다.

# 로직
# S 공식을 이용해서 R2를 구하는 식을 구한다. (R2 = 2S -R1)



R1, S = map(int, (input().split())) 

R2 = -R1 + (S * 2)

print(R2)