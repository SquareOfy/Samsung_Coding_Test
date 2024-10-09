"""
1차
풀이 시간 : 2시간 51분
시도 횟수 : 2회
실행 시간 : 276ms
메모리 : 28mb

2차
풀이 시간 : 1시간 24분
시도 횟수 : 1회 ~~~~~~~~~~~~~~ 원트 ~~ 오예 ~~
실행 시간 : 311ms
메모리 : 27mb

- 실수 모음
    - 변수명 헷갈리지마 !
    - 문제 조건 누락
         - 한턴 끝날때마다 안죽은 산타 더해주는거랑 산타 안움직일 수 있는거!
    - 이동 처리 배열에 반영하는 것 누락
        산타 이동 배열 반영 누락
    - 배열 초기값 주의!! 처음에 기절한 애들 0 아닌거 조건 추가 안함!  로직 연관지어 생각하기!!!!
    - 종료조건 누락
"""
"""
 좌상단은 (1,1)
거리 : (r1-r2)**2 + (c1-c2)**2
루돌프가 한 번 움직인 뒤,
1번 산타부터 P번 산타까지 순서대로 움직이게 됩니다

1. 루돌프 이동
    루돌프는 게임에서 탈락하지 않은 산타 중  가장 가까운 산타를 향해 1칸 돌진
    r 좌표가 큰 산타를 향해 돌진
    c 좌표가 큰 산타를 향해 돌진
    루돌프는 상하좌우, 대각선을 포함한 인접한 8방향 중 하나로 돌진
    산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생
    루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다.
    산타는 루돌프가 이동해온 방향으로 C 칸 만큼 밀려나게 됩니다.
    밀려나는 것은 이동하는 도중에 충돌이 일어나지는 않고  원하는 위치에 도달
    밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락
    밀려난 칸에 다른 산타가 있는 경우 상호작용이 발생
        충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 됩니다.
          그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복
          게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락
2. 산타
    기절해있거나 격자 밖으로 빠져나가 게임에서 탈락한 산타들은 움직일 수 없습니다.
    상하좌우로 인접한 4방향 중 한 곳으로 움직일 수 있습니다.
    루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
    가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위에 맞춰 움직입니다.
    움직일 수 있는 칸이 없다면 산타는 움직이지 않습니다.


"""
from collections import deque
def change(i):
    return int(i)-1

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def get_dist(r1, c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2

#충돌함수
def crush(step, di, dj, m):
    r, c = santa_info[m]
    nr, nc = r+di*step, c+dj*step
    score_lst[m] += step
    if oob(nr, nc):
        die_lst[m] = 1
        santa_arr[r][c] = 0
        return
    if santa_arr[nr][nc]:
        interact(santa_arr[nr][nc], di, dj)

    santa_arr[nr][nc] = m
    santa_arr[r][c] = 0
    santa_info[m]= (nr, nc)

#연쇄작용 함수
def interact(m, di, dj):
    r, c = santa_info[m]
    nr, nc = r+di, c+dj
    if oob(nr, nc):
        die_lst[m] = 1
        return
    if santa_arr[nr][nc]:
        interact(santa_arr[nr][nc], di, dj)
    santa_arr[nr][nc] = m
    santa_arr[r][c] = 0
    santa_info[m] = (nr, nc)


#가장 가까운 산타에게 가기 위한 방향 반환
def find_ru_dir():
    mn_dist = N*N
    santa_r, santa_c = -1, -1
    for m in range(1, P+1):
        if die_lst[m]: continue
        r, c = santa_info[m]
        dist = get_dist(rr, rc, r, c)
        if dist < mn_dist:
            mn_dist = dist
            santa_r, santa_c = r, c
        elif dist == mn_dist:
            if (santa_r, santa_c) < (r, c):
                santa_r, santa_c = r, c

    mn = get_dist(rr, rc, santa_r, santa_c)
    rdi, rdj = -1, -1
    #산타 위치 정해졌으므로 8방 탐색하며 이동할 곳 찾기
    for di, dj in ru_dir:
        nr, nc = rr+di, rc+dj
        if oob(nr, nc): continue
        dist = get_dist(nr, nc, santa_r, santa_c)
        if dist<mn:
            mn = dist
            rdi, rdj = di, dj
    return rdi, rdj


def find_santa_move(p):
    r, c = santa_info[p]
    mn = get_dist(r, c, rr, rc)
    result_d = 4

    for d in range(4):
        di, dj = santa_dir[d]
        du, dv = r + di, c + dj
        if oob(du, dv): continue
        if santa_arr[du][dv]: continue

        dist = get_dist(du, dv, rr, rc)
        if dist >= mn:
            continue
        mn = dist
        result_d = d
    return result_d


def move_santa():
    for p in range(1, P + 1):
        if (sleep_lst[p] != 0 and sleep_lst[p] in (turn, turn - 1)) or die_lst[p]: continue
        # print(f"===================={p}번 santa  이동 =========================")
        sd = find_santa_move(p)
        if sd == 4:
            continue
        sdi, sdj = santa_dir[sd]
        # print("sdi, sdj : ", sdi, sdj)

        scr, scc = santa_info[p]
        snr, snc = scr + sdi, scc + sdj
        santa_info[p] = (snr, snc)
        santa_arr[snr][snc] = p
        santa_arr[scr][scc] = 0
        # 루돌프 만나면
        if snr == rr and snc == rc:
            sleep_lst[p] = turn
            crush(D, -sdi, -sdj, p)
            if sum(die_lst)==P:
                return False
    return True


def printa(string, arr):
    print(f"=================={string}====================")
    for j in range(len(arr)):
        print(arr[j])
    print("==============================================")
    print()


#루돌프에게 가기 위한 방향 반환

N, M, P, C, D = map(int, input().split())
santa_dir = (-1, 0), (0, 1), (1, 0), (0, -1), (0, 0)
ru_dir = (-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)
score_lst = [0]*(P+1)
sleep_lst = [0]*(P+1)
die_lst = [0]*(P+1)
santa_info = [[] for _ in range(P+1)]
santa_arr = [[0]*N for _ in range(N)]
rr, rc = map(change, input().split())
for p in range(P):
    num, sr, sc = map(change, input().split())
    num += 1
    santa_arr[sr][sc] = num
    santa_info[num] = (sr, sc)




for turn in range(1, M+1):
    # 루돌프 이동하기
    rdi, rdj = find_ru_dir()
    rr += rdi
    rc += rdj
    # print("===========루돌프 이동 ==============")
    # print(rr, rc)
    #이동한 곳에 산타 있나 확인
    if santa_arr[rr][rc]:
        #충돌했으면 기절
        sleep_lst[santa_arr[rr][rc]] = turn
        crush(C, rdi, rdj, santa_arr[rr][rc])
        if sum(die_lst)==P:
            break

    # 산타 이동하기
    result = move_santa()
    if not result:
        break
    # printa("산타이동", santa_arr)
    # print('산타 죽은거 정보 ', die_lst)
    # print("산타 점수 정보 : ", score_lst[1:])

    for p in range(1, P+1):
        if die_lst[p]: continue
        score_lst[p]+=1

    # print("한턴 끝나고 !! ", score_lst[1:])

print(*score_lst[1:])

"""
====================== 1차 코드리뷰 =============================
풀이 시간 : 2시간 51분
실행 시간 : 276ms
메모리 : 28mb

1400 문제 정독 + 주석정리
    산타와 루돌프가 충돌하는게 시간 순이 아니게 나와서 각각 필요한 부분에 주석 가져다 붙임

1416 설계하며 구현
    산타, 루돌프 어디에 어떻게 저장하고 관리할 것인가.
    언제 업데이트할 것인가  중요하게 생각 (자꾸 움직이고 부딪히고 난리치기 때문)

    루틴 제대로 못지킴 이슈 .. 앞에 문제 못푼게 영향을 준듯. 조급했다

    구현하면서 워낙 관리할 변수가 많아 자꾸 변수가 겹쳐서(루돌프 충돌 후, 산타 충돌 후 등) 애먹음
    우선순위 정하는 거 좀 헷갈려하는데 거리 순으로 우선순위 매번 정해야해서 어질어질했음
1508 구현완 디버깅 시작
    - 루돌프가 선택한 산타 출력해보고 비교
        dist 값 갱신 안해서 못잡는 것 확인하고 고침
    - 코드 순차적으로 훑어가며 로직 잘못된 것 있는지 확인.
        기절한 산타 변수 초기값이 겹치겠다는 것 발견
        고침
    - 기절한 산타 안 움직일 때 앞에 루돌프 충돌에서 기절한 경우 고려 안함 발견=> 고침
    - 인덱스 1 빼는 함수 적용한 것 때문에 산타 번호 0부터 시작되는 이슈 발견. 1더해줌
    - 답이 안나오길래 보다가 산타 뎐쇄작용 후 원래 자리 안비워준 것 발견
    - 산타 이동, 루돌프 이동, 충돌 다 확인해봐도 이상하지 않다. .
    - 변수 다양해서 변수 다 맞게 썼나 확인
    - 연쇄작용 똑바로 안되는 이슈 확인
    - 우선순위 부분 점검(루돌프가 산타 잘 찾나1?)
    - 고치고 하다보니 딱 한놈이 점수 1 더 받는다 .이유가 뭐냐! 너 왜 점수 더받냐 !
        산타 재우는 순서 바꿔서 해결

    정답....

    피드백
    - 설계의 중요성
        앞에서 조급했다고 이러기냐? 루틴 지켜라 . 넌 실수를 많이 하는사람. 그래서 설계 필수임
        이렇게 개체 많아서 변수명 지저분해질 것 같은 문제는 함수화로 해결하자
        그리고 설계 때 변수명도 좀 정해서 코드짜면서 헷갈리지 말자.
        특히 화면 작아서 코드를 전반적으로 길게 못보니까 더 실수가 많다. 종이 설계를 활용하자. .


"""

def change_idx(i):
    return int(i)-1

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def find_nearest_santa():
    lst = []
    mn = N ** 2
    reuslt_r, result_c = -1, -1
    # print(die_santa)
    # print(santa)
    for p in range(1, P + 1):
        if die_santa[p]==1: continue  # 이미 죽어버림
        r, c = santa[p]
        dist = (rr-r)**2 + (rc-c)**2
        if dist<mn:
            mn = dist
            lst = [(r, c)]
            # reuslt_r, result_c = r, c
        elif dist ==mn :
            lst.append((r,c))
            # reuslt_r, result_c = r, c
    lst.sort(reverse=True)
    return lst[0]

def calculate_dist(i, j, y, x):
    return (i-y)**2 + (j-x)**2

def find_move_d(rr, rc, r, c):
    move_d = -1

    mn = calculate_dist(rr, rc, r, c)
    # (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
    for i in range(8):
        di, dj = dir_eight[i]
        nrr, nrc = rr+di, rc+dj

        if oob(nrr, nrc):
            continue
        dist = calculate_dist(nrr, nrc, r, c)
        # print("d : ", i, "일 때 dist : ", dist)
        if mn>dist:
            move_d = i
            mn=dist
    return move_d


def push_santa(r, c, di, dj, num):
    global cnt
    # 밀려난 칸에 다른 산타가 있는 경우 상호작용
    # 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 됩니다.
    # 연쇄작업
    nr = r+di #밀리는 위치
    nc = c+dj
    if oob(nr, nc): #밖이면 죽어
        die_santa[num] = 1
        cnt+=1
        santa_arr[r][c] = 0  #원래위치도 0으로 만들어주기
        return
    if santa_arr[nr][nc]: #다음 위치에 산타 있으면
        push_santa(nr, nc, di, dj, santa_arr[nr][nc]) #얘도 밀어주고
    santa_arr[nr][nc] = num #자리 차지
    santa[num] = [nr, nc] #정보업데이트



def crush(r, c, di, dj, step):
    global cnt
    num = santa_arr[r][c]


    score[num] += step #C또는 D
    du, dv = r + di * step, c + dj * step #밀려나는 자리

    # 이동하는 도중에 충돌이 일어나지는 않고 밀려난 위치가 게임판 밖이라면
    # 산타는 게임에서 탈락
    if oob(du, dv): #범위 넘어가면 죽음
        santa_arr[r][c] = 0 #원래 자리 비워주고 죽기
        die_santa[num] = 1
        cnt+=1
        return


    if santa_arr[du][dv]: #연쇄작용
        # print("=============연쇄작용==================")
        push_santa(du, dv, di, dj, santa_arr[du][dv]) #그방향으로 쭉쭉 밀어
    santa_arr[du][dv] = santa_arr[r][c] #그 자리 차지하고
    santa_arr[r][c] = 0
    santa[num] = [du, dv] #정보 업데이트



#  N×N 크기의 격자 좌상단은 (1,1)
N, M, P, C, D = map(int, input().split())
rr, rc = map(change_idx, input().split())
santa_arr = [[0]*N for _ in range(N)]
santa = [[-1, -1] for _ in range(P+1)]
for i in range(P):
    num, r, c = map(change_idx, input().split())
    santa_arr[r][c] = num+1 #santa 번호 함수로 1빼줬으니까 다시 더해줌
    santa[num+1][0] = r
    santa[num+1][1] = c

sleep_santa = [-1]*(P+1)
score = [0]*(P+1)
die_santa = [0]*(P+1)
cnt = 0
dir_eight = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
# 게임은 총 M 개의 턴에 걸쳐 진행
# 거리 (r-r2)**2 + (c-c2)**2


for k in range(1, M+1):
    r, c = find_nearest_santa()
    move_d = find_move_d(rr, rc, r, c)
    di, dj = dir_eight[move_d]

    rr, rc = rr+di, rc+dj

    if santa_arr[rr][rc]:
        sleep_santa[santa_arr[rr][rc]] = k
        crush(rr, rc, di, dj, C) #상호작용 이 안에서 호출

    if cnt == P:
        break

    for p in range(1, P+1):
        # print("=======", p, "번 산타 이동해보자")
        # 기절해있거나(k-1이면) 격자 밖으로 빠져나가 게임에서 탈락한 산타들은 움직일 수 없습니다.
        if die_santa[p]==1 or sleep_santa[p] in (k, k-1):
            # print("죽거나 기절")
            continue
        # 산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
        # 가장 가까워질 수 있는 방향이 여러 개라면, 상우하좌 우선순위
        r, c= santa[p]
        # print("r, c : ", r, c)


        min_dist = calculate_dist(rr, rc, r, c)
        move_d = (-1, -1)
        du, dv = r, c


        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            nr, nc = r+di, c+dj
            if oob(nr, nc) or santa_arr[nr][nc]:
                # print("범위 벗어나거나 santa가 있다")
                # for i in range(N):
                #     print(santa_arr[i])
                continue
            dist = calculate_dist(nr, nc, rr, rc)
            if min_dist>dist:
                min_dist = dist
                du, dv = nr, nc
                move_d = (di, dj)


        if du==r and dv ==c:
            continue
        santa_arr[r][c] = 0 # 원래 위치 복구
        santa_arr[du][dv] = p #새로운 위치로 이동
        santa[p] = [du, dv] #새로운 위치 저장

        if du==rr and dv ==rc:
            crush(du, dv, -move_d[0], -move_d[1], D)
            sleep_santa[p] = k

    if cnt == P:
        break

    for i in range(1, P + 1):
        if die_santa[i] !=1 :
            score[i] += 1

print(*score[1:])