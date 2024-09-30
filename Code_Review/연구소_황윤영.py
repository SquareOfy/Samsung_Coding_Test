"""
총 풀이시간 23분
실행시간 308ms
메모리 115744kb
1610 문제 이해 (어렵지 않았음)
1617 구현시작
        - 빈칸 lst에 넣을 때 0일때가 아니라 2일 때 넣는 실수
        - 바이러스 퍼뜨릴 때 0인 곳으로만 퍼뜨리는 조건문 누락함

1633 정답


* 아쉬운 점
    자신있어하는 유형이지만, 자잘한 실수가 아직 많다
    머릿 속에 벽을 세우겠다는 문제 맥락을 넣어두고, 문제 조건보다 그 맥락대로 문제를 풀이하는 경향이 있는듯하다
    빈칸 리스트를 만들 때 빈칸(0)인 곳을 넣어두고 나중에 1로 만든다는게 1인 곳의 위치를 넣는 등의 실수처럼
    ...
"""
from collections import deque

#앞에서 채운 다음 위치부터 보게 하여
# 매번 조건문으로 해당 칸에 벽이 세워졌는지 확인할 필요 없도록 함
def dfs(level, idx):
    global answer
    if level==3:
        # 벽 3개 다 세웠으면 바이러스 퍼뜨리기
        cnt = bfs() #퍼진 개수
        answer = max(answer, safe-3-cnt)
        return
    for i in range(idx, b):
        r, c = blanks[i]
        arr[r][c] = 1
        dfs(level+1, i+1)
        arr[r][c] = 0

def bfs():
    q = deque(virus)
    visited = [[0]*m for _ in range(n)]
    for i, j in virus:
        visited[i][j] = 2
    cnt = 0

    while q:
        r, c = q.popleft()

        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            du = r+di
            dv = c+dj
            if du<0 or dv<0 or du>=n or dv>=m:
                continue
            if visited[du][dv]:
                continue
            if arr[du][dv]!=0:
                continue
            visited[du][dv] = 2
            q.append((du, dv))
            cnt+=1
    # print()
    # for i in range(n):
    #     print(arr[i])
    # print()
    # print()
    # for i in range(n):
    #     print(visited[i])
    # print()

    return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
blanks = [] #초기 빈칸(벽을 세울 후보들)
virus = [] #초기 바이러스 위치 (bfs에서 deque 선언시 활용)
safe = 0 #초기 빈칸 개수
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            safe+=1
            blanks.append((i,j))
        elif arr[i][j]==2:
            virus.append((i, j))

b = len(blanks)
#빈칸 중에 3곳 고르기
dfs(0, 0)
print(answer)