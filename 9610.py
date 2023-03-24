# 문제
# 2차원 좌표 상의 여러 점의 좌표 (x,y)가 주어졌을 때, 각 사분면과 축에 점이 몇 개 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 n (1 ≤ n ≤ 1000)이 주어진다. 다음 n개 줄에는 점의 좌표 (xi, yi)가 주어진다. (-106 ≤ xi, yi ≤ 106)

# 출력
# 각 사분면과 축에 점이 몇 개 있는지를 예제 출력과 같은 형식으로 출력한다.


AXIS = Q1 = Q2 = Q3 = Q4 = 0


for _ in range(int(input())):

    x, y = map(int, input().split())

    if x == 0 or y == 0:
        AXIS += 1

    elif x > 0 and y > 0:
        Q1 += 1

    elif x < 0 and y > 0:
        Q2 += 1

    elif x < 0 and y < 0:
        Q3 += 1
        
    elif x > 0 and y < 0:
        Q4 += 1


print("Q1: %s" %(Q1))
print("Q2: %s" %(Q2))
print("Q3: %s" %(Q3))
print("Q4: %s" %(Q4))
print("AXIS: %s" %(AXIS))