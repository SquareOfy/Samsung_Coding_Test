"""
1차
풀이 시간 : 54분
시도 횟수 : 1회
실행 시간 : 303ms
메모리 : 34MB

1차
풀이 시간 : 36분
시도 횟수 : 1회
실행 시간 : 273ms
메모리 : 34MB

- 실수 모음
    - 프린트 디버깅 용 변수 겹쳐서 오류 다 고쳤는데 답 안나옴
        프린트용 변수는 잘 안쓰는 변수를 쓰거나 함수 활용하자..
    - 배열명 잘못 넣는 실수 * 2!!

"""
from collections import deque


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


def bfs(i, j, g_num):
    q = deque([(i, j)])
    n = arr[i][j]
    cnt = 0
    visited[i][j] = group_num
    lst = []

    while q:
        cr, cc = q.popleft()
        cnt += 1
        flag = False
        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv): continue
            if visited[du][dv]:
                continue
            if arr[du][dv] == n:
                q.append((du, dv))
                visited[du][dv] = g_num
            else:
                flag = True
        if flag:
            lst.append((cr, cc))
    return cnt, lst


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
answer = []


def calculate_score(a, b):
    cnt_sum = cnt_lst[a]+cnt_lst[b]
    line_cnt = line_arr[a][b] + line_arr[b][a]
    return cnt_sum*num_lst[a]*num_lst[b]*line_cnt



for i in range(4):
    # 예술 점수 구하기

    # 현재 배열에서 같은 그룹 구하기
    check_arr = [-1]
    visited = [[0] * N for _ in range(N)]
    num_lst = [-1]
    group_num = 0
    cnt_lst = [-1]
    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            num = arr[r][c]
            group_num += 1
            cnt, lst = bfs(r, c, group_num)
            cnt_lst.append(cnt)
            check_arr.append(lst)
            num_lst.append(num)
    line_arr = [[0]*(group_num +1) for _ in range(group_num+1)]
    for k in range(1, group_num+1):
        lst = check_arr[k]
        for r, c in lst:
            for di, dj in DIR:
                nr, nc = r+di, c+dj
                if oob(nr, nc): continue
                if visited[nr][nc]>k:
                    line_arr[k][visited[nr][nc]] += 1

    # for k in range(group_num+1):
    #     print(line_arr[k])
    # print("===========================")
    score = 0
    for a in range(1, group_num+1):
        for b in range(a+1, group_num+1):
            score += calculate_score(a, b)
    answer.append(score)
    if i == 3:
        break

    # 배열 회전하기
    tmp = [[0]*N for _ in range(N)]
    for t in range(N):
        tmp[t][N//2] = arr[t][N//2]
        tmp[N//2][t] = arr[N//2][t]

    tmp = list(map(list, zip(*arr)))[::-1]
    sub_tmp = [[] for _ in range(N//2)]
    for u in range(2):
        for v in range(2):
            sr, sc = (N//2+1)*u, (N//2+1)*v
            for t in range(N//2):
                sub_tmp[t] = arr[sr+t][sc:sc+N//2]
            sub_tmp = list(map(list, zip(*sub_tmp[::-1])))
            for t in range(N//2):
                tmp[sr+t][sc:sc+N//2] = sub_tmp[t][:]
    for t in range(N):
        arr[t] = tmp[t][:]


print(sum(answer))

"""
총 풀이시간 54분
실행시간 303ms
메모리 34MB

0903 문제 읽기 시작
    평소 문제 설명 외 예시를 흘려 읽는 습관이 있다는걸 느껴 주의하려고 노력
    중간에 문제풀이가 떠오르는 부분은 종이에 메모

0909 종이에 설계
    점수를 계산하기 위해 필요한 조건들을 잘 구해놓는게 중요하다 생각
    예술 점수를 구하는 것과 회전 두가지 파트를 크게 나누어 설계
    어떤 배열을 어떤 단계에서 만들어 놓을지 위주로(점수관련) 메모

0917 종이 설계한 내용 중 코드로 그대로 구현할 파트 주석으로 정리

0922 구현시작
    - 주석 부분을 코드 구현 부분에 가져와서 차근차근 구현함
    - 중간확인 명확하게 하려고 노력했음
    - 작은 사각형 4개 배열 복사/회전하는 과정에서 배열이름을 잘못 넣어 디버깅 조금 함
        배열 복사 후 / 회전 후 배열 프린트해보며 이상함 알아채고 수정

0957 테케 확인 후 제출 => 정답


피드백
    - 잘한 점
        이번 문제는 크게 실수가 없었다는 점에서 칭찬!!
        중간 확인을 꼼꼼히 한 덕분에 눈덩이 처럼 커지는 실수가 적었던 것 같다
    - 못한 점
        오타 있었던것..? 하지만 금방 찾았따 !! 잘햇따 !!!
==========================문제풀이 구상 =========================
1. 예술 점수 구하기
    1) BFS로 visited에 num 올려가며 그룹 표시하기
        여기서 아래 배열도 채울 수 있다(append로)

            해당 그룹의 칸 수
    2) visited 탐색하며 아래 배열 값 구하기
        - near_group_cnt = [[0] * (num+1) for _ in range(num+1)]
            그룹끼리 인접한 변의 개수
        - count_arr = [0] * (num+1)
            해당 그룹의 칸 수
        - num_arr = [0] * (num +1)
        - count_arr = [0] * (num+1)
    3) 조합 뽑아서 점수에 더하기
        - dfs 함수 (level, lst, idx)
            if level ==2:
                lst에 있는 애들 점수 구해서 score(전역)에 더하기
                :return
            for in range(idx, num+1)
                dfs(level, lst+[i], i+1)
    4) 점수 출력

2. 회전하기
    1). 새 배열 만들어서 십자가 옮기기
    2) 90도 반시계 회전
    3) 네 사각형 시계 회전해서 옮기기
    4) 배열 원본 배열에 붙이기

"""
from collections import deque

def oob(i, j):
    return i<0 or j<0 or i>=n or j>=n
def bfs(r, c, num):
    q = deque([(r, c)])
    visited[r][c] = num
    k = arr[r][c]
    while q:
        cr, cc = q.popleft()

        for di, dj in dir:
            du = cr+di
            dv = cc+dj

            if oob(du, dv) or visited[du][dv]:
                continue
            if arr[du][dv] == k:
                visited[du][dv] = num
                q.append((du, dv))

# - dfs 함수 (level, lst, idx)
#             if level ==2:
#                 lst에 있는 애들 점수 구해서 score(전역)에 더하기
#                 :return
#             for in range(idx, num+1)
#                 dfs(level, lst+[i], i+1)
def dfs(level, lst, idx):
    global score
    if level == 2:
        a, b = lst[0], lst[1]
        tmp = (count_arr[a]+count_arr[b])*num_arr[a]*num_arr[b]*near_group_cnt[a][b]
        # print("lst : ", lst)
        # print("tmp : ", tmp)
        score += tmp
        return
    for i in range(idx, num+1):
        dfs(level+1, lst+[i], i+1)

#입력받기
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dir = (-1, 0), (0, 1), (1, 0), (0, -1)
answer = 0
#1) BFS로 visited에 num 올려가며 그룹 표시하기
        # 여기서 아래 배열도 채울 수 있다(append로)
        # - num_arr = [0] * (num +1)
        # - count_arr = [0] * (num+1)
        #     해당 그룹의 칸 수
for i in range(4):
    visited = [[0]*(n) for _ in range(n)]
    num_arr = [0]
    num = 0
    for i in range(n):
        for j in range(n):
            #주변탐색하며 같은 그룹에 visited 표기
            if not visited[i][j]:
                num += 1
                bfs(i, j, num)
                num_arr.append(arr[i][j])

    #visited 그룹 분할 체크 완료 ########################
    # print(num)
    # for i in range(n):
    #     print(visited[i])
    # print()
    ######################################################3

    #     2) visited 탐색하며 아래 배열 값 구하기
    #         - near_group_cnt = [[0] * (num+1) for _ in range(num+1)]
    #             그룹끼리 인접한 변의 개수
    #         - count_arr = [0] * (num+1)
    #             해당 그룹의 칸 수


    near_group_cnt = [[0] * (num+1) for _ in range(num+1)]
    count_arr = [0] * (num + 1)
    for i in range(n):
        for j in range(n):
            group_num =visited[i][j]
            count_arr[group_num] += 1
            for di, dj in dir:
                du = i+di
                dv = j+dj
                if oob(du, dv):
                    continue
                near = visited[du][dv]
                if near != group_num:
                    near_group_cnt[group_num][near] += 1
#########################인접 개수, 그룹 개수 체크 완#################3
    # for i in range(num+1):
    #     print(near_group_cnt[i])
    # print()
    # print(count_arr)
    # print()
    #############################################

    # 3) 조합 뽑아서 점수에 더하기
    score = 0
    dfs(0, [], 1)
    answer += score
    # print(score)
    ### 0 회전 점수 체크 완

    # 2. 회전하기
    #     1). 새 배열 만들어서 십자가 옮기기

    new_arr = [[0]*n for _ in range(n)]
    new_arr[n//2] = arr[n//2][:] #가로 가운데 옮김
    for i in range(n):
        new_arr[i][n//2] = arr[i][n//2]

    #     2) 90도 반시계 회전
    new_arr = list(map(list, zip(*new_arr)))[::-1]

    ###########십자가 반ㅅ니계 체크 완 #############33
    # for i in range(n):
    #     print(new_arr[i])
    # print()

    ##############################################33


    #     3) 네 사각형 시계 회전해서 옮기기
    for i in range(0, n, n//2+1):
        for j in range(0, n, n//2+1):
            tmp = [[] for _ in range(n//2)]
            for k in range(n//2):
                tmp[k] = arr[i+k][j:j+n//2]

            tmp = list(map(list, zip(*tmp[::-1])))

            for k in range(n//2):
                new_arr[i+k][j:j+n//2] = tmp[k][:]

    # for i in range(n):
    #     print(new_arr[i])
    # print()
    #     4) 배열 원본 배열에 붙이기
    for i in range(n):
        arr[i] = new_arr[i][:]
print(answer)