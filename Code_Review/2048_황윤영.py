
"""
=================================== 2차 코드 리뷰 =========================
풀이 시간 1시간 33분
실행 시간 233ms
메모리 26MB


1008 문제 읽기 시작 + 주석으로 문제 정리
1011 루틴 정리했음 + 손설계 + 주석 정리
1032 구현시작
1044 디버깅 시작
    테케 안맞음 gravity index 수정
    gravity에서 좌우 이상하게 되는 것 확인. 행열 인덱스 실수 발견
    배엷 변화 보기 쉽게 하려고 printa 함수 만들어서 프린트 디버깅 쉽게 함
    배열 변화 보다가 가운데 뚫려있을 때는 merge안되는 것 확인하고 앞에 gravity 추가함
    change가 merge에 발생했을 때, gravity가 이뤄지지 않는 경우 있음. 수정

    여기까지는 틀린게 잘 발견돼서 고쳤는데
    다 고치고도 틀리고 찾기 어려워짐.. 리셋
1127 리셋 후 재작성

1144 정답

피드백 : 처음 보다 못한 풀이 / 시간 / 실수 ..
1차 풀이보다 무려 50분가량 더 오래 풀었다.
또 디버깅에 매몰되어 빠져들다가 팀원들끼리 새로 기출 풀 때는 1시간 잡고 리셋하는 연습을 하기로 한게 떠올랐다.
비록 1시간 20분이나 됐었고, 대부분이 잘 돌아가서 조금만 더 ? 라는 생각이 들었지만 과감하게 리셋
13분만에 구현해서 정답처리됐다. 코드 비교해서 틀린 부분 다시 찾아보자 ..

- 개선할 점
    - 실수 가득한 코드 디버깅에 매몰되지 않기. 리셋 연습 시급
    - 코드 개선해보려다 큰 코 다칠 뻔 !
        한번에 숫자 합치고 gravity하려다가 숫자 사이에 0이 있는데 merge가 되는 경우 놓침
        새로운 설계를 할 거였으면 똑바로 꼼꼼하게 체크했어야했다.
    - 루틴 중 또 다른 테케 생각해보기 저어어엉ㄴ혀 못함 ..
    - 새로 받아드린 중력 템플릿을 사용하던 부분에서 에러가 났을 것으로 보인다.
        새로운 배열 만들기 싫어서 기존 배열에서 하려고 했는데 이게 서툴었던 것 같다.
        이 템플릿 사용하려면 무조건 새로운 배열 써야겠다. (이게 더 구현 쉬워서 이걸로 쓸 예정)


"""

"""
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 : 딱히 없음
5. 종이에 손설계 ok
6. 주석으로 구현할 영역 정리 ok
7. 구현 ok
8.테스트케이스 단계별 디버깅 확인 ok
9. 예외될 상황 테스트케이스 만들어서 확인 no
10. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! so..so.. (1시간 20분에 리셋)

Debugging CheckPoint
- N, M / 행 열 index 오타 실수 점검
- max, min 구할 때 초기값 체크
- 배열 사용 목적 확인 후 배열 변수 실수 확인
- 조건분기문 복사한 경우 모두 바꿨는지 체크
- 디버깅해서 바꾼 코드 부분 혹은 로직이 있다면 그 부분 중심으로 전반적으로 재점검
- 문제 조건 + 코드 로직 같이 따라가며 이상한 로직 없는지 점검
- 로직이 맞는데 답이 이상하다면 아주 사소한 순서 문제는 없을지 점검

Reset Timing
- 1시간 ~ 1시간 반 : 코드 다 짰는데 테케 정답이 엉망진창? 
    문제 이해 미흡, 설계 미흡일 확률 높으므로 문제 다시 읽고 리셋할 모듈 찾을지 전체 리셋할지 판단하기
- 1시간 반 쯤에 코드 대부분이 잘 돌아가는데 특정 포인트에서 안되는 것 같다?
    - 특수한 테케가 있는지 1차로 점검해보고 디버깅 
    - 오타 찾아야할 것 같다 => 그냥 리셋해버리자 



 4 * 4 격자 안에서 이루어지는 게임
  상하좌우 중 한 방향을 정하게 되면, 모든 숫자들이 해당 방향으로 전부 밀리게 됩니다.

같은 숫자끼리 만나게 되는 경우 두 숫자가 합쳐지게 됩니다
단 한 번의 중력작용으로 이미 합쳐진 숫자가 연쇄적으로 합쳐지진 않습니다.
세 개 이상의 같은 숫자가 중력작용 방향으로 놓여 있으면, 중력에 의해 부딪히게 될 벽(바닥)에서 가까운 숫자부터 두 개씩만 합쳐집니다.
바닥에 가까운 순서대로 한 쌍씩 짝을 이뤄 합쳐집니다.



출력
5번 움직인 이후에 격자판에서 가장 큰 값의 최댓값


"""

def printa(string, arr):
    print(f"===================={string}======================")
    for k in range(N):
        print(arr[k])
    print()


def gravity(i, arr):
    di, dj = DIR[i]
    st, ed, step = idx_dict[i]
    new_arr = [[0]*N for _ in range(N)]
    #gravity는 ed를 포함해야해
    if di:
        for c in range(N):
            #채울 지점
            idx = st
            for r in range(st, ed+step, step):
                if arr[r][c]==0:
                    continue
                new_arr[idx][c] = arr[r][c]
                idx+=step
    else:
        for r in range(N):
            idx = st
            for c in range(st, ed+step, step):
                if arr[r][c] ==0: continue
                new_arr[r][idx] = arr[r][c]
                idx+= step
    return new_arr



def merge_number(i, arr, mx):

    di, dj = DIR[i]
    st, ed, step = idx_dict[i]
    result = mx
    if di:
        for c in range(N):
            for r in range(st, ed, step):
                if arr[r][c] == arr[r+step][c]:
                    arr[r][c] *= 2
                    arr[r+step][c] = 0
                    result = max(arr[r][c], result)
    else:
        for r in range(N):
            for c in range(st, ed, step):
                if arr[r][c] == arr[r][c+step]:
                    arr[r][c]*=2
                    arr[r][c+step] =0
                    result = max(arr[r][c], result)
    return arr, result




def dfs(level, arr, mx):
    global answer
    if level == 5:
        answer = max(answer, mx)
        return

    for i in range(4):
        changed_arr = gravity(i, arr)
        changed_arr, new_mx =  merge_number(i, changed_arr, mx)
        changed_arr = gravity(i, changed_arr)
        dfs(level+1, changed_arr,new_mx)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, 1)
idx_dict = {0:(0, N-1, 1), 1:(N-1, 0, -1), 2:(N-1, 0, -1), 3:(0, N-1, 1)}
answer = 0
for i in range(N):
    for j in range(N):
        answer = max(arr[i][j], answer)
dfs(0, arr, 0)
print(answer)


"""
=================================== 1차 코드 리뷰 =========================================
1545 문제읽기 시작
1555 문제 이해 + 구상 완료
1631 구현 완료 후 제출 한번에 정답!!!! 오예!!!


풀이시간 : 46분

1차시도
실행시간 :620ms
메모리 : 117016kb

2차시도  : 시간 줄여보자
배열 복사를 활용해서 움직일 수 없는 상황엔 DFS를 더 돌지 않도록 해보기
실행시간 : 288ms
메모리 : 113964 kb
기존 코드 그렇게까지 더럽진 않으니까 !!!
가지고 있던 함수 최대한 활용해보기
dfs에서 for문 내에서 매개변수로 들고다니는 배열 복사+움직임
pull, merge함수 활용해서 변화된 부분 있는지 flag와 return 값 활용해서 확인 => 변화 없다면 더 움직이지 말기



========== 잘한 점 ==========
문제 꼼꼼히 읽어서 실수 없이 한번의 구현에 정답 !
dict활용해서 최대한 상하좌우 반복 if문 없이 구현하려고 노력함

======== 아쉬운 점 =============
시간 왜이렇게 오래걸렸을까
백트래킹과 동시에 최댓값을 찾거나 가지치기하는 방법 생각해보기 ^.^ ...

"""
def dfs(level, board):
    global answer
    if level == 5:
        #max 구하기
        for i in range(n):
            # print(board[i])
            answer = max(max(board[i]), answer)
        return
    move_flag = False
    for i in range(4):
        # 이 방향으로 밀어보기
        # 밀어서 결과 같으면(움직이는 칸 없으면) continue
        # 있으면 dfs에 그 배열 담아서 다음 go !
        tmp = [[0] * n for _ in range(n)]

        for k in range(n):
            tmp[k] = board[k][:]
        is_move = move(tmp, i)

        # for j in range(n):
        #     print(tmp[j])
        # print(is_move)
        # print("============================")
        if not is_move:
            continue
        dfs(level+1, tmp)

def pull(tmp,d,  st, ed, gap):
    result = False
    # 1. 해당 방향으로 빈칸 없이 내린다
    # 위아래 이동일 때(row가 작은단위)
    if d in [(-1, 0), (1, 0)]:
        for c in range(n):
            for r in range(st, ed, gap):
                if tmp[r][c] != 0:
                    continue
                # d의 반대방향으로 0이 아닐때까지 살피며 발견되는 순간 내리기
                result = True
                du, dv = r, c
                while 1:
                    du -= d[0]
                    dv -= d[1]
                    if du < 0 or dv < 0 or du >= n or dv >= n:
                        break
                    if tmp[du][dv] != 0:
                        tmp[r][c] = tmp[du][dv]
                        tmp[du][dv] = 0
                        break

    # 좌우 이동일 때(col부터 보기)
    else:
        for r in range(n):
            for c in range(st, ed, gap):
                if tmp[r][c] != 0:
                    continue
                # d의 반대방향으로 0이 아닐때까지 살피며 발견되는 순간 내리기
                result = True
                du, dv = r, c
                while 1:
                    du -= d[0]
                    dv -= d[1]
                    if du < 0 or dv < 0 or du >= n or dv >= n:
                        break
                    if tmp[du][dv] != 0:
                        tmp[r][c] = tmp[du][dv]
                        tmp[du][dv] = 0
                        break
    return result
def merge(tmp, d, st, ed, gap):
    result = False
    #상하 이동일때 (row부터)
    if d in [(-1, 0), (1, 0)]:
        for c in range(n):
            for r in range(st, ed, gap):
                #0이 아니면 윗칸과 비교 후 합치고 윗칸 0
                if tmp[r][c] ==0:
                    continue
                result = True
                du = r-d[0]
                dv = c-d[1]
                if du<0 or dv<0 or du>=n or dv>=n:
                    continue
                if tmp[r][c]==tmp[du][dv]:
                    tmp[r][c] *=2
                    tmp[du][dv]=0


    # 좌우 이동일 때(col부터 보기)
    else:
        for r in range(n):
            for c in range(st, ed, gap):
                # 0이 아니면 윗칸과 비교 후 합치고 윗칸 0
                if tmp[r][c] == 0:
                    continue
                result =True
                du = r - d[0]
                dv = c - d[1]
                if du < 0 or dv < 0 or du >= n or dv >= n:
                    continue
                if tmp[r][c] == tmp[du][dv]:
                    tmp[r][c] *= 2
                    tmp[du][dv] = 0
    return result
def move(tmp, i):
    d = dir[i] #중력의 방향
    st = d_dict[d][0]
    ed = d_dict[d][1]
    gap = d_dict[d][2]
    result1 = pull(tmp, d, st, ed, gap)
    #2. 중력 방향 기준 제일 아래쪽부터 윗칸과 비교 후 같으면 합친다.
        # 합쳤다면 윗칸 0으로 만든다
    result2 = merge(tmp, d, st, ed, gap)

    #3. 합치기 완료 후 다시 해당 방향으로 빈칸 없이 내린다.
    pull(tmp, d, st, ed, gap)
    return result1 or result2
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = (-1, 0), (0, -1), (1, 0), (0, 1)

d_dict = {(-1, 0): (0, n, 1), (1, 0):(n-1, -1, -1), (0, -1):(0, n, 1), (0, 1):(n-1, -1, -1)}
selected = [0]*5
answer = 0
dfs(0, arr)
print(answer)




# #dfs
# def gravity(d, arr):
#     di, dj = DIR[d]
#     st, ed, step = idx_dict[d]
#     cnt = 0
#     if di:
#         for c in range(N):
#             idx = st
#             for r in range(st, ed+step, step):
#                 if arr[r][c] ==0: continue
#                 arr[idx][c] = arr[r][c]
#                 if idx!= r:
#                     arr[r][c] = 0
#                     cnt += 1
#                 idx += step
#
#
#         # for k in range(N):
#         #     print(arr[k])
#         # print()
#
#     else:
#         for r in range(N):
#             idx = st
#             for c in range(st, ed+step, step):
#                 if arr[r][c] ==0: continue
#                 if idx != c:
#                     arr[r][idx] = arr[r][c]
#                     arr[r][c] = 0
#                     cnt+=1
#                 idx += step
#     return arr, cnt
#
# def dfs(level, arr, mx, bd):
#     global answer
#     # level 5일 때 return .
#     if level == 5:
#         # printa("완료 후 !! ", arr)
#         answer = max(mx, answer)
#         return
#     #상하좌우 중에 움직여보기
#     for i in range(4):
#         # if i==bd: continue
#         printa("움직이기 전 !!!!!!!!!!!!!!", arr)
#         changed_arr, change0 = gravity(i, arr)
#         #수 합치면서 mx 가져오기
#         changed_arr, new_mx, change1 = merge(i, changed_arr, mx)
#         #gravity
#         changed_arr, change2 = gravity(i, changed_arr)
#         printa(f"{DIR[i]}로 움직인 후 ", changed_arr)
#         # 움직임 없으면 다음 dfs 부르지 말자
#         # if change1 == 0 and change2 :
#         #     print("안움직였다 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#         #     continue
#         dfs(level+1, changed_arr, new_mx, i)
#
#
# #merge
# def merge(d, arr, mx):
#     result = mx
#     st, ed, step = idx_dict[d]
#     change = 0
#     di, dj = DIR[d]
#
#     if di:
#         for c in range(N):
#             for r in range(st, ed, step):
#                 if arr[r][c] ==0: continue
#                 if arr[r][c] == arr[r-di][c]:
#                     arr[r][c] *= 2
#                     arr[r-di][c] = 0
#                     result = max(arr[r][c], result)
#                     change+=1
#
#     else:
#         for r in range(N):
#             for c in range(st, ed, step):
#                 if arr[r][c] ==0: continue
#                 if arr[r][c] == arr[r][c+step]:
#                     arr[r][c] *= 2
#                     arr[r][c+step] =0
#                     result = max(arr[r][c], result)
#                     change+=1
#     return arr, result, change
#
#
#
# #gravity
#
#
# #입력 받기
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# idx_dict = {0:(0, N-1, 1), 1:(N-1, 0, -1), 2:(N-1, 0, -1), 3:(0, N-1, 1)}
# DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
# answer = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]>answer:
#             answer = arr[i][j]
# #함수 실행
# dfs(0, arr, answer, -1)
# #출력
# print(answer)