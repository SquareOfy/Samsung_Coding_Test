"""
총 풀이시간 38분
사다리조작 문제 보고 빠르게 아기상어로 도망 왔다

1505 문제 읽기 시작
     전 날 봤던 문제라 이해는 어렵지 않았음
     전 날 테케 자꾸 안맞는 문제 있었어서 아예 다시 처음부터 짜보기로 함
1521 구상 완료 및 구현 시작
1545 구현완료 및 정답

전 날 실패요인 분석
1. bfs에서 방향백터 순서를 위쪽, 왼쪽 우선으로 하면
    좌표도 우선순위대로 먼저 나올거라고 잘못 생각함!!! 아닐 수 있따 !!
2. 추후 1을 깨닫고 고쳤으나 초기 값을 -1로 해둔 것으로 추가 조건이 생겨 실수가 있었다
    오늘은 초기 좌표를 크게 잡아 한번에 처리 가능했다.
    오늘 코드리뷰를 통해 그냥 튜플로 대소비교를 해도 가능하다는 사실을 새로 배움


"""

from collections import deque
def find_shark():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j

def bfs(i, j):
    q = deque([(i, j, 1)]) #상어 좌표
    visited = [[0]*n for _ in range(n)]
    visited[i][j] = 1
    t = n*n
    ar, ac = n, n
    while q:
        cr, cc, rank = q.popleft()
        #먹을 수 있는 물고기라면
        if rank <= t and arr[cr][cc] != 0 and arr[cr][cc] < size:
            #먹을 물고기 좌표 갱신
            t = rank
            if cr < ar:
                ar, ac = cr, cc
            elif cr==ar and cc<ac:
                ac = cc
            continue
        for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
            du = cr+di
            dv = cc+dj
            if du<0 or dv<0 or du>=n or dv>=n:
                continue
            #이미 방문한 곳, 먹을 수 없는 물고기는 방문 x
            if visited[du][dv] or arr[du][dv] > size:
                continue
            visited[du][dv] = 1
            q.append((du, dv, rank+1))
    return ar, ac, t-1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sr, sc = find_shark()
answer = 0
size = 2
cnt = 0

while 1:
    sr, sc, time = bfs(sr, sc)
    if sr == n:
        break
    answer += time
    cnt += 1
    arr[sr][sc] = 0

    if cnt == size:
        size+=1
        cnt = 0

print(answer)
