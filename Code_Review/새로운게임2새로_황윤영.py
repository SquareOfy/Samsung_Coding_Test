"""
1차
풀이 시간 : 3시간 30분
시도 횟수 : 3회
실행 시간 : 172 ms
메모리 : 113084 kb

2차
풀이 시간 : 40분
시도 횟수 : 1회
실행 시간 : 176 ms
메모리 : 113084 kb

- 실수 모음
    - 말이 이동할 때 한꺼번에 이동되는데, 이 때 info배열도 함께 수정해줘야함을 놓침
        1,2차 모두 또옥같이 실수함;;

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 파란색 반대편으로 이동할 때 코드 안더러워지게 주의하기
    : 방향 배열 바꿨다가 디버깅 때 더 헷갈리니까 그냥 있는거 사용하기
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok !
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!

"""

"""
======================== 2차 코드 리뷰 =============================

녹화를 깜빡하고 못했다 ..^^ .. 

1차 때랑 똑같은 코드 똑같이 짜다가 똑같이 문제 발견하고 해결함 
말 info 배열 활용하다가, 말이 다른 말에 딸려서 이동될 때 업데이트 안하는 문제

다만, 1차 때는 업데이트를 매번 하려고 하다가 실수 엄청 많이 나와서 한참 걸렸다면
 2차 때는 빠르게 움직일 말을 찾기 위해 그냥 배열 전체 탐색하는 방식을 바로 택하여 
 비교적 빠르게 해결했다. 
"""
"""

n * n 격자판
격자판은 흰색, 빨간색, 파란색 중 하나의 색
말은 총 k개가 주어지며, 모두 격자판의 한 지점에 놓여있습니다
1번부터 k번까지 번호가 지정되어 있으며 이동 방향 또한 미리 정해져있습니다.
상하좌우의 4가지 방향으로 움직일 수 있습니다.

쌓여있는 말을 이동하는 경우에는 본인 위에 있는 말과 함께 이동

말이 이동하려는 칸이 흰색인 경우에는 해당 칸으로 이동
    이동하려는 칸에 말이 이미 있는 경우에는 해당 말 위에 이동하려던 말을 올려둡니다
    이미 말이 올려져 있는 상태에도 말을 올릴 수 있습니다.

이동하려는 칸이 빨간색인 경우에는 해당 칸으로 이동하기 전 (옮길 말들의) 순서를 뒤집습니다.
    이동하려는 칸에 말이 있는 경우에는 흰색 칸과 같이 그 위에 쌓아둡니다.

이동하려는 칸이 파란색일 경우에는 이동하지 않고 방향을 반대로 전환한 뒤 이동
    만일 반대 방향으로 전환한 뒤 이동하려는 칸도 파란색이라면 방향만 반대로 전환한 뒤 이동하지 않고 가만히 있습니다.
    이동하려는 말에 다른 말들이 쌓여있을 경우에 이동하려는 말만 방향을 반대로 바꿔야 함

격자판의 범위를 벗어나는 이동일 경우 파란색으로 이동하려는 것과 똑같이 생각하여 처리

아직 한 턴이 다 끝나지 않은 경우더라도 말이 4개 이상 겹쳐지는 경우가 생긴다면 그 즉시 게임을 종료
 게임이 종료되는 순간의 턴의 번호

 1: 오른쪽
 2: 왼쪽
 3: 위쪽
 4: 아래쪽


"""


def change_direction(i):
    if i in (1, 2):
        return 3 - i
    else:
        return 7 - i

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def find_place(k):
    for i in range(N):
        for j in range(N):
            if k in mal_arr[i][j]:
                return i, j
def move():
    for k in range(1, K + 1):
        # r, c, d = mal_info[k]
        r, c = find_place(k)
        d = mal_info[k]
        result = move_to_point(k, r, c, d, 0)
        if result:
            return result
    return False

def move_to_point(k, r, c, d, flag):

    di, dj = DIR[d]
    du, dv = r+di, c+dj
    if oob(du, dv) or arr[du][dv] == 2:
        if not flag:
            return move_to_point(k, r, c, change_direction(d), 1)
        else:
            mal_info[k] =d
            du, dv = r, c

    elif arr[du][dv] == 0:
        idx = mal_arr[r][c].index(k)
        mal_arr[du][dv].extend(mal_arr[r][c][idx:])
        mal_arr[r][c][idx:] = []
        mal_info[k] = d

    elif arr[du][dv] == 1:
        idx = mal_arr[r][c].index(k)
        tmp = mal_arr[r][c][idx:]
        mal_arr[r][c][idx:] = []
        tmp = tmp[::-1]
        mal_arr[du][dv].extend(tmp)
        mal_info[k] =d


    return len(mal_arr[du][dv])>=4
# 입력 받기
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mal_arr = [[[] for _ in range(N)] for _ in range(N)]
mal_info = [-1]
DIR = (-1, ), (0, 1), (0, -1), (-1, 0), (1, 0)

for k in range(1, K + 1):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    mal_arr[x][y].append(k)
    mal_info.append(d)

turn = 0
# while (turn 진행)
while 1:
    # turn +
    turn += 1
    # 종료조건
    if turn > 1000:
        turn = -1
        break
    # 말 옮기기
    result = move()
    if result:
        break

print(turn)


"""
나의 삽질기 ...

세시간 풀로 투자해서 봐야할 문제가 있다면 이거다. 난이도에 비해 삽질한 최고봉 문제

1451 어른상어와 새로운게임2 문제 비교하여 이 문제 선택함
    선택이유 : 상어마다 우선순위 다른거 어려워보여서 ..

1501 새로운게임 본격적으로 문제 읽고 구상 시작
    주석+종이에 주의사항 / 구현방식 메모
    주석 달면서 종이에 일부 구현 정리한 것들 구현함
    중간중간 놓치는 구현들이 많음.
        - 나보다 아래 있는 말은 함께 이동하지 않음 근데 한번에 구현했다가 그림과 비교하며 찾고 수정
        - 배열에 해당 말이 언제 시작하는지 알아야해서 dict에 중간에 st 추가 (화근)
    함수화 + 재귀로 파란걸 다시 만나는 경우 처리는 좋았다 ; 하지만 시간 내에 못 풀엇쬬 ..^^?
    dir 갱신 과정, 타이밍에서 실수 많이 함 ㅠㅠ
1530 대략적인 틀 구현 다 하고 테케 안맞아서 무한 디버깅 함
    말이 내가 원하는대로 자꾸 이뤄지지 않음 원인을 모르겠다 ;;

    디버깅 과정이 너무 어려웠음
        - 이동하는 말의 정보는 dict에 따로 저장
        - arr 배열은 3차원으로 프린트하기 힘들고,,
        - 그래서 주먹구구 식으로 막 프린트 찍다가 이러다 큰일 나겠다는 생ㅇ각함;
    말 계속 이상하게 이동한다? dict 찍어봤더니 st값 이상함
        - st를 dict에 갱신하는 과정이 없었다는 것 알게됨 + 어떤 말 옮기면 그 위에 같이 옮긴 말들 정보까지
            싹다 dict에 갱신해줘야함을 깨닫고 로직 추가ㅏㅎㅁ
        - 그런데도 st가 원하는대로 컨트롤 되지 않아 나중엔 옮길 때 st를 돌아서 찾아보는 방식으로 수정

1613 체스판 색깔 확인하는데 board 말고 arr 사용했다는 사실 발견
    - board 값이 체스판의 색깔을 담은 배열인데 습관적으로 arr을 씀
        - 자주 쓰지 않는 변수명의 폐해 혹은 뭐가 씌었나 ! 정신차려라
    - 이 때 갈아엎었어야했음
    - board를 고쳐도 에러의 갈피가 안잡힘
    - 프린트 아무리 찍어봐도 말이 정상 이동하는 것으로 보이며 마지막 테케가 안맞는데,
    - 테케 규모가 크고,, 말이 많아서 확인이 쉽지 않음
    - 디버거 써도 dict와 arr로 관리하는 구조 때문에 쉽지 않았다

1644 포기.
    갈아엎을지 상어 문제로 넘어갈지 고민함
    내 로직이 분명 맞다는 생각이 드는데, 다시 뒤집어 엎었을 때 똑같이 테케가 안맞으면 디버깅할 자신 없었음
    + 어른상어 최근에 많이 구현해본 스타일이라 할 수 있을거라 생각됨(방법 머릿속에 구상됏음)
    = 어른상어로 넘어가기로 결정

2028 ~ 2100
    어른상어 30분 가량 디버깅 with 디버거 손으로 테케 따라가기
    진짜. 나 . 맞는데. 어디가 틀린건지 모르겠고 코드 너무 더러움을 느꼇고 ,,
    30분 더 디버깅해봤으니 코드 버리고 새로 짜는게 맞다는 생각이 들어 뒤집어엎기로 함



다시하기 ;;
2249
말의 방향을 mal_dir 배열로 관리하자
board배열은 말의 색깔 표시
arr 배열은 거기에 들어있는 말 리스트를 관리하자


2313 성공 (23분만에 ;;)
    뒤집어 엎는게 맞았군
    기존 로직 그대로 스무스하게 성공 .. 스무스하지 않았다
    달라진 점 = dict 버림. 상어 방향 배열로 따로 들고 가기

피드백
못한점
 - 왜 arr과 dict 따로 관리했는가
     - 낚시왕 문제를 풀며 동일한 개체를 배열과 dict 처럼
        두 곳에 두고 정보를 둘다 동일하게 업데이트 해야하는 방식의 구현이 실수를 남발하게 함을 느꼈었음
        그리고 오늘 코드리뷰때도 앞으론 안 그러겠다고 다짐까지 했는데
        홀린듯; 바보같이 또 그렇게 구현했다.
        모든 정보를 매번 한곳에 다 담아서 관리할 필요 없다
        dict에 한번에 모아둔다고 더 사용하기 편하지 않다
        요소를 분리하는 작업을 잘 ㅎㅏ 자
 - 최악의 시간 분배
    1시간 남았을 때 문제를 넘어간다? 절대 안된다
    이 문제를 버리고 포기할거라면 최소한 1시간 30분은 남았을 때 넘어가야함을 느낌 (나는 구현 속도가 빠르지 않다)
    1시간 30분 남았을 때 어려움을 겪고있다면 앞으로 무조건 둘 중 하나를 선택하자 => 문제 버리고 넘어가기(두문제라면) or 뒤집어 엎기
    이번의 경우는 뒤집어 엎기를 먼저 선택했어야 했다.
    문제 중간에 dict 요소가 날 더 어렵게 했고 디버깅과 잦은 수정으로 인해 코드가 더러워졌고 문제 이해 됐으니까 ..

- board arr 이런 실수? 정신차려
    변수명 정신차리고 기억하자 못하겠으면 주석이라도 옆에 달아놔라
- 커피 마시지 말자 ............

잘한점
    없다





"""
def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N


def find_point(mal):
    for i in range(N):
        for j in range(N):
            if mal in arr[i][j]:
                return i, j, arr[i][j].index(mal)
    return -1, -1, -1


def move(k, r, c, d, st, flag):
    di, dj = directions[d]

    du = r + di
    dv = c + dj
    # print(f"============={k}번째 말 움직이기=============")
    # print(f"r : {r}   c : {c}    d : {d}")
    #
    if (oob(du, dv) or board[du][dv]==2) and not flag:
        # print("범위 아웃 또는 파랑 만남")
        #방향 바꾸기
        d = change_dir(d)
        dir_idx[k] = d
        di, dj = directions[d]
        du += di
        dv += dj
        return move(k, du, dv, d, st, 1)
    elif (oob(du, dv) or board[du][dv]==2) and flag:
        # print("또 범위아웃 파랑만나서 그대로 ")
        #안움직임. 그대로
        return False
    elif board[du][dv] ==0:
        #흰색이면
        arr[du][dv].extend(arr[r][c][st:])
        arr[r][c][st:] = []
    elif board[du][dv] ==1:
        tmp = arr[r][c][st:]
        tmp = tmp[::-1]
        arr[du][dv].extend(tmp)
        arr[r][c][st:] = []



    return len(arr[du][dv])>=4


def move_all():
    for k in range(1, K + 1):
        # 현재바라보는 방향
        d = dir_idx[k]
        r, c, st = find_point(k)

        if move(k, r, c, d, st, 0):
            return True

    return False


def change_dir(d):
    if d>2:
        return 7-d
    return 3-d


N , K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
dir_idx = [0]*(K+1)

#방향이동 d>2 이면 7-d
#방향이동 else 3-d
directions = (0,), (0, 1), (0, -1), (-1, 0), (1, 0)
for k in range(1,K+1):
    r, c, d = map(int, input().split())
    arr[r-1][c-1].append(k)
    dir_idx[k] = d

answer = 0

while 1:
    answer +=1
    if answer>1000:
        break
    if move_all():
        break
print(answer if answer <=1000 else -1)
