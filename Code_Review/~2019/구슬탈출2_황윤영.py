"""
1차
풀이 시간 : 2시간 15분
시도 횟수 : 3회
실행 시간 : 260ms
메모리 : 114520kb

2차
풀이 시간 : 41분
실행 시간 : 186 ms
메모리 : 25 mb

실수 모음
- break, return 잘못 사용
- 로직 순서 잘못해서 틀림(설계 미흡)
- 문제 조건 잘못 파악(#...)
- 새로운 방법 적용하려다 실수


"""
"""
=============================== 2차 코드 리뷰 ============================
1303 문제 정독 + 주석 정리 
    얼마 전에도 풀었던 문제라 그냥 빠르게 읽혔음
    주석으로 문제 복사 정리 
1311 손설계 간단하게 하고 구현 시작
    
1324 구현완료 후 디버깅
    답이 ㅇ왜 다른가. ! 얼마 전에 풀었는데 !! 
    # 틀림 이슈 X 아님 # 임
    MOVE 의심해서 중점적으로 프린트 디버깅 (구멍에 들어가야할 위치로 가야하는데 거기로 간 적이없;)
    변수를 맘대로 변경하는 것 같아 du, dv 변수 새로 선언해서 사용해 봄
    그러다 move 함수 실행시킬 때 들어가는 변수 잘못 넣은 것 확인해서 수정 
    step 바깥에서 올리는 방법 잘못 사용한 것 확인 해서 기존 방법대로 수정함 
1344 제출 후 오답
    rank 종료 조건 틀린 것 확인

총평 및 피드백 
- 기출 후에 서너번은 더 풀어봤는데도 또 실수를 했다. 
- 문제 조건 잘읽기. 새로운 방법은 지금은 가능한 한 적용 안하기
    
"""

"""
N, M
. 빈칸
# 장애물
R : 빨간사탕
B : 파란사탕
O : 출구

바깥 부분 모두 장애물로 막힘

상하좌우로 기울임. 기울어진 방향으로 사탕 끝까지 미끄러짐.
미끄러지는 도중에 상자를 다른 방향으로 기울일 수는 없습니다

빨간색 사탕을 밖으로 빼야 하지만, 파란색 사탕이 밖으로 나와서는 안됩니다.
빨간색 사탕이 나오기 전에 파란색 사탕이 먼저 나오면 안되며
빨간색 사탕이 나올 때 파란색 사탕이 동시에 나오는 것도 안됩니다.
"""
from collections import deque

def bfs():
    q = deque([(br, bc, rr, rc, -1, -1, 0)])
    step = 0

    while q:
        cbr, cbc, crr, crc, bdi, bdj, rank= q.popleft()

        if rank==10:
            return -1
        if bdi == -1:
            DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
        elif bdi:
            DIR = (0, 1), (0, -1)
        else:
            DIR = (-1, 0), (1, 0)

        for di, dj in DIR:
            nbr, nbc = move(cbr, cbc, di, dj)
            if arr[nbr][nbc] == 'O':
                continue
            nrr, nrc = move(crr, crc, di, dj)
            if arr[nrr][nrc]=='O':
                return rank+1

            if nbr==nrr and nbc == nrc:
                if di<0 or dj<0: #상 또는 좌로 이동
                    if cbr<crr or cbc < crc: #파랑이 위쪽 또는 왼쪽에 있으면
                        nrr -= di
                        nrc -= dj #빨강을 뒤로 물러주기
                    else:
                        nbr-=di
                        nbc-=dj
                else:
                    if cbr<crr or cbc < crc: #
                        nbr -= di
                        nbc -= dj
                    else:
                        nrr -= di
                        nrc -= dj
            if nbr==cbr and nbc==cbc and nrr == crr and nrc == crc:
                continue
            q.append((nbr, nbc, nrr, nrc, di, dj, rank+1))
    return -1
def move(r, c, di, dj):
    du, dv = r, c
    while arr[du][dv] != '#':
        du += di
        dv += dj
        if arr[du][dv] == 'O':
            return du, dv
    du-=di
    dv-=dj
    return du,dv

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rr, rc = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            br, bc = i, j
            arr[i][j] = '.'

answer = bfs()
print(answer)



"""

=============================== 1차 코드 리뷰 ============================
총 풀이시간 2시간 15분
실행시간 260ms
메모리 114520kb

1534 문제읽기 시작
1538 문제 이해했으나 구현 방법 바로 안떠오름 ㅠ
1547 구상 완료
1622 구현은 완료했는데 index error .... 디버깅 해보자 ,,
        R이 자꾸 #의 위치로 이동함(R이 TMP상에서 사라지는 문제 발생 ;)
1633 B가 이동하려다가 R을 만나서 R을 먼저 이동시킬 때 B가 R을 삼키는 것 같다 ,, R 사라짐
1718 테케 다 맞고 .. 만든 테케도 다 맞는데 뭐가 문제인지 모르겠음
        답이 10일 때가 문제일까 ...?
        10 11 인 경우 해봤는데 이것도 맞음 ㅠㅠ
10 10
##########
###...####
#R..#...##
#######.##
#####...##
#.###.####
#.#...##.#
###.#..###
#B#.##O.##
##########

#answer 10

10 10
##########
#R#...####
#...#...##
#######.##
#####...##
#.###.####
#.#...##.#
###.#..###
#B#.##O.##
##########
ans -1


1743 진심 뭐가 문젠지 모르겠다 ^^^^^^^^^^^^^^^^^^^^^^^^^ 화남. ..
1906 밥먹고와서 4분만에 에러 찾았습니다 ...!

=================틀린 원인=================
1. 초기 구현 후 디버깅 시엔, 파란구슬 앞에 빨간 구슬이 있는경우,
    빨간 구슬 움직임에 따라 파란구슬 처리 미흡
2. 빨간 구슬 구멍에 빠졌을 때, 파란 구슬도 이어서 체크해야 하므로
    배열에 반영해 놓고 파란색 계속 움직였어야 함
3. 마지막 최고 날 고생시키게 한!
    빨간 구슬이 빠졌을 경우, 둘다 not move여서 return -2가 먼저 되어버릴 경우가 있을 수 있음
    따라서 return이 나오는 if문의 순서를 바꿨더니 정답처리 됨

=================구상 ================
1. 구슬 움직인 횟수와 움직임 방향 정하기 => 백트 with dfs 활용
    level이 움직인 횟수
    level == 10 일 때 상태로 -1 출력 여부 판정
    (answer = inf 로 해두고 최종 출력 때 -1할것. 최솟값 찾아야하므로)

    구슬 움직일 수 있는지 확인하고 없으면 return

    한번이라도 answer 갱신된 적 있으면 -1 출력 안하고 바로 return 되도록 하기
2. 구슬 이동 구현
    주어진 방향 따라 B 움직이기
        벽 만나면 STOP
        R 만나면 R 움직이고 B 마저 움직이기 (R움직였다는 flag 변환)
        구멍 만나면 flag_B 변환
    R움직인 적 없으면 R 움직이기
        벽이나 B 만나면 STOP
        구멍 만나면 flag_A 변환
    flag_B True면 0 (불가능)
    flag_A True면 1 (정답 갱신하기)
    둘 다 아니면 다음 dfs 호출   return -1

"""


def dfs(level, arr):
    global answer
    if answer <= level:
        return
    # 구술 한번이라도 움직일 수 있는지 확인. 없으면 return

    # 종료 조건
    if level == 11:
        return
    for d in (-1, 0), (0, -1), (1, 0), (0, 1):
        tmp = [arr[i][:] for i in range(N)]  # 복사해서 움직여보자
        # print(d, level, answer)
        result = move(d, tmp)
        # print("=====move 이후 ======")
        # for k in range(N):
        #     print(tmp[k])
        if result == 0:  # b 빠짐
            continue
        elif result == 1:  # r이 먼저 빠짐
            # print("============answer 갱신 ===========")
            answer = min(answer, level)
            return
        elif result == -2:  # 아무 움직임 없음
            continue
        else:

            dfs(level + 1, tmp)


def move(d, arr):
    flag_R = False
    move_R = False
    blue_move = False
    red_move = False
    rr, rc = -1, -1
    br, bc = -1, -1
    # 구슬 위치 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                rr, rc = i, j
            elif arr[i][j] == 'B':
                br, bc = i, j
    du, dv = br, bc
    # 파란 구슬 이동시키기 d방향으로
    while 1:
        du += d[0]
        dv += d[1]
        if arr[du][dv] == '#':
            du -= d[0]
            dv -= d[1]
            break
        if arr[du][dv] == 'O':
            return 0
        # 빨간 구슬이면 빨간 구슬 부터 다 이동시키고 마저 이동해
        if arr[du][dv] == 'R':
            if move_R:
                du -= d[0]
                dv -= d[1]
                break
            move_R = True
            hole = move_red(d, rr, rc, arr)
            if hole == 1:
                flag_R = True
            else:
                du -= d[0]
                dv -= d[1]
            if hole != 0:
                red_move = True

    # 파란구슬 이동
    if br != du or bc != dv:
        arr[br][bc] = '.'
        arr[du][dv] = 'B'
        blue_move = True
    if not move_R:
        hole = move_red(d, rr, rc, arr)
        if hole == 1:
            flag_R = True
        if hole != 0:
            red_move = True

    if flag_R:
        return 1
    if not red_move and not blue_move:
        return -2
    return -1


def move_red(d, rr, rc, arr):
    di = rr
    dj = rc

    while 1:
        di += d[0]
        dj += d[1]
        # print(du, dv)
        if arr[di][dj] == '#' or arr[di][dj] == 'B':
            di -= d[0]
            dj -= d[1]
            break
        if arr[di][dj] == 'O':
            arr[rr][rc] = '.'
            return 1
    arr[rr][rc] = '.'
    arr[di][dj] = 'R'

    if rr == di and rc == dj:
        return 0  # 움직임 없음
    return -1  # 움직이긴 함 . 구멍 x


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
inf = 11
answer = inf
dfs(1, board)
print(answer if answer != inf else -1)
