# 해당 문제는 인공지능의 도움을 받음
import sys

# 1. 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.read
data = input().split()

# 2. 첫 번째 값은 N, 나머지는 정렬할 숫자들
N = int(data[0])
arr = list(map(int, data[1:]))

# 3. Python의 기본 정렬(Timsort)은 매우 효율적입니다 (O(N log N))
arr.sort()

# 4. 한 번에 합쳐서 출력하여 출력 속도 최적화
sys.stdout.write('\n'.join(map(str, arr)) + '\n')