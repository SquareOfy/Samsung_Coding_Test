"""
1차
풀이 시간 1시간 42분 (다시풀어도 오래걸림)
시도 횟수 2회
실행 시간 100ms
메모리 111240kb


2차
풀이 시간 : 58분
시도 횟수 : 1회
실행 시간 : 92 ms
메모리 : 109240 KB

- 실수 모음 (또옥같은 실수 함)
    - 문제 맘대로 이해해버리기
    - 배열 복사 후 원본 배열 dfs에 넘기기
    - 방향 벡터 index 평소랑 달리 1 마진 넣었다가 모듈 헷갈림;
    -

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 배열 복사하자
    : 술래가 도둑 잡을 때 배열에 이동시키는 순서 주의하자. 뭐가 먼저
    : N칸 도착하자마자 내리는 거 놓치지 말기!!
5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인
    : 답 다르길래 deque 사람 움직이기 전 후로 프린트+종이테케 따라가기로
    틀린 부분 찾음
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!

"""

"""
========================== 2차 코드리뷰 ===========================
1917 문제 읽기 + 주석
1925 설계 시작
    도둑 이동 메인 로직
    술래 이동 메인 로직짜고 이 때 배열 바꾸는거 순서 중요하게 고려함
    배열 뭐 복사해서 들고다닐건지 정해둠
    입력받는거 복잡해서 이것도 설계
1936 구현
1956 구현 완료 후 테케 안맞아서 디버깅버깅버깅
    왜 상어를 미친듯이 잡아먹는거지 
    봤더니 상어를 안잡아먹고 냅둠. 
    물고기 이동도 안함. 
    arr 넘긴 것 확인 
    고쳤는데 더 많이 먹음
    아 도둑이구나 ;
    아무튼 많이 먹음
    ---------------------잠깐 팀장님 공지가 있었음-----------------------
    돌아와서 다시 보니 도둑 이동에서 이동할 자리를 못잡음 
    d 값을 이상하게 구한 사실 + 이동도 이상하게 시킨 것 발견해서 고치고 해결

"""

"""
4 x 4의 격자로 이루어진 체스판
술래 말 하나만 사용하여 도둑말을 잡으며
말의 방향이란 해당 말이 이동할 수 있는 방향을 의미하며
상하좌우, 대각선에 해당하는 8가지의 방향의 종류

말판의 위치 0번 인덱스부터 시작
각각의 도둑말에는 1이상 16이하의 번호가 서로 겹치지 않게 매겨져 있음

초기에는 (0, 0)에 있는 도둑말을 잡으며 시작

- 도둑말 이동
    도둑말은 번호가 작은 순서대로 본인이 가지고 있는 이동 방향대로 이동
    한 번의 이동에 한 칸을 이동
    도둑 말은 이동할 수 있을 때까지 45도 반시계 회전  갈 수 있는 칸을 탐색
    만약 이동할 수 있는 칸이 없다면 이동하지 않습니다.
    그 이외의 경우에는 칸을 이동
    해당 칸에 다른 도둑말이 있다면 해당 말과 위치를 바꿉니다.


- 도둑 말의 이동이 모두 끝나면 술래말이 이동
    이동 가능한 방향의 어느 칸이나 이동할 수 있습니다.
     한 번에 여러개의 칸도 이동할 수 있습니다.
    잡고자하는 도둑말로 이동할 때 지나는 칸들의 말들은 잡지 않습니다.
    술래말은 도둑말이 없는 곳으로는 이동할 수 없습니다.
    술래말은 도둑말을 잡을 때마다 잡은 도둑말의 방향을 갖게 됩니다.


만약 술래말이 이동할 수 있는 곳에 도둑말이 더이상 존재하지 않으면 게임을 끝냅니다.

"""


def oob(i, j):
    return i < 0 or i >= 4 or j < 0 or j >= 4


def move_thief(arr, dir_lst, place_lst):
    # 도둑 번호 순대로 움직이기
    for i in range(1, 17):

        cd = dir_lst[i]
        if cd == -1: continue  # 이미 잡힌 도둑은 넘기기
        cr, cc = place_lst[i]

        for k in range(8):  # 내 방향부터 8방을 돌아본다
            nd = (cd+k-1)%8+1


            di, dj = DIR[nd]
            nr = cr + di
            nc = cc + dj
            if oob(nr, nc): continue  # 범위 나가면 못가
            if arr[nr][nc] == -1: continue #술래 있어서 못가
            arr[cr][cc] = 0

            #도둑이랑 자리를 바꾸게 되면
            if arr[nr][nc] != 0:
                nxt = arr[nr][nc]
                #자리 바꾸기
                place_lst[nxt] = (cr, cc)
                arr[cr][cc] = nxt #빈칸 자리 바꾼 도둑번호로 채우기


            arr[nr][nc] = i
            place_lst[i] = (nr, nc)
            dir_lst[i] = nd
            break
    return arr, dir_lst, place_lst


def dfs(arr, score, dir_lst, place_lst, sr, sc, sd):
    # 도둑 이동
    arr, dir_lst, place_lst = move_thief(arr, dir_lst, place_lst)

    # 술래 이동 가능한 lst 찾기
    di, dj = DIR[sd]
    nr, nc = sr+di, sc+dj
    candi_lst = []
    while not oob(nr, nc):
        if arr[nr][nc] != 0:
            candi_lst.append((nr, nc))
        nr+=di
        nc+=dj
    if not candi_lst:
        global answer
        answer = max(answer, score)
        return

    tmp = [[] for _ in range(4)]
    for r, c in candi_lst:
        for t in range(4):
            tmp[t] = arr[t][:]
        tmp_dir_lst = dir_lst[:]
        tmp_place_lst = place_lst[:]

        #원래자리 빈칸 만들고
        tmp[sr][sc] = 0
        plus = tmp[r][c]
        new_d = tmp_dir_lst[plus]
        #도둑 잡기
        tmp[r][c] = -1
        tmp_dir_lst[plus] = -1
        tmp_place_lst[plus] = -1
        # print(f"============={r}, {c}로 술래 이동 후 ==========")
        # for t in range(4):
        #     print(tmp[t])
        # print('=======================================')
        dfs(tmp, score+plus, tmp_dir_lst, tmp_place_lst, r, c, new_d)



    # 종료 조건

    # 술래 이동시켜보기


direction_lst = [0] * 17
place_lst = [None] * 17
arr = [[0] * 4 for _ in range(4)]
DIR = (-1,), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0, 8, 2):
        idx = lst[j]
        d = lst[j + 1]
        direction_lst[idx] = d
        place_lst[idx] = (i, j // 2)
        arr[i][j // 2] = idx

# 위치 저장, 점수 저장 후 배열에 술래 표기
sr, sc = 0, 0
num = arr[0][0]
arr[0][0] = -1
# 방향 저장 후 잡힌 도둑 표기
sd = direction_lst[num]
direction_lst[num] = -1
place_lst[num] = -1
answer = 0
dfs(arr, num, direction_lst, place_lst, sr, sc, sd)
print(answer)

"""


다시 각잡고 풀기 REVIEW
총 풀이시간 1시간 42분 (다시풀어도 오래걸림)
실행시간 100ms
메모리 111240kb

1459 문제읽고 구상 시작 (6분)
    - 처음 문제를 풀었을 때와 이해한 바가 같아서 비슷하게 구상함...
    - 물고기 위치 관리만 따로 배열이나 딕셔너리로 관리하던 방식에서 그냥 배열 탐색해서 찾는걸로 바꿈
    - 다시 봐도 안보였던 문제의 숨은 틈..

1504 주석 개요 작성
1506 구현시작
    - 물고기 위치 찾아오는 단계에서 이미 죽은 물고기 처리를 안해 타입에러 자꾸 발생
        수정 1차 : 죽은 물고기 리스트를 가지고 다니면서 그 물고기가 리스트에 있으면 conitnue
        수정 2차 : 기존 배열을 추가 활용하기 위해 물고기 죽일 때 fish_dir 을 -1로 바꿔두고 -1인지 확인하는 방식
            => 2차 방법으로 하다가 -1로 바꾸는 순서 잘못해서 에러 많이 났었음.
            => fish_dir을 복사해서 tmp로 활용하는 로직을 나중에 추가하면서 꼼꼼하게 수정 못해서 에러 많이 만남

    - 배열복사 누락
        위 수정2차에서 말했듯, fish_dir 누락했고 수정하는 과정에서 수정 안하고 사용한 배열 많아서 디버깅에 시간 소요
    - 값이 전혀다르다?
        회전 후 이동했을 때 회전 값을 안넣었다 -> 복사배열 말고 전역 배열에서 수정했다 -> 매개변수 배열에 정상 수정
    - 일부 테케가 안맞는다?
        이 문제가 나에게 진짜 특히 어려웠던 점.
        나는 중간중간 오타나 자잘한 로직 실수가 많은 편인데. 문제에 단계별 테케 예시도 없고,, 손으로 따라가기도 쉽지 않은 유형의 입력 ;
        그리고 print 디버깅 하기 매우 까다로운 dfs ..이런 문제의 경우 어떤 디버깅 방법이 좋을지, 테케 테스트는 어떻게 해야할지 고민이다.

        하지만 어쩔 수 없다. 안맞는 테케 하나 진짜 손으로 따라갔다.
        따라가다보니 내가 이해한 문제 안에서는 내 답이 맞다.
        그렇다면 합리적 의심. 내가 문제를 잘못 이해했을 가능성 매우 높아짐.
        12가 왼쪽으로 가는데 바로 앞칸이 0이라 내 기준 stop이 맞았다.
        근데 그 한칸 더 앞에 있는 15를 먹으면 테케와 답이 일치했던 상황이었다.
        그래서 내가 문제를 잘못 이해했을 가능성을 다시 두고 문제를 다시 읽음
        문제에서 "상어는 방향에 있는 칸으로 이동할 수 있는데," 이 부분이 가는 길에 물고기 없는 칸을 지나지 못한다는 의미는 아니겠구나 함
        그래서 cal_shark_move 함수에서 arr[du][dv]일때도 break하던걸 뺌. 그랬더니 테케 다 맞아씅ㅁ

    - 제출했더니 오답 + 수정 후 정답
        와 이제 진짜 다다아아아아ㅏ 맞는데 싶었음
        그렇다면 마지막 그 부분이 걸림.
        생각해보니 움직이지 않았을 때 cnt!=0이지만 벽까지 가는 길이 다 0(빈칸)이어서 물고기를 먹은적이 없을 때
        그 때의 물고기 번호 합을 갱신 안했다는 사실 깨달음
        종료 조건문 + 갱신 부분을 for문 아래로 이동하고 flag로 체크했더니 정답!


피드백
- 잘한점
    음..? 딱..히..
    처음에 설계할 때 가장 메인로직이 될 함수의 대략적인 구조를 설계하고 주석으로 설계영역 마련해둔 것
    나의 로직이 정말 맞다 싶은데 자꾸 틀려서, 내가 문제 자체를 잘못 이해했을 수 있음을 테케 확인을 통해 검증한 것..?
- 못한점
    - 입력값 받기도 실수함; 중간테스트 ㅠㅠ
        입력 외 다른 부분들은 break가 물고기 움직임 + 상어 이동이 함께 복합적으로 이뤄져야 가능해서 코드 짜면서 중간테스트가 어려웠다 ..
        이럴 경우는 step을 두고 한번씩 움직여서 중간 테스트를 했어야햇나?,,
    - 문제 잘 잘 이해해야 한다. 행간을 안읽는 습관, 내 맘대로 추가적인 의미를 더해 이해하는 습관을 버리기

=============구상 ==================
**초기세팅
 상어 (0, 0) 에 넣어두고 그 자리에 있는 물고기 방향 가지기.


1. 물고기 이동
    1~16 순서대로 이동
    이동방법
     - 자기가 가진 방향으로 갈 수 있으면(상어x / oob x) 이동
        -물고기 있으면 자리바꾸기
        -없으면 이동(빈칸이랑 바꾸기 해야함)
    - 없으면 45도 반시계 회전
        - 갈 수 있는데 찾아서 가고
        - 한바퀴 다 돌아도 이동 불가하면 이동 x

2. 상어 이동
    - 자신의 방향대로 가능한 칸 수 중 하나로 이동
        그 방향에서 가능한 칸 수 찾기
        그 칸대로 for문 돌며 dfs 호출
        - 배열 복사
        - 물고기 먹기

dfs ( 배열, 상어위치, 상어 방향, 먹은 물고기 번호의 합)

    #물고기 이동시키는 함수 호출

    #상어 이동 가능한 칸 카운트
    # 0이면 return / 정답 갱신

    #
    # for 이동 가능한 칸
    #     배열 복사
    #     복사한 배열에서 이동 + 물고기 먹기
    #     dfs 호출

"""

def dfs(arr, shark, sd, sm, fish_dir):

    # print("+++++++++++++++++++++++Dfs 호출 ++++++++++++++++")
    # print(dead_lst)
    # print(sm)
    # print("fish 정보 : ")
    # print(fish_dir)
    # print()

    global answer
    #물고기 이동 함수 호출
    # print(dead_lst)
    move_fish(arr, shark, fish_dir)

    # print("================move 후 =================")
    # print(dead_lst)
    # for k in range(4):
    #     print(arr[k])
    #
    # print(fish_dir)
    # print("=======================================")
    #
    #
    # print("shark 정보 !! : " , sd, eight_dir[sd])

    # 상어 이동 가능한 칸 카운트
    cnt = cal_shark_move(arr, shark, sd)
    # print("cnt : ", cnt)
    r, c = shark
    # 0이면 return / 정답 갱신
    di, dj = eight_dir[sd]

    flag = False
    # for 이동 가능한 칸
    for k in range(1, cnt+1):
        # print("k : ", k)
        du = shark[0]+di*k
        dv = shark[1]+dj*k
        if arr[du][dv]==0:
            continue

        #     배열 복사
        tmp_fish_dir = fish_dir[:]
        tmp = [[] for _ in range(4)]
        for y in range(4):
            tmp[y] = arr[y][:]

        #     복사한 배열에서 이동 + 물고기 먹기
        tmp[r][c] = 0
        catch = tmp[du][dv]
        n_sd = tmp_fish_dir[catch]
        tmp_fish_dir[catch] = -1
        tmp[du][dv] = -1
        flag = True



        #     dfs 호출
        dfs(tmp, (du, dv), n_sd, sm + catch, tmp_fish_dir)
    if cnt == 0 or not flag:
        answer = max(answer, sm)
        return

def find_fish(arr, i):
    # print(f"=======================find fish {i} ===================")
    for y in range(4):
        for x in range(4):
            if arr[y][x] == i:
                return y, x

def move_fish(arr, shark, tmp_fish_dir):
    # print(tmp_fish_dir)
    for i in range(1, 17):
        if tmp_fish_dir[i]==-1:
            continue
        #물고기 찾기
        y, x = find_fish(arr, i)
        d = tmp_fish_dir[arr[y][x]]
        #자기 자리부터 회전
        for k in range(8):
            di, dj = eight_dir[(d+k)%8]
            du, dv = y+di, x+dj
            if oob(du, dv) or (du, dv) == shark:
                continue
            tmp_fish_dir[arr[y][x]] = (d+k)%8
            arr[y][x], arr[du][dv] = arr[du][dv], arr[y][x]
            break

def cal_shark_move(arr, shark, sd):
    du, dv = shark
    di, dj = eight_dir[sd]
    cnt = 0
    # print("sd" , sd)
    while 1:
        du += di
        dv += dj
        # print("du, dv ", du, dv)
        if oob(du, dv):
            break
        cnt+=1
    return cnt

def oob(i, j):
    return i<0 or j<0 or i>=4 or j>=4

arr = [[0]*4 for _ in range(4)]
eight_dir = (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
fish_dir = [0]*17

#4개의 줄에 물고기 번호 / 방향 순으로 8개 숫자 들어옴
for i in range(4):
    lst = list(map(int, input().split()))
    for j in range(0,8,2):
        a, b = lst[j], lst[j+1]
        arr[i][j//2] = a
        fish_dir[a] = b-1


answer = 0
# for i in range(4):
#     print(arr[i])
r, c = 0, 0
num = arr[0][0]
sd = fish_dir[num]
# print(fish_dir)
arr[0][0] = -1
fish_dir[num] = -1

dfs(arr, (r, c), sd ,num, fish_dir )
print(answer)