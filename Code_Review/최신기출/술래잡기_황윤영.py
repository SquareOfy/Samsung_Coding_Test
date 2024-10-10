"""
1차
풀이 시간 : 3시간 +@
시도 횟수 : 4회
실행 시간 : 365 ms
메모리 : 35MB

2차
풀이 시간 : 1시간 풀이 후 철회 + 다음날 처음부터 다시 1시간 8분
시도 횟수 : 2회(다음날 풀이만 카운트....)
실행 시간 275 ms
메모리 32 mb

3차
풀이 시간 : 51분
시도 횟수 : 2회
실행 시간 : 291 ms
메모리 : 32mb



실수 모음
    - 설계 미흡 ( 왜자꾸 놓치지 ) : 3차 때 안함 굿
        - 1차 : 되돌아올 때 방향 반대인거 생각 못하고 방향배열 거꾸로 안함
        - 2차 : 되돌아올때 방향 인덱스 안바꿔줌,, ! 0부터 시작해줘야하는데 한칸 갈 때 또 0...
        => 이런 디테일을 놓친다 ㅠ
    - 인덱스 실수 (M+1까지 봐야하는데 !! ) 3차 때 안함 굿
    - 배열 이름 실수 ! dir 써야 하는데 route배열 이름 써서 실수 *2
    - 로직 누락
        맘 급했니 !!!!!!!!!!!11 왜 잡은 사람 처리 안하니 ! @!@ 

""""""
도망자의 종류
    좌우로만 움직이는 유형  오른쪽을 보고 시작
    상하로만 움직이는 유형 아래쪽을 보고 시작
    도망자는 중앙에서 시작하지는 않습니다.

h개의 나무  도망자와 초기에 겹쳐져 주어지는 것 가능


도망자가 1턴 그리고 이어서 술래가 1턴 진행하는 것을 총 k번 반복

    1. 도망자 움직임
        현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
        두 사람간의 거리는 |x1 - x2| + |y1 - y2|로 정의

        현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
             방향을 반대로 틀어줍니다.
             바라보고 있는 방향으로 1칸 움직인다 했을 때
             해당 위치에 술래가 없다면 1칸 앞으로 이동
             있으면 스테이

        현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나지 않는 경우
            움직이려는 칸에 술래가 있는 경우라면 움직이지 않습니다.
            움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동합니다.
            나무가 있어도 괜찮습니다.
    2. 술래 움직임
        달팽이 모양으로 움직입니다. ( 상 우 하 좌 )
         끝에 도달하게 되면 다시 거꾸로 중심으로 이동
        중심에 오게 되면 처음처럼 위 방향으로 시작하여 시계뱡향으로 도는 것을 k턴에 걸쳐 반복
         위치가 만약 이동방향이 틀어지는 지점이라면, 방향을 바로 틀어줍니다.

        2-2 도망자 잡기
             술래의 시야는 현재 바라보고 있는 방향을 기준으로 현재 칸을 포함하여 총 3칸입니다
             나무가 놓여 있는 칸이라면, 해당 칸에 있는 도망자는 나무에 가려져 보이지 않게 됩니다.
              t x 현재 턴에서 잡힌 도망자의 수만큼의 점수
"""
"""======================== 3차 코드 =============================="""
def change(i):
    return int(i)-1


def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def cal_dist(i, j, x, y):
    return abs(i-x) + abs(j-y)

def set_route_dir():
    global back_Route_lst, back_Dir_lst
    r, c = N//2, N//2
    go_Route_lst.append((r,c))
    l = 1
    cnt =0
    while 1:
        for dk in range(4):
            di, dj = DIR[dk]
            go_Dir_lst[-1]= dk
            for lk in range(l):
                r+=di
                c+=dj
                go_Dir_lst.append(dk)
                back_Dir_lst.append((dk+2)%4)
                go_Route_lst.append((r,c))
                if r==0 and c==0:
                    go_Dir_lst[-1]=2
                    back_Dir_lst = back_Dir_lst[::-1]
                    back_Dir_lst[-1] = 0
                    back_Route_lst = go_Route_lst[::-1]
                    return
            cnt +=1
            if cnt==2:
                cnt=0
                l+=1



N, M, H, K = map(int, input().split())

runner_info = [-1]
runner_arr = [[[] for _ in range(N)] for _ in range(N)]
tree_arr = [[0]*N for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

go_Route_lst = []
back_Route_lst = []

go_Dir_lst = [0]
back_Dir_lst = [2]

for m in range(M):
    x, y, d = map(change, input().split())
    d = 1 if d==0 else 2
    runner_info.append((x, y, d))
    runner_arr[x][y].append(m)

set_route_dir()
s_idx = 0
go_flag = 1
answer = 0
for h in range(H):
    x, y = map(change, input().split())
    tree_arr[x][y] = 1

for k in range(1, K+1):

    sr, sc = go_Route_lst[s_idx] if go_flag else back_Route_lst[s_idx]
    for m in range(1, M+1):
        if runner_info[m]==-1:
            continue
        Rx, Ry, Rd = runner_info[m]
        dist = cal_dist(sr, sc, Rx, Ry)
        if dist>3: continue

        Rdi, Rdj = DIR[Rd]
        nRx, nRy = Rx+Rdi, Ry+Rdj
        if oob(nRx, nRy):
            Rd = (Rd+2)%4
            nRx -= Rdi*2
            nRy -= Rdj*2
        if sr == nRx and sc == nRy:
            runner_info[m] = (Rx, Ry, Rd)
        else:
            runner_info[m] = (nRx, nRy, Rd)

    runner_arr =[[[] for _ in range(N)] for _ in range(N)]
    for m in range(1, M+1):
        if runner_info[m] == -1:
            continue
        x, y, d = runner_info[m]
        runner_arr[x][y].append(m)

    s_idx +=1
    if s_idx == N*N -1:
        go_flag = not go_flag
        s_idx = 0

    sr, sc = go_Route_lst[s_idx] if go_flag else back_Route_lst[s_idx]
    sd = go_Dir_lst[s_idx] if go_flag else back_Dir_lst[s_idx]
    sdi, sdj = DIR[sd]
    for t in range(3):
        nSr, nSc = sr+sdi*t, sc+sdj*t
        if oob(nSr, nSc): break
        if tree_arr[nSr][nSc]: continue
        answer += k*len(runner_arr[nSr][nSc])
        for m in runner_arr[nSr][nSc]:
            runner_info[m] = -1
print(answer)

"""
================= 2차 코드 리뷰 ==================
1008 문제읽기..
1019 설계
1026 구현 
1033 잠깐 스탑 ======

1051 다시시작
    돌아올 때 dir 배열이 어려워서,, 중간 테스트함

1113 구현완료 후 답 달라서 프린트 해봄
    K+1 안한 것 발견. M+1 안한 것 발견
    수정 후 테케 맞아서 제출했으나 에러 
    go_flag false일 때 back 배열 dir아니고 route쓴 것 발견 
    고쳤으나 답이 틀림
    예전에도 큰 테케에서 이렇게 틀렸어서 아마 되돌아올 때의 문제라고 생각
    하지만 route, dir 함수 다 맞아서 뭐지 했다 .
    코드 뜯어보기 
    되돌아올 때 모듈하고 끝이 아니라 0으로 index를 만들어줘야한다고 깨달음
    

"""
"""
n * n 크기의 격자에서 진행
술래는 처음 정중앙

술래잡기 게임에는 m명의 도망자 도망자는 중앙에서 시작하지는 않습니다.
좌우로만 움직이는 유형 항상 오른쪽을 보고 시작
상하로만 움직이는 유형 항상 아래쪽을 보고 시작

술래잡기 게임에는 h개의 나무
도망자와 초기에 겹쳐져 주어지는 것 역시 가능

도망자가 1턴 그리고 이어서 술래가 1턴 진행하는 것을 총 k번 반복

    도망자 이동
        현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
        두 사람간의 거리는 |x1 - x2| + |y1 - y2|로 정의

        격자를 벗어나지 않는 경우
            움직이려는 칸에 술래가 있는 경우라면 움직이지 않습니다.
            움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동
            나무가 있어도 괜찮습니다.
        격자를 벗어나는 경우
            방향을 반대로 틀어줍니다.
            이후 바라보고 있는 방향으로 1칸 움직인다 했을 때
            해당 위치에 술래가 없다면 1칸 앞으로 이동


    술래 이동
        처음 위 방향으로 시작하여 달팽이 모양으로 움직입니다.
         끝에 도달하게 되면 다시 거꾸로 중심으로 이동
         중심에 오게 되면 처음처럼 위 방향으로 시작
         치가 만약 이동방향이 틀어지는 지점이라면, 방향을 바로 틀어줍니다.
    술래는 턴을 넘기기 전에 시야 내에 있는 도망자를 잡게 됩니다
    술래의 시야는 현재 바라보고 있는 방향을 기준으로
      현재 칸을 포함하여 총 3칸
    만약 나무가 놓여 있는 칸이라면,
    해당 칸에 있는 도망자는 나무에 가려져 보이지 않게 됩니다.

    잡힌 도망자는 사라지게 되고, 술래는 현재 턴을 t번째 턴이라고 했을 때
     t x 현재 턴에서 잡힌 도망자의 수만큼의 점수를 얻게 됩니다
"""


def change(i):
    return int(i) - 1


def get_sul_loc():
    if go_flag:
        sr, sc = go_route_lst[s_idx]
        sd = go_dir_lst[s_idx]
    else:
        sr, sc = back_route_lst[s_idx]
        sd = back_dir_lst[s_idx]
    return sr, sc, sd


def set_route_lst():
    global back_route_lst, back_dir_lst
    r, c = N // 2, N // 2
    go_route_lst.append((r, c))
    back_route_lst.append((r, c))
    go_dir_lst.append(0)
    back_dir_lst.append(0)
    l = 1
    cnt = 0
    while 1:
        for i in range(4):
            di, dj = DIR[i]
            go_dir_lst[-1] = i
            back_dir_lst[-1] = (i + 2) % 4
            for k in range(l):
                r += di
                c += dj
                go_route_lst.append((r, c))

                go_dir_lst.append(i)
                # back_dir_lst.append((i+2)%4)

                if r == 0 and c == 0:
                    go_dir_lst[0] = 0
                    go_dir_lst[-1] = 2
                    back_route_lst = go_route_lst[::-1]
                    return
            cnt += 1
            if cnt == 2:
                l += 1
                cnt = 0


def calculate_d(x, y, r, c):
    return abs(x - r) + abs(y - c)


def oob(i, j):
    return i >= N or j >= N or i < 0 or j < 0

def printa(string, arr):
    print(f"================{string}===================")
    for z in range(N):
        print(arr[z])
    print("============================================")
    print()

N, M, H, K = map(int, input().split())
runner_lst = [-1]
runner_arr = [[[] for _ in range(N)] for _ in range(N)]
tree_arr = [[0] * N for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

for m in range(1, M + 1):
    x, y, d = map(change, input().split())
    d = 1 if d == 0 else 2  # 좌우로 움직이면(d==0) 오른쪽보기 아니면 아래쪽
    runner_arr[x][y].append(m)
    runner_lst.append((x, y, d))

for h in range(H):
    x, y = map(change, input().split())
    tree_arr[x][y] = 1

go_flag = True
go_route_lst = []
back_route_lst = []
go_dir_lst = []
back_dir_lst = []

set_route_lst()
back_dir_lst = [(i + 2) % 4 for i in go_dir_lst[N * N - 2::-1]] + [0]

# print(go_route_lst)
# print(go_dir_lst)
# print(len(go_dir_lst))
#
# print()
# print(back_route_lst)
# print(back_dir_lst)
s_idx = 0
answer = 0
for k in range(1, K+1):
    # print(f"===================turn : {k} ===================")

    sr, sc, sd = get_sul_loc()
    # 도망자 이동시키기
    for m in range(1, M + 1):
        if runner_lst[m] == -1: continue
        x, y, d = runner_lst[m]
        dist = calculate_d(x, y, sr, sc)
        # print("이동가능한가? dist : ", dist)
        if dist > 3:
            continue

        di, dj = DIR[d]
        du, dv = x + di, y + dj
        if oob(du, dv):
            d = (d + 2) % 4
            du -= di * 2
            dv -= dj * 2
        if du == sr and dv == sc:
            runner_lst[m] = (x, y, d)
        else:
            runner_lst[m] = (du, dv, d)

    runner_arr = [[[] for _ in range(N)] for _ in range(N)]
    for m in range(1, M+1):
        if runner_lst[m] == -1:
            continue
        x, y, d = runner_lst[m]
        runner_arr[x][y].append(m)
    # printa("도망자 이동 후", runner_arr)
    # print(runner_lst)
    # print()

    s_idx += 1
    s_idx %= N * N
    sr, sc, sd = get_sul_loc()
    sdi, sdj = DIR[sd]

    if s_idx==N*N-1:
        s_idx = 0
        go_flag = not go_flag
    # print("술래 현 위치 ", sr, sc, sdi, sdj)
    for t in range(3):
        sight_r, sight_c = sr + sdi * t, sc + sdj * t
        if oob(sight_r, sight_c):
            break
        if tree_arr[sight_r][sight_c]:
            continue
        # print("잡은 애들 : ", runner_arr[sight_r][sight_c])
        if runner_arr[sight_r][sight_c]:
            answer += k*len(runner_arr[sight_r][sight_c])
            for runner in runner_arr[sight_r][sight_c]:
                runner_lst[runner] = -1

print(answer)

"""
코드 리뷰
풀이 시간 : 3시간 +@
실행 시간 : 365 ms
메모리 : 35MB

1410 문제읽기 시작 + 함께 설계 (13분)
    문제 조건 주석에 적어가며 읽었음
    필요하다면 복사도 함
    아래는 구현 어떻게 할 지 아이디어에 대한 주석 추가로 달았음.

1423 구현시작
    달팽이부터 구현 => 중간 프린트로 확인함
        추후 여기가 문제였다. 달팽이로 구현한 부분이 중간 프린트로 확인하며,
        그 때 작성한 방향배열까지 의심하지 않음....

1501 제출 - 런타임에러(51분)
    처음엔 런타임에러날 구석이 없다고 생각했다가 번뜩 달팽이라인을 왔다갔다할 때가 바로 의심 됐다
    고치니 런타임에러는 해결 됏지만 TC3에서 문제

1503 본격적인 TC3과의 전쟁 시작
    초기에만 도망자의 자리가 겹치지 않고 이동하다보면 겹치는데, 이걸 고려안하고 한 자리에
    한 도망자만 덮어씌우는 실수를 했었다. 이걸 대왕 큰 TC3을 보고 깨닫고 고침 (도망자가 왤케 많지..하다가)
    테케가 너무 커서 토론방을 찾았지만, 저 테케도 손으로 따라가긴 꽤나 규모가 컸다...
    의미 없이 계속 손테케 따라가다 헷갈려하기를 반복함..
    내가 틀렸을거야 .. 하고 문제를 다시 살펴보다 도망자와 거리가 3이하인 경우 ! 이 부분의 말이 모호함을 느껴
    내가 잘못이해하진 않았나 거듭확인함
    확인했던 달팽이도 의심하기 시작했지만, 되돌아오는 방향을 고려하지 않았다. (돌아오는 길은 맞지만 보는 방향이 틀림)

    코드 뜯어봐다가 벽 마주쳐서 방향 바꾸는 과정에서 모듈을 4가 아닌 2로 나눈 오타도 발견 .. (정신 차려잇)


시간 끝나버림 .................................... 진짜 끝의 한시간이 너무 무의미했다...

1850 다시 디버깅
    코드 훑어보기 ...
    아무리 생각해도 전반적인 로직은 맞단 말야
    그렇담 안봤던 달팽이 다시보기
    그러다 되돌아올 때 방향 반대로 안바꿔준 것 깨닫고 +2 하고 모듈했지만 답이 안나온다
    끝을 찍고 돌아오는 부분이 문제일거라 생각해서 그냥 돌아올 때 술래가 바라보는 방향을 저장한 배열
     하나 더 새로 만들었더니 됐다 ..

1905 정답처리





- 실패의 원인?
    부족한 설계
    부족한 설계였을 때 디버깅으로 이를 잡지 못했다 => 테케가 클 때 대처 미흡

    도망자 위치나 dist 막 프린트해서 도망친 후 배열이랑 비교하며 확인하긴 했는데,
    테케가 워낙 헷갈려서 명확하게 문제를 파악하는 듯한 느낌의 디버깅이 아니었다.

    거리가 3인 부분의 말이 모호한 것 같아 dist를 구해서 비교하는 부분의 기준점과
    로직 위치만 이리저리 바꿔가기만 할 뿐, 다른 대처를 어떻게 해야할지 몰라 우왕좌왕했고,
    틀린 부분의 빈틈을 끝까지 알아채지 못함.....................

- 어떻게 했으면 좀 나았을까?
    다시 회고해보니 테케가 규모가 클 수 밖에 없었다.
    내가 틀린 부분에서 문제의 원인이 크게 두가지가 있을 수 있었는데,
        첫째, 거리가 3초과인 경우가 생겨서 도망자가 도망가지 않는 경우
        둘째, 끝까지 달팽이 모양으로 갔다가 다시 되돌아오게 되는 경우
    이 두 가지는 어느 정도 테케 규모가 커야 가능한 경우였기 때문이다.

    그렇다면, 손으로 따라가기 어려웠다면, 테케들의 공통점을 찾아보려하면 좀 더 빨리 찾을 수 있었을까??
    K의 값이 모두 충분히 크다는 것, 거리가 3 초과인 값이 있어서 라는 공통점을 찾고 그 부분을 집중 디버깅했다면?

    또한, 이번 문제에서 유독 프린트 디버깅을 해놓고 진짜 큰 범위였을 때 술래가 맞게 이동하는지
    꼼꼼하게 보지 않았던 것 같다.

    범위가 크면 큰 범위로 갔을 때 틀린다는 뜻이므로 좀 더 멀리까지 디버깅으로 내다보자 ..

- 고민되는 점
    테케가 클 때 너무 난감하고, 손으로 따라가기 어려운 경우 감당이 안된다 ........
    게다가 이걸로 당황하니까 무의미한 디버깅을 좀 한듯 (확실하지 않은데 값이나 순서만 바꿔보는 행위)
    위에서 말한 공통점을 찾아내면 그나마 다행이지만 그마저 찾지 못했을 때 ... 어쩌지 ...

- 개선할 점
    가끔 이렇게 한번씩 넘어지는 문제에서는 설계 미흡이 정말 많다.
    실수를 자주하는 편인데도 문제내용이 애매하게 머리에 남은 상태에서 시작하면 꼭 이런다.

    주석으로 구현 공간을 전반적으로 정리할 수 있을 만큼! 문제와 풀이과정의 구조가 이해될 때
    구현을 시작하는 루틴을 꼭 지키자.

"""

"""
==================조건 정리 및 구상====================
1. 도망자 움직이기
    현재 바라보고 있는 방향으로 1칸 움직일 때
        격자를 벗어나지 않는 경우
            술래가 있는 경우라면 움직이지 않습니다.
            술래 없다면 해당 칸으로 이동.  나무가 있어도 괜찮

        격자를 벗어나는 경우
            방향을 반대로 틀어주기.
            바라보고 있는 방향으로 1칸 움직인다 했을 때
            해당 위치에 술래가 없다면 1칸 앞으로 이동합니다.

2. 술래 움직이기
    가운데에서 시작해서 상 우 하 좌 순으로 달팽이 모양으로 움직임
    도달하면 반대로 움직여서 중심으로 오기

    ************주의 !!!!!!!!!!!!!!!!!!!!!111
    한칸 이동 후 방향을 트는 곳이라면 방향을 바로 틀어준다 !!!!!!! !!
    ********************************************8
나무의 역할이 뭐지 ?
만약 나무가 놓여 있는 칸이라면, 해당 칸에 있는 도망자는 나무에 가려져 보이지 않게 됩니다.
술래가 보고 있는 방향을 끝까지 보고 나무 있는 칸의 도망자는 살아남고 아니면 잡힌다 !

점수
    t번째 턴일 때, t*잡힌 도망자 수


==============구현 설계=================
1. 도망자 움직이기
    도망자 위치 배열에 담아두기 ( arr 배열에는 도망자 번호로 넣어두기!!!)
    도망자 배열 탐색하며 다음 위치 새 배열에 넣기 (술래와의 거리 3이하인지 확인하고 움직이기, 아니면 그대로)
        oob 활용
        oob 아닐 때 술래 위치 idx 로 기억해둔 것 활용

2. 술래 이동
    달팽이 모양(술래 위치 순서) 배열에 담아두기
    그 때의 방향 배열 만들어 두기

    술래 현 위치가 끝점이면 위치 index 1 빼기
    아니면 index +1

    index 변경 시킨 후 방향도 방향 배열의 값으로 갱신해두기

    그리고 그 방향에서 사람 있나 쭈우우욱 보고 잡기 + 점수 더하기
"""
def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def get_distance(i, j, x, y):
    return abs(i-x)+abs(j-y)

#인덱스 1부터 시작하니까 꼭 1 빼기 !!!!!!!!!!!!!!!!!!!!!!!!!!!
N, M, H, K = map(int, input().split())

arr = [[[] for _ in range(N)] for _ in range(N)]
tree = [[0]*N for _ in range(N)]
runner = []
route = []
d_by_route = []
d_by_route2 = []
dir = (-1, 0),(0, 1), (1, 0), (0, -1) #상 / 우 / 하 / 좌 (1, 2그대로 유지! )
answer = 0

#도망자 입력 받기
for i in range(M):
    x, y, d = map(int, input().split())
    runner.append([x-1, y-1, d])
    arr[x-1][y-1].append(i)

for j in range(H):
    x, y = map(int, input().split())
    tree[x-1][y-1] = 1


#술래 이동 route 배열 만들어 놓기
r = N//2
c = N//2
l = 1
cnt = 0
route.append((r,c))
d_by_route.append(0)
d_by_route2.append(0)
d = 0
while 1:
    di, dj = dir[d]
    for k in range(l):
        r += di
        c += dj
        route.append((r, c))
        d_by_route.append(d)
        d_by_route2.append((d+2)%4)

        if r==0 and c==0:
            break

    cnt += 1
    if cnt ==2:
        l+=1
        cnt = 0
    d += 1
    d %= 4
    d_by_route[-1] = d
    if r==0 and c==0:
        d_by_route[-1] = 2
        d_by_route2[-1] = 2
        break
######################달팽이 확인 완
# print(route)
# print(d_by_route)
####################################33

# 1. 도망자 움직이기
#     도망자 배열 탐색하며 다음 위치 새 배열에 넣기 (술래와의 거리 3이하인지 확인하고 움직이기, 아니면 그대로)
#         oob 활용
#         oob 아닐 때 술래 위치 idx 로 기억해둔 것 활용
#         격자를 벗어나지 않는 경우
#             술래가 있는 경우라면 움직이지 않습니다.
#             술래 없다면 해당 칸으로 이동.  나무가 있어도 괜찮
#
#         격자를 벗어나는 경우
#             방향을 반대로 틀어주기.
#             바라보고 있는 방향으로 1칸 움직인다 했을 때
#             해당 위치에 술래가 없다면 1칸 앞으로 이동합니다.
#현재 술래 정보
idx = 0
r = 1

for k in range(1, K+1):

    cr, cc = route[idx]
    d = d_by_route[idx]

    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    new_runner = []
    runner_idx = 0

    for i,j,run_d in runner:
        if i== -1 and j==-1:
            continue

        # 움직임 가능성 체크
        dist = get_distance(i, j, cr, cc)
        if dist > 3:
            new_runner.append([i, j, run_d])
            new_arr[i][j].append(runner_idx)
            runner_idx += 1
            continue
        di, dj = dir[run_d]
        du = i+di
        dv = j+dj
        if oob(du, dv): #
            run_d = (run_d+2)%4
            du -= di*2
            dv -= dj*2

        #술래가 있으면 ...
        if du == cr and dv == cc:
            new_runner.append([i, j, run_d])
            new_arr[i][j].append(runner_idx)
            runner_idx+= 1
            continue

        new_arr[du][dv].append(runner_idx)
        runner_idx+=1
        new_runner.append([du, dv, run_d])

    #옮긴 도망자 원본 배열에 다시 반여하기
    for i in range(N):
        for j in range(N):
            arr[i][j] = new_arr[i][j][:]
    runner = new_runner[:]
    # print("==========도망친 후 ===================")
    # for i in range(N):
    #     print(arr[i])
    # print()
    #술래 옮기기
    idx += r
    #술래의 옮긴 위치와 방향
    cr, cc = route[idx]
    if r==-1:
        di, dj = dir[d_by_route2[idx]]
    else:
        di, dj = dir[d_by_route[idx]]

    if idx == N*N -1 and r==1:
        r*= -1
    elif idx == 0 and r==-1:
        r*= -1
    catch = 0

    for t in range(3):
        du = cr + di*t
        dv = cc + dj*t

        if oob(du, dv):
            break
        if tree[du][dv]:
            continue
        if arr[du][dv]:
            catch += len(arr[du][dv])
            for u in arr[du][dv]:
                runner[u] = [-1, -1, 0]
            arr[du][dv] = []

    answer += k*catch
print(answer)
