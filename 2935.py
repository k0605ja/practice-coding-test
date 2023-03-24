# 입력
# 첫째 줄에 양의 정수 A가 주어진다.
# 둘째 줄에 연산자 + 또는 *가 주어진다.
# 셋째 줄에 양의 정수 B가 주어진다.
# A와 B는 모두 10의 제곱 형태이고, 길이는 최대 100자리이다.

# 출력
# 첫째 줄에 결과를 출력한다. 결과는 A+B 또는 A*B이며, 입력에서 주어지는 연산자에 의해 결정된다. 


x = int(input())
operator = str(input())
y = int(input())

result = 0

if operator == '+':
    result = x+y
elif operator == '*':
    result = x*y

print(result)