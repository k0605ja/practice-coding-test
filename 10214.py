# 입력
# 입력 파일의 첫 번째 줄에 테스트 케이스의 수를 의미하는 자연수 T가 주어진다. 그 다음에는 T개의 테스트 케이스가 주어진다.

# 각 테스트 케이스는 9줄에 걸쳐서 입력되며, 매 줄마다 해당 회의 연세대 득점 Y와 고려대 득점 K가 공백으로 구분되어 주어진다. 이 두 수는 0이상 9이하이다.

# 출력
# 각각의 케이스마다 한 줄에 연세대가 이겼을 경우 "Yonsei", 고려대가 이겼을 경우 "Korea", 비겼을 경우 "Draw"를 출력한다.


T = int(input()) # 테스트 케이스 입력

for _ in range(T):
        
        # 각 학교의 총점을 저장할 변수 선언
        Yonsei_score = Korea_score = 0

        for _ in range(9):
           
           Y, K = map(int, input().split())

           # 9번 반복하며 총 점수 합산
           Yonsei_score += Y
           Korea_score += K

        
        if Yonsei_score > Korea_score:
            print("Yonsei")
        elif Yonsei_score == Korea_score:
            print("Draw")
        elif Yonsei_score < Korea_score:
            print("Korea")
