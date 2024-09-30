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
