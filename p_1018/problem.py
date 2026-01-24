M, N = map(int, input().split())
board = [input() for _ in range(M)] # 2차원 배열로 입력 받기
results = []

# (i, j)는 8x8로 자를 영역의 왼쪽 위 시작점
for i in range(M - 7):
    for j in range(N - 7):
        draw1 = 0 # 'W'로 시작하는 경우
        draw2 = 0 # 'B'로 시작하는 경우

        # 시작점부터 8x8 영역 탐색
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 행+열 인덱스 합이 짝수인 칸
                    if board[a][b] != 'W': draw1 += 1
                    if board[a][b] != 'B': draw2 += 1
                else: # 행+열 인덱스 합이 홀수인 칸
                    if board[a][b] != 'B': draw1 += 1
                    if board[a][b] != 'W': draw2 += 1
        
        results.append(draw1)
        results.append(draw2)

print(min(results))