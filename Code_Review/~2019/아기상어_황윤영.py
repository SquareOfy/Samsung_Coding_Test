"""
1차
풀이 시간 : 38분
시도 횟수 : 1회
실행 시간 :152ms
메모리 : 114684kb

2차
풀이 시간 : 23분
시도 횟수 : 2회
실행 시간 : 192ms
메모리 : 114872kb


실수 모음 
- 꼼꼼하지 못한 설계 9인 칸 0으로 안바꿔줌
- rank 더 클 때 무조건 바꿔주기 안함

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 행열 우선순위 bfs순서로 해결 안되는 것 주의
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : no. 구현량이 많지 않았음
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : no... 왜 안했지 ,, 반성
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""

"""
=================== 2차 코드 리뷰 ==================
1413 문제 읽기 시작  주석정리
1419 설계 
    전반적인 코드 작성함
1424 구현시작
1451 제출 후 오답
    코드 다시 뜯어보기
    너무 졸렸음,, 이 시간에 졸리면 안되는데 ㅠ 
    rank 값 갱신되는 경우!! 무조건 답으로 교체하도록 수정
    9인 곳 0으로 안바꿔준 것 발견
    
1437 정답

총평 
- 다시 푸는 문제도 긴장하고 꼼꼼히 설계하자 .
"""
"""
n * n 격자판에 m개의 몬스터와 하나의 전투로봇
한 칸에는 몬스터가 최대 하나만 존재
초기의 전투로봇의 레벨은 2,  전투로봇은 1초에 상하좌우로 인접한 한 칸씩 이동

자신의 레벨보다 큰 몬스터가 있는 칸은 지나칠 수 없고, 나머지 칸은 모두 지날 수 있습니다. 
전투로봇은 자신의 레벨보다 낮은 몬스터만 없앨 수 있습니다. 

없앨 수 있는 몬스터가 있다면 해당 몬스터를 없애러 갑니다.
없앨 수 있는 몬스터가 하나 이상이라면, 거리가 가장 가까운 몬스터를 없애러 갑니다.
    거리는 해당 칸으로 이동할 때 지나야하는 칸의 개수의 최솟값
    가장 가까운 거리의 없앨 수 있는 몬스터가 하나 이상
    => 가장 위에 존재하는 몬스터 ->  가장 왼쪽에 존재하는 몬스터
없앨 수 있는 몬스터가 없다면 일을 끝냅니다.

전투로봇이 한 칸 이동하는데에는 1초
몬스터를 없애는 시간은 없다.  몬스터가 있는 칸에 도달하면 바로 몬스터가 없어집니다. 
몬스터를 없애면 해당 칸은 빈칸
전투 로봇은 본인의 레벨과 같은 수의 몬스터를 없앨 때마다 레벨이 상승

전투 로봇이 일을 끝내기 전까지 걸린 시간
"""
from collections import deque

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def find_monster():
    q= deque([(r, c, 0)])
    visited=  [[0]*N for _ in range(N)]
    visited[r][c] = 1
    ar, ac = N, N
    arank = N*N
    while q:
        cr, cc, rank = q.popleft()
        if arr[cr][cc] != 0 and arr[cr][cc] < level and arank>=rank:
            if arank>rank or (arank==rank and (ar, ac)>(cr, cc)):
                ar, ac = cr, cc
                arank = rank

            continue
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            du, dv = cr+di, cc+dj
            if oob(du, dv): continue
            if visited[du][dv]: continue
            if arr[du][dv]>level: continue
            q.append((du, dv, rank+1))
            visited[du][dv] = 1

    return ar, ac, arank

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            r, c = i, j
            arr[i][j] = 0
level = 2
cnt = 0
answer = 0
while 1:

    nr, nc, time = find_monster()
    if nr==N:
        break

    r, c = nr, nc
    answer += time
    arr[r][c] = 0
    cnt+=1
    if cnt==level:
        level+=1
        cnt=0
print(answer)

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
