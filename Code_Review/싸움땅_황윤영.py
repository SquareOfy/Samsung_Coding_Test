"""
1차
풀이 시간 : 2시간 20분
시도 횟수 : 겁나겁나 많이많이
실행 시간 : 189 ms
메모리 : 25MB

2차
풀이 시간 : 1시간 + 20분 + 리셋하다가 정정 23분
시도 횟수 : 3회
실행 시간 : 171ms
메모리 : 26MB

- 실수 모음 
    - 변수 잘못 씀
    - 동일 로직 복사했다가 변수 수정 덜함
    - 조건문 누락 후 추가했다가 인덴트 실수
    - 로직 흐름 놓침
        (이동 후 INFO 반영 순서 늦게 해서 내가 이동 후 졌을 때 
        내 바뀐 위치가 아닌 기존위치에서 방향 탐색후 이동하게 됨; )
    - 힙큐 잘못 사용
"""

# def oob(x, y):
#     return x<0 or y<0 or x>=N or y>=N
#
# N, M, K = map(int, input().split())
# DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
#
# gun_arr = [[[] for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     guns = list(map(int, input().split()))
#     for j in range(N):
#         if guns[j] == 0: continue
#         gun_arr[i][j].append(guns[j])
#
# player_arr = [[0]*N for _ in range(N)]
# gun_lst = [0]*(M+1)
# player_info = [-1]
# player_power_lst = [-1]
# point_lst = [0]*(M+1)
#
# for m in range(M):
#     x, y, d, s = map(int, input().split())
#     x -= 1
#     y -= 1
#
#     player_info.append((x, y, d))
#     player_arr[x][y] = m
#     player_power_lst.append(s)
#
#
# for k in range(K):
#
#     #player 이동
#     for m in range(1, M+1):
#         #기존 위치, 방향
#         x, y, d = player_info[m]
#         di, dj = DIR[d]
#         du, dv = x+di, y+dj
#         #기존 위치 해제
#         if oob(x, y): #벽만나면 반대로 한칸, 방향 바꿈
#             d=(d+2)%4
#             du -= di*2
#             dv -= dj*2
#
#         #이동한 곳에 사람이 없으면
#         if player_arr[du][dv] == 0:
#             if gun_arr[du][dv]: #총 있으면 내가 가진거랑 비교해서 주울거야
#                 if gun_lst[m]:
#                     gun_arr[du][dv].append(gun_lst[m])
#                     gun_lst[m] = 0
#                 gun_arr[du][dv].sort()
#                 gun_lst[m] = gun_arr[du][dv].pop()
#         else: #사람 있으면 싸울거야
#             your_num = player_arr[du][dv]
#             your_power = player_power_lst[your_num] + gun_lst[your_num]
#             my_power = player_power_lst[m] + gun_lst[m]
#
            # => 여기서 리셋하면서 다시 풀다가 틀린 거 번뜩 알 것 같아서 기존 코드 고쳐봄 정답. .

"""

초기에는 무기들이 없는 빈 격자에 플레이어들이 위치하며 각 플레이어는 초기 능력치를 가짐


1. 이동
    첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동
    해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동

2. 도착 -> 총 줍기 또는 싸움
     이동한 방향에 플레이어가 없다면 총을 획득
     플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는 총 가운데
     공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.

    이동한 방향에 플레이어가 있는 경우
    해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
    이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리

    이긴 플레이어
        각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로
        승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득
        기존 총은  해당 격자에 내려 놓습니다.

    진 플레이어
        본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동
        만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는
        오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동
        이동 후, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.

k 라운드 동안 게임을 진행하면서 각 플레이어들이 획득한 포인트를 출력

"""

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def printa(string, arr):
    print(f"================{string}===============")
    for i in range(N):
        print(arr[i])
    print("============================================")
    print()
N, M, K = map(int, input().split())
gun_arr = [[[] for _ in range(N)] for _ in range(N)]

for r in range(N):
    lst = list(map(int, input().split()))
    for c in range(N):
        if lst[c] == 0: continue
        gun_arr[r][c].append(lst[c])

player_arr = [[0]*N for _ in range(N)]
player_loc_lst = [-1]
player_power_lst = [-1]
player_dir_lst = [-1]
player_gun_lst = [0]*(M+1)
point_lst = [0]*(M+1)

DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

for m in range(1, M+1):
    x, y, d, s = map(int, input().split())
    x -= 1
    y -= 1
    player_arr[x][y] = m
    player_loc_lst.append((x, y))
    player_dir_lst.append(d)
    player_power_lst.append(s)
# printa("초기 플레이어위치 ", player_arr)
# print("gun : ", player_gun_lst)
# print("dir : ", player_dir_lst)
# print("loc : ", player_loc_lst)
for k in range(K):

    # print(f"===============================k : {k} ==========================")
    for i in range(1, M+1):
        x, y = player_loc_lst[i]
        d = player_dir_lst[i]
        di, dj = DIR[d]
        du, dv = x+di, y+dj
        if oob(du, dv):
            d = (d+2)%4
            du -= di*2
            dv -= dj*2
        player_arr[x][y] = 0
        player_loc_lst[i] = (du, dv)
        player_dir_lst[i] = d
        #사람 없으면 총 줍기
        if not player_arr[du][dv]:
            #총 있으면
            if gun_arr[du][dv]:
                if player_gun_lst[i]:
                    gun_arr[du][dv].append(player_gun_lst[i])
                gun_arr[du][dv].sort()
                mx = gun_arr[du][dv].pop()
                player_gun_lst[i] = mx

            #이동하기

            player_arr[du][dv] = i

            # print("=================i : ", i, "======================")
            # printa("이동했다 !! ", player_arr)
            # print("gun : ", player_gun_lst)
            # print("dir : ", player_dir_lst)
            # print("loc : ", player_loc_lst)
        else: #사람 있으면 싸워
            # print(f"{du}, {dv}에서 싸울거야 !!!!!!!!!!!!")
            my_power = player_power_lst[i]+player_gun_lst[i]
            your_num = player_arr[du][dv]
            your_power = player_power_lst[your_num]+player_gun_lst[your_num]
            # print("=================i : ", i, "======================")
            # printa("싸웠다 !! ", player_arr)
            # print("상대편 : ", your_num)
            # print("gun : ", player_gun_lst)
            # print("dir : ", player_dir_lst)
            # print("loc : ", player_loc_lst)
            #승패 가리기
            if my_power>your_power:
                winner = i
                loser = your_num
            elif my_power<your_power:
                winner = your_num
                loser = i
            else:
                if player_power_lst[i] < player_power_lst[your_num]:
                    winner = your_num
                    loser = i
                else:
                    winner = i
                    loser = your_num

            #점수 더해주기
            point_lst[winner] += abs(my_power-your_power)
            # print("power : ", player_power_lst)
            # print("gun : " , player_gun_lst)
            # print("winner : ", winner)
            # print("loser : ", loser)
            # print("mypower : ", my_power)
            # print("yourPower : ", your_power)
            # print(point_lst)

            #패자 되돌아가기
            #총 있으면 내놔
            if player_gun_lst[loser]:
                gun_arr[du][dv].append(player_gun_lst[loser])
            player_gun_lst[loser] = 0
            loser_d = player_dir_lst[loser]
            lnr, lnc = du, dv
            #되돌아가. 안돼면 4방 탐색해
            for t in range(4):
                nd = (loser_d+t)%4
                ldi, ldj = DIR[nd]
                lnr, lnc = du+ldi, dv+ldj
                if oob(lnr, lnc) or player_arr[lnr][lnc]:
                    continue
                #이동하기
                player_loc_lst[loser] = (lnr, lnc)
                player_dir_lst[loser] = nd
                player_arr[lnr][lnc] = loser
                break
            if gun_arr[lnr][lnc]:
                gun_arr[lnr][lnc].sort()
                player_gun_lst[loser] = gun_arr[lnr][lnc].pop()
            if gun_arr[du][dv]:
                #승자 총줍기
                if player_gun_lst[winner]:
                    gun_arr[du][dv].append(player_gun_lst[winner])
                gun_arr[du][dv].sort()
                mx = gun_arr[du][dv].pop()
                player_gun_lst[winner] = mx
            player_loc_lst[winner] = (du, dv)
            player_arr[du][dv] = winner

            # printa("싸웠다 !! ", player_arr)
            # printa("총 보자 ! ", gun_arr)
            # print("gun : ", player_gun_lst)
            # print("dir : ", player_dir_lst)
            # print("loc : ", player_loc_lst)

print(*point_lst[1:])

"""
코드리뷰
풀이 시간 : 2시간 20분
실행시간 : 189 ms
메모리 : 25MB

0904 문제 읽기 시작
    루틴대로 1회독 정독 (문제 길고 중간에 애매한 말 생각하느라 8분가량 걸림)
    문제 내용 그대로 구현할 위치에 주석으로 정리

0920 입력 받기 + DIR 같은 함수 입력 + 문제에 사용되는 값들 어떤 자료구조로 놓고 쓸지 설계
    손으로 슈더코드 설계

0927 구현시작
    왜 힙큐를 쓰려고 했을까 ㅎ ㅏ 영상 보면서도 진짜 왜 저랬지 싶다 .....
    ㅇ ㅏ .......................................................

0955 구현완료 디버깅 시작
    1. 테케 안맞음
        PLAYER 이동할 때 딕셔너리서 꺼낸 정보 1차적으로 확인
        dict 정보 안바뀌는 것 확인. 값 변경 안해줬구나 생각나서 수정
    2. 또 안맞음. dict 꺼내서 확인해보고 싸울 때 dict 갱신 문제인거 확인
        싸울 때 loser가 누구냐에 따라 갱신 되는게 달라짐
        dict 변경 싸울 때와 아닐 때 각각 다르게 변경
    3. 또 안맞아 ^^ player_arr 출력해보고 player_arr 값 이동할 때 안비워준 거 확인
        진짜 바부탱
    4. 테케 6번 안맞다. 작은 테케 찾아서 확인해보자
        문제 조건과 같이 다시 코드 보기 + arr 출력해보기 하다보니 0이 왜나오나 싶었다
        arr 값 세팅할 때 0 안넣기 + player가 총 안가지고 있을 때는 arr에 넣지 않기 처리 등을 추가로 해줌
    5. 그래도 안맞다
        단계별, player별 출력해서 봤다 (사실 위에서도 이렇게 봄)
        싸울 때, 그리고 현재 움직인 player가 졌을 때 패배자의 이동방향이 틀림을 알고
        패자 승자 각각 누군지 결정해서 winner, loser에 넣는 if문에서 조정해줬다
    6. 그.래.도. 6.번.이.문.제.다
        이 때부터 좀 초조해짐..
        코드 뜯어봐도 문제가 안보여서(문제가 없을리가 ...........)
        테케 다양하게 찾아가며 넣어보고 테스트하려했지만 디버깅으로 따라가기엔 다소 큰 테케들..
        한 놈이 딱 1 크길래 그 근방을 디버거로 살펴봄
        유의미하진 않았음. 무승부가 나왔어야할 것 같은데 그 총을 가지게 된 순간을 찾기도 어렵고
        찾는다 해도 그 총이 어쩌다 그 위치로 잘못 오게됐는지를 모두 알기는 어려웠다.

        이 멍청한 디버깅 반복하다가 2시간이 돼서 5분 휴식
        5분동안 이 디버깅 그만하자. 저 테케 그만보자 생각함. 어차피 한시간 내내 이 테케로 봐도 못잡겠다 싶었다.
        지난번 큰 테케로 고생할 때, 사실 예제로도 잡을 수 에러였다는 걸 알았던게 5분 쉬는 동안 생각남
        그냥 문제 조건과 내 코드와 상이한 부분이 있는지 보고 그 다음
        예제로 주어진 테케 (그림까지 있으니까)로 진짜 모든게 정상 동작하는지 살펴보자 생각

        다시 디버깅 시작
        일단 코드 뜯어봄 . 문제 없어보인다. 문제를 잘못이해했나 고민해봐도 맞는 것 같다
        예제 테케로 디버깅 시작
        문제에서 한 칸에 1, 2가 있는 case가 있는데 난 없다?
        왜지? 꺼내오는 총 출력해보니 2를 꺼내온다. 3을 꺼내와야하는데.
        왜지? 하다가.........불현듯..... 아 heapq는 ..........최소구나. ..
        아 ...........맞ㅈ지..........................함

        수정. ..
        다 수정 못하고 제출해서 또 틀리고 마저 수정해서 제출

1123 정답

피드백
- 잘한 점
    루틴대로 문제 1회독 / 주석 복사
        => 구현 과정에서 덜렁대긴 했으나, (0은 arr에 안넣기 등)
            빠르게 찾을 수 있었다.
- 못한 점
    나 왜 힙큐 몰라 ..? 왜 저렇게 써 .............?
    바본가 ....................원인 알자마자 자괴감 밀려왔다
    핑계를 대자면 자바에선 뭘 쓸 때 어떤 동작인지 똑바로 생각하고 쓰자 ;

    멍청한 디버깅을 30분 넘게 했다 .. 빠른 상황판단 필요
"""
"""
플레이어 N*N 배열에 위치 넣기
플레이어 위치에 그 플레이어의 번호 넣기
플레이어의 방향과 초기 능력치는 dict로 관리  key : num // value : (x, y, 방향, 초기 능력치)

gun = 플레이어가 현재 들고 있는 총의 공격력
point = 플레이어별 획득한 포인트 ( 출력 배열)



"""

def oob(x, y):
    return x < 0 or y < 0 or x >= N or y >= N

# ↑, →, ↓, ←
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
# 입력
# 첫 번째 줄에 n, m, k가 공백을 사이에 두고 주어집니다.
# n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수를 의미합니다.
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
player_arr = [[0] * N for _ in range(N)]
player_dict = {}
point = [0] * (M + 1)
gun = [0] * (M + 1)

# n개의 줄에 걸쳐 격자에 있는 총의 정보가 주어집니다
# 숫자 0은 빈 칸, 0보다 큰 값은 총의 공격력
# 3차원으로 만들기
# arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if lst[j] == 0: continue
        arr[i][j].append(lst[j])

#  m개의 줄에 걸쳐 플레이어들의 정보 x, y, d, s가 공백을 사이에 두고 주어집니다
# (x, y)는 플레이어의 위치, d는 방향, s는 플레이어의 초기 능력치를 의미
#  방향 d는 0부터 3까지 순서대로 ↑, →, ↓, ←을 의미
for i in range(1, M + 1):
    x, y, d, s = map(int, input().split())
    x -= 1
    y -= 1
    player_dict[i] = (x, y, d, s)
    player_arr[x][y] = i

# 플레이어의 초기 위치에는 총이 존재하지 않습니다.


# 라운드
for k in range(K):
    #  첫 번째 플레이어부터 순차적으로 본인이 향하고 있는 방향대로 한 칸만큼 이동합니다
    # 해당 방향으로 나갈 때 격자를 벗어나는 경우에는 정반대 방향으로 방향을 바꾸어서 1만큼 이동
    for i in range(1, M + 1):
        x, y, d, s = player_dict[i]
        player_arr[x][y] = 0
        di, dj = DIR[d]
        if oob(x + di, y + dj):
            d += 2
            d %= 4
            di, dj = DIR[d]
        nx, ny = x + di, y + dj
        # print("다음 위치 : ", nx, ny)
        # 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸우게 됩니다.
        # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다
        # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
        # 각 플레이어의 초기 능력치는 모두 다릅니다.

        if player_arr[nx][ny]:
            enemy_num = player_arr[nx][ny]
            enemy_power = player_dict[enemy_num][3] + gun[enemy_num]
            my_power = s + gun[i]

            if enemy_power < my_power or (enemy_power == my_power and player_dict[enemy_num][3] < s):
                winner = i
                loser = enemy_num
                player_dict[i] = (nx, ny, d, s)
                player_arr[nx][ny] = winner
                loser_d = player_dict[loser][2]
                loser_s = player_dict[loser][3]
            else:
                winner = enemy_num
                loser = i
                loser_d, loser_s = d, s

            # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득

            point[winner] += abs(enemy_power - my_power)  # 점수획득

            #  진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다.
            # 총내려놓기
            if gun[loser]:
                arr[nx][ny].append(gun[loser])
                arr[nx][ny].sort()
            gun[loser] = 0

            # 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는
            # 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동합니다.
            #  해당 칸에 총이 있다면,
            #  해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
            # ?????????이동한 후 칸이군
            # 회전하며 빈칸 탐색
            for t in range(4):
                new_d = (loser_d + t) % 4
                di, dj = DIR[new_d]
                if oob(nx + di, ny + dj) or player_arr[nx + di][ny + dj]:
                    continue
                player_dict[loser] = (nx + di, ny + dj, new_d, loser_s)
                player_arr[nx + di][ny + dj] = loser

                # 가장 높은 총 얻기
                if arr[nx + di][ny + dj]:
                    gun[loser] = arr[nx + di][ny + dj].pop()
                break


            # . 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중
            # 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.

            if arr[nx][ny]:
                mx_gun = arr[nx][ny].pop()
                if gun[winner]:
                    arr[nx][ny].append(min(mx_gun, gun[winner]))
                    arr[nx][ny].sort()
                gun[winner] = max(mx_gun, gun[winner])



        #  만약 이동한 방향에 플레이어가 없다면 해당 칸에 총이 있는지 확인합니다.
        # 총이 있는 경우, 해당 플레이어는 총을 획득합니다.
        # 플레이어가 이미 총을 가지고 있는 경우에는 놓여있는 총들과 플레이어가 가지고 있는
        # 총 가운데 공격력이 더 쎈 총을 획득하고, 나머지 총들은 해당 격자에 둡니다.
        else:
            if arr[nx][ny]:
                if gun[i] == 0:
                    gun[i] = arr[nx][ny].pop()
                else:
                    mx_gun = arr[nx][ny].pop()
                    arr[nx][ny].append(min(gun[i], mx_gun))
                    arr[nx][ny].sort()
                    gun[i] = max(mx_gun, gun[i])
            player_arr[nx][ny] = i
            player_dict[i] = (nx, ny, d, s)


    # k 라운드 동안 게임을 진행하면서 각 플레이어들이 획득한 포인트
print(*point[1:])