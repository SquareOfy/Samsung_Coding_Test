"""
1차
풀이 시간 : 1시간 1분
시도 횟수 : 2회
실행 시간 : 184 ms
메모리 :112196kb

2차
풀이 시간 : 1시간 20분
시도 횟수 : 코드트리 2회.... 백준 엄청 많이 ..
실행 시간 : 196 ms
메모리 : 112348kb

- 실수 모음
    - 경계값 실수
    - 오타
    - 냄새 없애기 순서 설계 미흡
    - 종료조건 순서 실수

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 독점구역 - 하는 순서 주의
    : 시작할 때도 독점하고 시작하는 것 주의
    : 방향벡터 인덱스 1 뺀거 주의
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : good
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : 깔끔하게 디버깅한듯
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""

"""
=================== 2차 리뷰 =========================
1056 문제읽기 + 주석정리
1059 설계시작
1112 구현시작 
1126 구현완료 디버깅 시작
    인덱스 에러 -> 방향 담는 lst 마진 빼먹은 것 발견
    답이 안맞아서 turn 제한 두는 브레이크 만들어서 프린트 디버깅
    pr_함수 만들어서 사용함 => 깔끔해서 편했음 
    플레이어 이동 안하는 문제 발견. 조건문에 오타 발견해서 수정
    
    cnt_arr 리셋될 때 3차원 인덱스 누락한 것 발견해서 코드트리 정답
1141 코드트리 정답 . 근데 백준 왜 오답?
    조건 다시 읽어봄
    아무리 생각해도 내가 맞는데,, 싶음
    모든 테케도 다 맞고 ,, 
    그래서 그림이랑 다시 비교. 이것도 너무 똑같고 잘 동작한다. 
    상어가 빈칸 못찾았을 때 자기 냄새 있는 칸으로 갈 때는 굳이 다른 상어 만날 일 없어서
    그냥 갔는데 그게 문젠가 싶어서 건드려봄. 역시 아님; 
    그럼 다시 .. 뜯어보다가 하안참 뒤에 경계값 의심; 
    1000보다 클 때 -1 출력하는 걸 밑에서 처리하니까 정답 ㅠㅠ 힝 
    정답 되고 나서 위에서 추가한 로직 지우니 역시 맞았다 . 필요없는게 맞아 .. 
    
"""



"""
n * n 격자칸 ,  m개의 플레이어로 구성

턴이 한 번 진행될 때 각 플레이어들은 한 칸씩 이동
해당 칸에 이동했을 때 플레이어는 해당 칸을 독점 계약하게 됩니다.
초기 상태에 위치한 땅 역시 해당 플레이어의 독점 계약한 칸

각 플레이어는 각 방향별로 이동 우선순위
본인에게 인접한 상하좌우 4 칸 중 아무도 독점계약을 맺지 않은 칸으로 이동
만약 그러한 칸이 없을 경우에는 인접한 4방향 중 본인이 독점계약한 땅으로 이동합니다.
이동할 수 있는 칸이 여러개일 수 있음으로 이동 우선순위에 따라 움직일 칸을 결정

 플레이어가 보고 있는 방향은 그 직전에 이동한 방향

 ############임시배열 만들기
 모든 플레이어가 이동한 후 한 칸에 여러 플레이어가 있을 경우에는
 가장 작은 번호를 가진 플레이어만 살아남고 나머지 플레이어는 게임에서 사라지게 됩니다.

 출력 1번 플레이어만 살아남기까지 걸린 턴의 수
  답이 1000 이상이거나 불가능한 경우에는 -1
  

"""

# dir 번호 감소 함수
def change_dir_idx(i):
    return int(i) - 1


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N

def pr_arr(string, arr):
    print(f"====================={string}===================")
    print("=======================arr=======================")
    for i in range(N):
        print(arr[i])
    print("================================================")
    print()
def pr_cnt_arr(string):
    print(f"====================={string}===================")
    print("=======================cnt_arr=======================")
    for i in range(N):
        print(cnt_arr[i])
    print("================================================")
    print()
# 입력
N, M, K = map(int, input().split())

# 필요배열 준비
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (-1, 0), (1, 0), (0, -1), (0, 1)
player_dir_lst = [-1]+list(map(change_dir_idx, input().split())) # 초기방향
priority_info = [-1]
for m in range(M):
    p_lst = [list(map(change_dir_idx, input().split())) for _ in range(4)]
    priority_info.append(p_lst)
cnt_arr = [[[0] * 2 for _ in range(N)] for _ in range(N)]  # 독점 횟수 cnt할 배열
turn = 0
cnt = M
# while 문
while 1:
    # 내 자리 독점하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue
            cnt_arr[i][j] = [arr[i][j], K]
    # pr_cnt_arr("냄새 뿌린 후 ")

    # 종료조건
    if cnt == 1:
        break
    if turn > 1000:
        break
    # 턴 추가
    turn += 1
    tmp = [[0] * N for _ in range(N)]
    # arr 돌면서 플레이어 이동(tmp 생성)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0: continue  # 플레이어 없으면 지나가기
            n = arr[i][j]
            my_d = player_dir_lst[n]
            # 내 우선순위 방향 배열 찾아오기
            dir_lst = priority_info[n][my_d]

            # 빈칸 찾기 : 이동 시 사람 있으면 대소비교 cnt -=1
            for d in dir_lst:
                di, dj = DIR[d]
                du, dv = i + di, j + dj
                if oob(du, dv): continue
                if cnt_arr[du][dv] != [0, 0]: continue
                # 빈칸이면 가보기
                # tmp에 이미 누군가가 있다면?
                if tmp[du][dv]:
                    cnt -= 1
                    if n < tmp[du][dv]:
                        tmp[du][dv] = n
                        player_dir_lst[n] = d
                else:
                    tmp[du][dv] = n
                    player_dir_lst[n] = d
                break
            # 빈칸 없으면 내자리 찾기 : 이동 시 사람 있으면 대소비교 cnt -=1
            else:
                for d in dir_lst:
                    di, dj = DIR[d]
                    du, dv = i + di, j + dj
                    if oob(du, dv): continue
                    if cnt_arr[du][dv][0] == n:
                        tmp[du][dv] = n #다른 놈이 와있을리 없으니 그냥 내가 가기
                        player_dir_lst[n] = d
                        break
                else:
                    tmp[du][dv] = n
    # pr_arr("이동 완료 후" , tmp)
    # print(player_dir_lst)
    # 이동 완료 후 기존 cnt배열 감소시키기
    for i in range(N):
        for j in range(N):
            if cnt_arr[i][j][0]!=0:
                cnt_arr[i][j][1]-=1
                if cnt_arr[i][j][1]==0:
                    cnt_arr[i][j] = [0, 0]
            if tmp[i][j] !=0:
                cnt_arr[i][j] = [tmp[i][j], K]

    # tmp에 사람 있으면 갱신하기
    for i in range(N):
        arr[i] = tmp[i][:]


print(turn if turn < 1001 else -1)
"""
1644 약 2시간 새로운게임2에 시달리고 너덜너덜해져서 들어온 아기상어
    - 맘급해짐 평정심 유지해야해,,
    - 문제 후다닥 읽고 구현시작
    - 그래도 사전에 문제 고를 때 대략 어떤 방식으로 구현하면 되겠다 생각해둔 게 잇어서
    - 비교적 문제가 빨리 읽혔고 설계가 됐다
1646 구현시작
    움직임 동시에 하는거 tmp 배열 생각함(이번엔 요 포인트론 실수 안함)
    냄새 없는 것 우선 -> 나와 동일한 것 우선 그래도 없으면 그대로 위치를 for-else로 구현

1714 구현 전반적으로 완료 후 테케 테스트 했는데 안맞음. 디버깅 시작
    1001번이나 돌아서 프린트 디버깅이 쉽지 않아 answer>10일 때 break 걸었음
    주석으로 #길게 표시해서 잊지 않고 지우려고 노력
    움직일 때마다 상어 위치 그림이랑 비교하며 잘못 움직인 상어있나 찾아봄
    상어 1번의 이동만 보려고 프린트를 찍어도 안나와서 당황
    d 변수 겹치는 것 발견하고 고침
    요상하다 왜 왜왜 이상하게 이동하지: 배열명, 인덱스 등등 쭈욱 점검
    하도 찾아봐도 안보여서 이번엔 냄새배열 확인 ;
        =>이동 후 냄새 반영하는 과정에서 에러 발견
        냄새가 있는 곳을 없다 하고 가는 것 확인
        초기 상어 위치에서 냄새를 안뿌린 것 확인 + 방금 상어가 이동해서 옮긴 곳은 K 감소 안시켜야함을 깨달ㅇ므

1742 버저비터를 기대하고 제출했으나 25퍼에서 틀림
    뭐가 문젤까 난 맞는데,, 하고 고민하다가
    처음부터 1번상어만 있을 때는 바로 끝나야함을 생각
    answer +=1 타이밍 바꿔서 제출
1745 정답


피드백
- 못한점
    올거면 더 빨리 이문제로 왔어야했다
    평정심 찾지 못했다 . 급할수록 침착하자. 그럼 버저비터는 했을것.
- 잘한점
    while 문 규모 너무 커서 break걸어서 프린트 디버깅하고 잊지 않고 지우기 위해
    주석으로 길게 표시한건 잘했다..


"""

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

directions = (0, 0), (-1, 0), (1, 0), (0, -1), (0, 1) #상어 우선순위 보고 여기서 뽑아오기
shark_order = []
smell_arr = [[[0]*2 for _ in range(N)] for _ in range(N)] #상어 번호, k
shark_direction = [0]+list(map(int, input().split()))

shark_order.append([])
for i in range(1, M+1):
    tmp = [[]]
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    shark_order.append(tmp)

answer = 0
cnt = M

while 1:

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                smell_arr[i][j] = [arr[i][j], K]
    if cnt ==1 or answer >1000:
        break
    answer += 1
    # if answer >= 10 :
    #     break
    #움직임 동시에
    move = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # print(arr[i][j])
            if arr[i][j]==0:
                continue
            num = arr[i][j]
            dk = shark_direction[num]
            dir_lst = shark_order[num][dk]
            non_flag = False

            #냄새 없는 것 우선 찾기
            for d in dir_lst:
                di, dj = directions[d]
                du = i+di
                dv = j+dj
                if du<0 or du>=N or dv<0 or dv>=N:
                    continue
                if smell_arr[du][dv][0] !=0:
                    continue

                #여기로 이동
                if move[du][dv]!=0:
                    if move[du][dv]>num:
                        #내가이겨먹음
                        move[du][dv] = num
                    cnt -= 1
                else:
                    move[du][dv] = num
                shark_direction[num] = d
                break
            else:

                #냄새 없는 곳 없으면 나랑 같은 거라도 찾아
                for d in dir_lst:
                    di, dj = directions[d]
                    du = i + di
                    dv = j + dj
                    if du < 0 or du >= N or dv < 0 or dv >= N:
                        continue
                    if smell_arr[du][dv][0] != num:
                        continue

                    # 여기로 이동
                    if move[du][dv] != 0:
                        if move[du][dv] > num:
                            move[du][dv] = num
                        cnt -= 1
                    else:
                        move[du][dv] = num
                    shark_direction[num] = d
                    break
                else:
                    #그것도 못찾음?
                    #이동불가
                    move[i][j] = num #원래 위치로!
    #################

    ##################3333
    #이동을 마쳤으니 move를 smell과 arr에 반영하자
    for i in range(N):
        arr[i] = move[i][:]
        for j in range(N):
            if arr[i][j] ==0 :
                continue
            smell_arr[i][j] = [arr[i][j], K]
    # print("==================move 이동 ================")
    # for i in range(N):
    #     print(arr[i])

    #이동을 마쳤으니 smell을 깎자
    for i in range(N):
        for j in range(N):
            if smell_arr[i][j][0] == 0:
                continue
            if arr[i][j] !=0:
                continue
            smell_arr[i][j][1] -= 1
            if smell_arr[i][j][1]==0:
                smell_arr[i][j][0] = 0
    # print("======================그때의 smell =============")
    # for i in range(N):
    #     for j in range(N):
    #         print(smell_arr[i][j])
    #     print()
print(answer if answer <1001 else -1)
