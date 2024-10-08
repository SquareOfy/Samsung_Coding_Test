"""
1차
풀이 시간 : 3시간 + @ (밥먹고 와서 5분..)
실행 시간 : 368ms
메모리 : 29mb

2차
풀이 시간 : 46분
실행 시간 : 338 ms
메모리 : 28 mb

- 실수 모음
    - 시간관리 실패.. 이상하게 꼬였었음(1차)
    - 코드 뒤엎을 때 변수 수정 덜해서 더 꼬임
    - 남 안되고 서 볼 때 check(남) 함수 호출 시 옆으로 이동한 입력 안넣어줌
"""
"""
격자는 가장 위를 1행, 가장 아래를 R행
총 K명의 정령은 각자 골렘을 타고 숲을 탐색

골렘은 십자 모양의 구조
골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구

정령은 어떤 방향에서든 골렘에 탑승할 수 있지만
골렘에서 내릴 때에는 정해진 출구를 통해서만 내릴 수 있습니다.

골렘은 숲의 가장 북쪽에서 시작
골렘의 중앙이 ci 열이 되도록 하는 위치에서 내려오기 시작
초기 골렘의 출구는 d 의 방향에 위치

(1) 남쪽으로 한 칸 내려갑니다.
    [r+1][c-1], [r+2][c] , [r+1][c+1]

(2) (1)의 방법으로 이동할 수 없으면 서쪽 방향으로 회전하면서 내려갑니다.
    서쪽 : [r-1][c-1] [r][c-2] [r+1][c-1]

(3) (1)과 (2)의 방법으로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려갑니다.
    동쪽 : [r-1][c+1] [r][c+2] [r+1][c+1]


"""
from collections import deque

def printa(string, arr):
    print(f"=============={string}==============")
    for i in range(len(arr)):
        print(arr[i])
    print("====================================")
    print()
def oob(i, j):
    return i < 0 or j < 0 or i >= R + 3 or j >= C


def check(cd, r, c):
    if cd == 0:  # 남쪽 체크
        if oob(r + 2, c):
            return False
        if arr[r + 1][c - 1] or arr[r + 2][c] or arr[r + 1][c + 1]:
            return False
    elif cd == 1:  # 서쪽 체크
        if oob(r + 1, c - 2):
            return False
        if arr[r - 1][c - 1] or arr[r][c - 2] or arr[r + 1][c - 1]:
            return False
    else:  # 동쪽 체크
        if oob(r + 1, c + 2):
            return False
        if arr[r - 1][c + 1] or arr[r][c + 2] or arr[r + 1][c + 1]:
            return False
    return True


def move_near_gol(gol_num, r):
    global answer
    visited = [0] * (K + 1)
    visited[gol_num] = 1
    q = deque([gol_num])
    mx = r
    while q:
        num = q.popleft()
        cr, cc, cd = gol_info[num]
        mx = max(mx, cr+1)
        cdi, cdj = DIR[cd]
        cr+=cdi
        cc+=cdj
        for di, dj in DIR:
            du, dv = cr+di, cc+dj
            if oob(du, dv): continue
            if arr[du][dv] == 0: continue
            G_num = arr[du][dv]
            if visited[G_num]: continue

            q.append(G_num)
            visited[G_num] = 1
    return mx

R, C, K = map(int, input().split())
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
arr = [[0] * C for _ in range(R + 3)]

answer = 0

gol_info = [[] for _ in range(K + 1)]
for k in range(1, K + 1):
    c, d = map(int, input().split())
    c -= 1
    r = 1

    while 1:
        if check(0, r, c):
            r += 1
        elif check(1, r, c) and check(0, r, c-1):
            r += 1
            c -= 1
            d = (d - 1) % 4
        elif check(2, r, c) and check(0, r, c+1):
            r += 1
            c += 1
            d = (d + 1) % 4
        else:
            break
        if r == R + 1:
            break

    if r < 4:
        arr = [[0] * C for _ in range(R + 3)]
        continue
    gol_info[k] = (r, c, d)
    arr[r][c] = k
    for di, dj in DIR:
        du, dv = r + di, c + dj
        arr[du][dv] = k
    # printa(f"{k}", arr)
    answer += move_near_gol(k, r) -2
    # print("answer : ", answer)
print(answer)

"""
1차 코드리뷰

풀이 시간 : 3시간 + @ (밥먹고 와서 5분..)
실행 시간 : 368ms
메모리 : 29mb


============================== 풀이과정 ======================================

1405 문제 정독
    보자마자 쉽다고 생각함.......... 하지만 1시간반의 헛짓거리 덕에 시간 내에 못품이슈
    주석 정리하면서 머릿속으로 조금 구상 됨

1420 구상 및 설계 시작
    - 문제에서 말한 그대1~~~로 구현하면 되겠다고 생각함
    - 머리 빼꼼 내밀어서 남쪽 갈 수 잇으면 내밀고, 아니면 서쪽 갈 수 있는지 보고 없으면 동쪽가기
        if문 잘 쓰고 while문으로 해서 갈 수 없을 때까지 돌면 되겠다고 생각하고 설계
    - 구현할 영역 주석 정리
1440 구현시작
    - 구현하면서 추가로 주석 더 씀.. 이런건 참 잘했는데 말이지

1501 구현완료 디버깅
    can_move 함수에서 index 에러 oob로 처리
    print 찍어가면서 왜 can_move 통과했는지 어디서 걸리는지 왜 통과 못하는지 확인함
    통과를 못하는게 아니라 종료 조건이 부족했던 거 깨닫고 수정
    row 값이 1부터 시작인데 안더해준 것 확인
    답 또 안나오길래 블럭 하나씩 내려올때마다 arr 출력해서 확인
    그래도 답이 안나온다 1!! 블럭 안에 못들어갈 때 배열 RESET 놓침
    뭔가 답이 이상해서 출력해가면서 봤고 아직 십자가 모양이 배열안으로 안들어왔을 때
    봐야하는 아래칸의 경우가 다른걸 깨닫고 can_move 함수의 조건문 수정
    원하는 답 나왔고 그래도 모든 절차 모양 동일한지 한번 더 체크
1529 제출하기 직전 아 뭔가 마진 넣어서 해야할 것 같은데 생각함
    can_move의 if문이 다소 부실하지 않을까하는 생각을 스치듯이함
    지금 생각해보면 이 때가 원샷원킬로 정답 맞출 수 있는 절호의 기회였는데 수정하다가
    테케 답 안맞으니까 아잇 그냥 일단 내보자 하고 원상 복구하고 대차게 틀림
    근데 그랬으면 다시 수정해볼 것이지 일단 테케 담아서 출력해보며 어떤 현상으로
    답이 틀린지 확인 후 can_move 조건문 추가로 수정해보려 했으나 잘 안됐음.
    근데 그러고 저거 고쳐볼 생각 안하고 설계 새로하려고 함 ;;

    뭔가 이상하게 생각이 꼬인듯하다. 순간 아래 쌓인 블럭들을 잘못 보고
    저 마진으로도 해결 못할 거라고 생각함
1541 새로운 설계 세우고 구현
    완탐 방식으로 다 보고 낮은 곳 찾으려함

    서쪽 다 보고(남 포함) 못가면 동쪽 다 봐서 갈 수 있는 낮은 곳으로 내려가는 방식
    제출 후 테케 보고 아 ... 중간에 같아지면 못가는구나 하고 break 조건 넣음
    이 과정에서 기존 코드를 뜨개질하다보니 변수 세팅, 그렇게 해서 찾은 애들가지고
    행값, 열값, 그 때의 출구 방향 기억하는게 굉장히 복잡해졌었음...
    이 방법이 맞앗더래도 리셋을 해야했을 시점

1605 5분 휴식 후 내가 지금 하던 방법 안되면 다른거 더 생각해보자고 판단. .
    이 때 왜 R+3을 생각못했냐 이말이야 정말 이해가 안간단 말야
    진짜 마지막 기출인데 왜이러냐고
    그래서 이번엔 lst에 내려갈 지점을 담아보는 방식으로 구현했는데 택도 없엇음
    테케도 안맞고 파일은 많아지고 헷갈리고 헤매다 시간 끝남
    ㅎ ㅏ

저녁 먹고 R+3 생각나서 바로 해봤더니 정답;

총평 피드백
분명 풀 수 있는 문제였다. 뭐가 씌인듯 시야가 갇혔다.
5분 리프레쉬를 잘 활용하지 못했다. 분명 풀이 중간에 솔루션을 생각했는데 선택하지 않았다.
=> Reset 타이밍도 실수 체크리스트처럼 정해서 남은 기출 뺑뺑이에서 적용할것.
마지막 기출 쯤에 3문제를 연달아 넘어지니 불았했다. 이게 최근 경향인데 너무 못푼다.
자신감 뚝 떨어짐ㅇ ㅣ슈  막혔을 때 전략 어떻게 세워야할지 너무 어렵군
일단 실수를 줄이고,, 설계를 할 때 예외 상황이나 주의사항은 뭐가 있는지 점검하는 부분을 더 확실히 하자.


============================ 피드백 ==========================================
"""


#  각 골렘은 십자 모양의 구조 . 중앙 칸을 포함해 총 5칸을 차지
# 골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구입니다
# 어떤 방향에서든 골렘에 탑승할 수 있지만 내릴 때에는 정해진 출구를 통해서만 내릴 수 있다


# (1) 남쪽으로 한 칸 내려갑니다.
# (2) (1)로 이동할 수 없으면 서쪽 방향으로 회전하면서 내려갑니다. 서쪽 한 칸이 모두 비어 있어야 함
# 출구가 반시계방향으로 이동
# (3) (1)과 (2)의 안되면 동쪽 방향으로 회전하면서 내려갑니다.
# 골렘을 기준으로 동쪽 한 칸이 모두 비어 있어야 함에 유의
# 출구가 시계방향으로 이동


def oob(r, c):
    return r < 0 or c < 0 or r >= R + 3 or c >= C


def can_move(r, c, dk):
    if dk == 2:
        if oob(r + 2, c):
            return False
        if not arr[r + 2][c] and not arr[r + 1][c - 1] and not arr[r + 1][c + 1]:
            return True
        return False
    elif dk == 3:
        if oob(r, c - 2):
            return False
        if not arr[r][c - 2] and not arr[r + 1][c - 1] and not arr[r - 1][c - 1]:
            return True
        return False
    elif dk == 1:
        if oob(r, c + 2):
            return False
        if not arr[r][c + 2] and not arr[r + 1][c + 1] and not arr[r - 1][c + 1]:
            return True
        return False


def move_to_exit(r, c, d):
    mx = r + 1 #초기값 : 나의 제일 아래칸
    er, ec = r + DIR[d][0], c + DIR[d][1]
    for di, dj in DIR:
        nr, nc = er + di, ec + dj
        if oob(nr, nc) or arr[nr][nc] == 0 or arr[nr][nc] == i:
            continue
        num = arr[nr][nc]
        if visited[num] == i: continue
        ngr, ngc, ngd = gol_info[arr[nr][nc]]
        visited[num] = i
        tmp = move_to_exit(ngr, ngc, ngd) #출구를 통했을 때의 최대 아래 행index
        if tmp > mx:
            mx = tmp
    return mx


R, C, K = map(int, input().split())
arr = [[0] * C for _ in range(R + 3)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
gol_info = [0] * (K + 1)
visited = [0] * (K + 1)
answer = 0
for i in range(1, K + 1):
    cc, d = map(int, input().split())
    cr = 1
    cc -= 1

    while 1:
        if can_move(cr, cc, 2): #남쪽으로 이동하면
            cr += 1
        elif can_move(cr, cc, 3) and can_move(cr, cc - 1, 2): #서쪽으로 이동 후 남쪽 이동 가능하면
            cr += 1
            cc -= 1
            d = (d - 1) % 4

        elif can_move(cr, cc, 1) and can_move(cr, cc + 1, 2): #동쪽으로 이동 후 남쪽 이동 가능하면
            cr += 1
            cc += 1
            d = (d + 1) % 4
        else:
            break
        if cr == R + 1:
            break

    if cr < 4:
        arr = [[0] * C for _ in range(R + 3)]
        continue

    arr[cr][cc] = i
    for di, dj in DIR:
        arr[cr + di][cc + dj] = i
    gol_info[i] = (cr, cc, d)
    tmp = move_to_exit(cr, cc, d) - 2
    answer += tmp

print(answer)
