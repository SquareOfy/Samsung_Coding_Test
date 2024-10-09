"""
1차
풀이 시간 : 52분
시도 횟수 : 1회
실행 시간 : 116 ms
메모리 : 113812 kb


2차
풀이 시간 : 20분
시도 횟수 : 1회
실행 시간 : 146ms
메모리 : 25 mb

- 실수 모음
    - N, M 실수
"""
"""
====================== 2차 코드 리뷰 ==================
1429 문제 읽기 + 주석정리 + 문제 읽자마자 주사위 굴리는 설계부터 해놓음
1438 설계할 것들 주석 메모 + 설계
1431 구현시작
1449 구현완료 제출 정답
"""
"""
1이상 6이하 중 임의의 숫자가 그려진 n * n 격자판에  한 면이 1 * 1 크기인 정육면체
m번에 걸쳐 주사위를 계속 1칸씩 굴리게 됩니다.
마주보는 면에 적혀있는 숫자의 합은 정확히 7
항상 초기에 격자판의 1행 1열에 놓여져 있고, 처음에는 항상 오른쪽으로 움직입니다.

주사위를 움직일때마다, 격자판 위 주사위가 놓여있는 칸에 적혀있는 숫자와
 상하좌우로 인접하며 같은 숫자가 적혀있는 모든 칸의 합만큼 점수를 얻게 됩니다.

 주사위의 아랫면이 보드의 해당 칸에 있는 숫자보다 크면 현재 진행방향에서 90' 시계방향으로 회전
 주사위의 아랫면의 숫자가 더 작다면 현재 진행방향에서 90' 반시계방향으로 회전

 만약 진행 도중 다음과 같이 격자판을 벗어나게 된다면,
 반사되어 방향이 반대로 바뀌게 된 뒤 한 칸 움직이게 됩니다.

 n * n 크기의 격자판의 상태가 주어졌을 때, m번 진행하며 얻게되는 점수의 총 합

"""
from collections import deque


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


# 1. 점수판 배열 구하기
def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    lst = []
    score = 0
    num = arr[i][j]

    while q:
        cr, cc = q.popleft()
        lst.append((cr, cc))
        score += num

        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv): continue
            if visited[du][dv]: continue
            if arr[du][dv] != num: continue
            q.append((du, dv))
            visited[du][dv] = 1

    for r, c in lst:
        visited[r][c] = score


# 2. 주사위 굴리는 함수 만들기
def move_dice(d):
    global bottom
    tmp = bottom
    bottom = side[d]
    side[d] = 7 - tmp
    side[(d + 2) % 4] = 7 - side[d]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
DIR = (0, 1), (-1, 0), (0, -1), (1, 0)

bottom = 6
side = [3, 5, 4, 2]
r, c = 0, 0
d = 0
answer = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

for m in range(M):
    di, dj = DIR[d]
    r += di
    c += dj
    if oob(r, c):
        d = (d + 2) % 4
        di, dj = DIR[d]
        r += di * 2
        c += dj * 2
    move_dice(d)
    answer += visited[r][c]
    if arr[r][c] > bottom:
        d = (d + 1) % 4

    elif arr[r][c] < bottom:
        # 시계 회전
        d = (d - 1) % 4
print(answer)

"""
총 풀이시간 52분
실행시간 116 ms
메모리 113812 kb


1404 두 문제 비교 후 선택 / 문제이해. 온풍기 안녕 안녕하고 여기로 왔다
        - 선택 이유 1 : 온풍기에 벽 개념 낯섬 + 단계 굉장히 많음+ 신경쓸 조건 많음
        - 선택 이유 2 : 최근 풀어본 주사위 굴리기의 구현 아이디어 가져다 쓰기 가능

        - 점수를 더한다는게 뭔말인지 이해안갔음 . 1칸 가는데 왜 네칸 값을 더하지?
            => 테케 비교하며 이해 완
            => 각 영역마다 더할 점수 미리 저장해놔야겠다고 생각함

        - 문제 읽으며 주사위 처음 위치 + 방향 이동에 따라
            주사위 동서남북 방향의 숫자 저장할 배열 어떻게 설계할지 함께 고민
        - 이 부분 슈더코드를 종이에 정리해 놓음
1426 설계한 내용 주석 정리 + 구현시작
        - 주사위 굴리는 부분이 복잡한 로직이므로 이를 위해 필요한 배열들부터 먼저 정리
        - 점수배열 bfs로 만들어두기
        - 주사위 굴리는 로직 슈더코드 덕에 이지했다
        - 주사위 회전 프린트로 중간체크 함 굿굿
1446 구현 후 디버깅 함
        - 단계별로 print 찍기 활용
        - 주사위 bottom이 다른 단계가 있음 확인 => 초기 주사위 배열 세팅 새로 해서 해결
        - 뭔가 덜 더해지는 값이 생김
        - 점수 배열 출력해서 확인했더니 0인 곳이 있따??
        - 코드 뜯어살피다가 n m 을 n n 이라고 한 실수 발견 => 해결
1456 제출 및 정답


피드백
- 잘한 점
    1. 요즘 뜸했던 슈더코드를 다시 시작함 (코드리뷰 때 광수님의 방법을 듣고 각성..! )
    2. 문제 이해 안갈 때 테케로 검증하며 확인한 것
    3. 온풍기로부터 도망을 잘 침

- 개선할 점
    1. 실수 ^_^ .... n, m 종이에 써놓고 안보면 안된다 !


"""
from collections import deque
def obb(y, x):
    return y<0 or y>=n or x<0 or x>=m
def set_score_arr():
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            cnt =0
            lst = []
            q = deque([(i, j)])
            visited[i][j] = 1
            v = arr[i][j]
            while q:
                cr, cc = q.popleft()
                lst.append((cr, cc))
                cnt+=1
                for di, dj in directions:
                    du = cr + di
                    dv = cc + dj
                    if obb(du, dv) or visited[du][dv]:
                        continue
                    if arr[du][dv]==v:
                        q.append((du,dv))
                        visited[du][dv] = 1

            s = cnt*v if cnt !=0  else v
            for nr, nc in lst:
                score[nr][nc] = s

#입력
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
#방향 배열, 주사위 배열 세팅
side = [3, 5, 4, 2]  #동 남 서 북 순
directions = (0, 1), (1, 0), (0, -1), (-1, 0) #동남서북
d = 0 #동쪽 방향으로 시작
bottom = 6

#arr 자리별 점수 세팅
score = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
set_score_arr()

# for i in range(n):
#     print(score[i])
# # 점수배열 체크 완


#주사위 굴리기 k번 시작
#시작 0, 0
r, c = 0, 0
answer = 0
for i in range(k):
    di, dj = directions[d]
    nr = r+di
    nc = c+dj

    #범위 벗어나는지 체크하고 벗어나면 방향 반대로
    if obb(nr, nc):
        d = (d+2)%4
        di, dj = directions[d]
        nr = r+di
        nc = c+dj
    #그 칸으로 이동(주사위 bottom, side 변동)
    r = nr
    c = nc
    side[(d+2)%4] = bottom
    bottom = side[d]
    side[d] = 7-side[(d+2)%4]

    #이동한 칸의 점수 answer에 더하기
    answer += score[r][c]

    #주사위 회전여부 판단

    # print(f"============={i}=================")
    # print(r+1, c+1)
    # print("회전 전 d : ", d)

    if bottom > arr[r][c]:
        d = (d+1)%4
    elif bottom < arr[r][c]:
        d = (d+3)%4
    # print(arr[r][c])
    # print("bottom : ", bottom)
    # print("회전 후 d : " , d)
    # print(score[r][c])
    # print('=================================')
print(answer)