"""
1차
풀이 시간 : 1시간 12분
시도 횟수 : 1회
실행 시간 : 278ms
메모리 : 27mb

2차
풀이 시간 : 1시간
시도 횟수 : 1회
실행 시간 : 250ms
메모리 : 26mb

- 실수 모음
    - 문제 이해 실수 : 최단거리 공식 알려준 적 없음! bfs 돌려봐야했다
    - 사용할 변수 헷갈림 이슈 ! : 목적지 찾을 때 넣어야하는 인덱스가 for문 인덱스가 아닌데 실수함 * 2번다 !!
    - bfs continue 조건 누락
"""
"""
======================= 2차 코드 리뷰 ========================
1904 문제읽기 + 주석 + 설계
1919 구현시작
    - 구현하다가 최단거리 잘못 이해한거 깨닫고 다시 구현
    
1949 디버깅
    에러 
    목적지 구하는 인덱스 잘못 넣은 것 깨닫고 고침
    
    답틀림
    움직임 전 후 프린트 디버깅
    움직인 위치 이상하다. mn_dist 적용해서 구해오기 
    
    제출 후 에러 오답
    return이 안된다. 길이 막힌다.
    프린트해서 잘못 좌표 잡는 부분 없는지 체크 
    가장 최단거리 베이스캠프 잘못 찾아오는 부분 확인함(손으로 따라가기 + 프린트디버깅)
    bfs continue 조건 누락 확인 .. 담엔 코드 먼저 보도록 ;; 
    
    
"""
"""
빵을 구하고자 하는 m명의 사람

 1번 사람은 정확히 1분에,...,
  m번 사람은 정확히 m 분에 각자의 베이스캠프에서 출발하여 편의점으로 이동

사람들이 목표로 하는 편의점은 모두 다릅니다.

1.
격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
최단거리 : 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여
        도달하기까지 거쳐야 하는 칸의 수가 최소가 되는 거리

2.
편의점에 도착한다면 해당 편의점에서 멈추게 되고
다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다
격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐

3.
시간이 t분이고 t ≤ m를 만족
t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
우선순위 : 행이 작은 베이스캠프, 행이 같다면 열이 작은 베이스 캠프로
이때부터 다른 사람들은 해당 베이스 캠프가 있는 칸을 지나갈 수 없게 됩니다.


"""
from collections import deque


def calculate_dist(r, c, sr, sc):
    return abs(r - sr) + abs(c - sc)


def get_move_loc(i, j, gi, gj):
    q = deque([(i, j, 0, i, j)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while q:
        cr, cc, rank, fr, fc = q.popleft()
        if cr == gi and cc == gj:
            return fr, fc
        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv): continue
            if arr[du][dv] < 0: continue
            if visited[du][dv]: continue
            visited[du][dv] = 1
            if rank == 0:
                q.append((du, dv, rank + 1, du, dv))
            else:
                q.append((du, dv, rank + 1, fr, fc))
    # return -1, -1

def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


def find_base(sr, sc):
    q = deque([(sr, sc, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    rr, rc = N, N
    mn_dist = N*N

    while q:
        cr, cc, rank = q.popleft()
        if arr[cr][cc] == 1:
            if rank < mn_dist:
                rr, rc = cr, cc
                mn_dist = rank
            elif rank == mn_dist and (rr, rc) > (cr, cc):
                rr, rc = cr, cc
            continue
        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv): continue
            if visited[du][dv]: continue
            if arr[du][dv]<0: continue
            q.append((du, dv, rank+1))
            visited[du][dv] = 1
    # print("거리 : ", mn_dist)
    return rr, rc

# 인덱스 1부터 시작!!
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# move_arr =[[[] for _ in range(N)] for _ in range(N)]
store_lst = [-1]
moving_lst = []
arrived_cnt = 0
DIR = (-1, 0), (0, -1), (0, 1), (1, 0)
time = 0
for m in range(M):
    x, y = map(lambda x: int(x) - 1, input().split())
    store_lst.append((x, y))





while arrived_cnt < M:
    time += 1
    # 이동
    arrived_lst = []
    for m in range(len(moving_lst)):
        if moving_lst[m] == -1:
            continue

        num, r, c = moving_lst[m]
        sr, sc = store_lst[num]

        nr, nc = get_move_loc(r, c, sr, sc)

        if nr == sr and nc == sc:
            arrived_cnt+=1
            moving_lst[m] = -1
            arrived_lst.append((sr, sc))
        else:
            moving_lst[m] = (num, nr, nc)

    for x, y in arrived_lst:
        arr[x][y] = -1

    # 새로운 애 투입
    if time <= M:
        sr, sc = store_lst[time]
        br, bc = find_base(sr, sc)
        arr[br][bc] = -1
        moving_lst.append((time, br, bc))
print(time)


"""
풀이시간 1시간 12분

실행시간 278ms  => 줄여보자 유녕아 ..
메모리 27mb

1400 ~ 1405 2번문제 읽어봄
            오전에는 확실히 N, M 이 겁나 커서 그래 이거 2번이다 했는데
            시뮬레이션 문제 풀면서 컨테이너 어쩌고 하는 것도 몇번 보기도 했고,
            N이 엄청나게 크지 않아서 실제 시험이었으면 잉? 바뀐건가? 라는 생각이 조금 들었을 지도?
            하지만 10만도 충분히 크다 하나만 10만이 아니었으니까
            게다가 코드트리빵 문제도 상당히 복잡한 편이어서 ..
            그래도 코드트리빵 N범위, 시키는 동작의 복잡성 등 고려해서 이거 골랐을듯
1404 문제 읽고 조건 정리
    (정독만 8분...)
    종이 x 주석 x 그냥 무조건 정독. 동작 설명이 꽤나 복잡하고 낯선 느낌이라
    시간을 여유있게 두고 읽으려고 노력했음.
    글자 하나하나 짚어가며, 방금 읽은 내용 이해 됐는가 생각하고 안되면 다시 읽어보기 반복함

    문제 절차 및 필요한 조건 복사해서 구현하기 위한 공간 남기고 구현할 순서대로 주석으로 복사
    이 때 베이스캠프 찾는 절차를 앞으로 뺄까 잠깐 고민했지만 괜한 모험하지 말고 시키는 대로 하기로 함

1424 종이에 설계 + 슈더코드
    주석으로 옮겨놓은 조건, 문제 함께 봐가며 고민하며 설계
    변수, 함수, 메인 로직 등 모두 설계함

1434 구현 시작
    후다닥 하지 않고 한 단계 구현하고 문제 상황 생각하고 반복. .
    시험 직전에 광수님한테 배운 함수 만들기 + 단축키가 너무너무 유용했따 ~

1457 구현 완료. 디버깅 시작
    - Index Error
        사람별 목적지 받을 때 평소에 배열 자리 만들어놓고 대입 많이하는데
        설계할 때 append 하려고 빈배열로 뒀다가, 막상 입력받을 땐 대입 또 함;
        하던대로 하자 . .
    - 무한루프?
        원인 알려고 bfs 부분 출력했는데 아무것도 안나오길래
        peopel 출력해봤더니 텅텅 비어있었다. 사람이 배열로 들어올 때 people append 누락;
    - 냅다 코드가 안멈춘다
        while 문이 bfs 2개, 전체로직으로 총 3개 쓰여서 이 중 어디를 의심해야할 지 알기 위해
        print 찍어봄
        visited면 continue 누락 발견해서 해결

    - TypeError
        대입돼야할 값, queue 출력해보며 초기값이 -1, -1이 들어가는 것 발견

        그리고 0번째에 마진으로 넣어둔 -1, -1이 들어가는 것 발견하고 베이스캠프 찾는 로직에
        time>=1 추가

    - 또 나는  TypeError
        이번엔 베이스캠프는 찾아서 편의점 찾기 위한 step에서 난다 !

    - 코드가 안멈추고 이상해서 time 값에 따라 break 걸어놓고 bfs 결과값 출력해서 확인해봄
        원하는 위치가 아니라 이상하게 나온다 !!
        편의점에 도착하는 포인트 찾기 위해 print 찍기
        안찾아져서 gr,gc 출력해봣더니 -1-1 들어옴
        그래서 대입값인 목적 편의점 위치 출력해보니 -1-1 ...
        목적지 찾을 때 사람 번호인 num을 넣어야 하는데 for문 index 넣은 것 찾아서 해결

1511 검증
    printt 함수로 단계별로 문제 그림이랑 완전히 일치하는지 확인해봄

1516 제출 정답


피드백
- 잘한점
    문제 완전히 이해될 때까지 정독
    문제 루틴대로 주석 정리 잘함
    요 며칠 기본 테케에서 각 단계별로 검증 한번만 했어도 잡혔을 에러로 1시간 디버깅한 고생경험으로
    기본 테케에서 문제에서 말한 단계와 완전 일치하는지 검증해봄

- 못한점
    한번 구현할 때 왜이리 빈틈이 많을까 !!!!!!!!!!!!!!!!!!!!!!!!!!!!
    실수 없이 구현하는 법은 안늘어도,, 내 실수 찾는 능력은 조금 는 것 같긴 한데 ,,
    이젠 코드 칠 때 좀 더 정신 차리고 구현하는데에 신경 써보자고 제발제발제발제발 ..

"""

from collections import deque

# n*n 크기의 격자
# 0의 경우에는 빈 공간, 1의 경우에는 베이스캠프
# 각 사람마다 가고 싶은 편의점의 위치는 겹치지 않으며,
# 편의점의 위치와 베이스캠프의 위치도 겹치지 않습니다
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
goal_store = [(-1, -1)] * (M + 1)
DIR = (-1, 0), (0, -1), (0, 1), (1, 0)
for i in range(1, M + 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    goal_store[i] = (x, y)

time = 0
cnt = 0
people = []
finished = [0] * (M + 1)


def oob(r, c):
    return r < 0 or c < 0 or r >= N or c >= N


def move_one(sr, sc, gr, gc):
    #  최단 거리로 움직이는 방법이 여러가지라면
    #  ↑, ←, →, ↓ 의 우선 순위로 움직이게 됩니다.
    # 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여 도달하기까지
    # 거쳐야 하는 칸의 수가 최소가 되는 거리
    q = deque([(sr, sc, 0, None)])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1
    rr, rc = N, N
    while q:
        # print(q)
        cr, cc, rank, move = q.popleft()
        # print("find goal_step")
        # print(cr, cc, rank, move)
        if cr == gr and cc == gc:
            # print("===================!!!!=============")
            # print("편의점 도착 ", move)
            mr, mc = move
            if mr < rr:
                rr, rc = mr, mc
            elif mr == rr and mc < rc:
                rr, rc = mr, mc
            continue
        for di, dj in DIR:
            du = cr + di
            dv = cc + dj

            if oob(du, dv) or arr[du][dv] == -1 or visited[du][dv]:
                continue

            visited[du][dv] = 1
            if rank + 1 == 1:
                q.append((du, dv, rank + 1, (du, dv)))
            else:
                q.append((du, dv, rank + 1, move))
    # print("return rr, rc ", rr, rc)
    return rr, rc


def find_base(t):
    # t번째 사람이 들어갈 베이스캠프 구하기
    # 0의 경우에는 빈 공간, 1의 경우에는 베이스캠프를 의미
    # -1은 못감

    sr, sc = goal_store[t]
    visited = [[0] * N for _ in range(N)]
    q = deque([(sr, sc, 0)])
    visited[sr][sc] = 1

    min_rank = N * N + 1
    rr, rc = N, N

    while q:
        cr, cc, rank = q.popleft()
        if rank < min_rank and arr[cr][cc] == 1:
            min_rank = rank
            rr, rc = cr, cc
            continue
        if rank == min_rank and arr[cr][cc] == 1:
            # 지금 행이 더 작거나 행 같은데 왼쪽인 경우 갱신
            if cr < rr or (rr == cr and cc < rc):
                rr, rc = cr, cc
                continue
        for di, dj in DIR:
            du = cr + di
            dv = cc + dj

            if oob(du, dv) or arr[du][dv] == -1 or visited[du][dv]:
                continue
            visited[du][dv] = 1
            q.append((du, dv, rank + 1))
    return rr, rc


def printt():
    if debug:
        for i in range(N):
            print(arr[i])
        print()

debug= False
while 1:
    time += 1
    if cnt == M :
        printt()
        # print(people)
        # print(finished)
        break
    # m번 사람은 정확히 m 분에 각자의 베이스캠프에서 출발하여
    # 편의점으로 이동하기 시작합니다
    # 사람들은 출발 시간이 되기 전까지 격자 밖에 나와있으며,
    # 사람들이 목표로 하는 편의점은 모두 다릅니다

    arrived_lst = []

    # 이 3가지 행동은 총 1분 동안 진행되며, 정확히 1, 2, 3 순서로 진행되어야 함

    # 격자에 있는 사람들 모두가 본인이 가고 싶은 편의점 방향을 향해서 1 칸 움직입니다.
    # 이동하는 도중 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우 역시 가능함에 유의합니다
    # print(people)
    # print(finished)
    for k in range(len(people)):
        num, cr, cc = people[k]
        # 이미 편의점 도착한 사람 continue
        if finished[num]:
            continue
        gr, gc = goal_store[num]
        nr, nc = move_one(cr, cc, gr, gc)
        people[k] = [num, nr, nc]
        # print(nr, rc)
        if nr == gr and nc == gc:
            arrived_lst.append((gr, gc))
            cnt += 1
            finished[num] = 1
    # 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고,
    # 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 됩니다.
    # 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의합니다.
    # 움직이지 못하게 막기
    for r, c in arrived_lst:
        arr[r][c] = -1

    # 현재 시간이 t분이고 t ≤ m를 만족한다면,
    # t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어갑니다.
    # 여기서 가장 가까이에 있다는 뜻 역시 1에서와 같이 최단거리에 해당하는 곳을 의미합니다.
    # 가장 가까운 베이스캠프가 여러 가지인 경우에는 그 중 행이 작은 베이스캠프,
    # 행이 같다면 열이 작은 베이스 캠프로 들어갑니다.
    # t번 사람이 베이스 캠프로 이동하는 데에는 시간이 전혀 소요되지 않습니다.

    if time >= 1 and time <= M:
        br, bc = find_base(time)
        arr[br][bc] = -1
        people.append((time, br, bc))
    #  해당 턴 격자에 있는 사람들이 모두 이동한 뒤에 해당 칸을 지나갈 수 없어짐에 유의
    #  t번 사람이 편의점을 향해 움직이기 시작했더라도
    #  해당 베이스 캠프는 앞으로 절대 지나갈 수 없음에 유의합니다.


# 총 몇 분 후에 모두 편의점에 도착하는지

print(time-1)
