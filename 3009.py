# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

# 로직
# 사각형의 좌표는 각각 2개의 x, y좌표를 가진다.
# => 따라서, 입력값 중 1개만 존재하는 좌표가 미지수다.


def coordinate(x, y, z):
    if x == y: 
        return z
    
    elif x == z:
        return y
    
    else:
        return x

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())    

print(coordinate(a, c, e), coordinate(b, d, f))
