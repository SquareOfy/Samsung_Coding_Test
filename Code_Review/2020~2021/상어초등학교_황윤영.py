
"""
1차
풀이 시간 : 21분
시도 횟수 : 1회
실행 시간 :208ms
메모리 : 112436 kb

2차
풀이 시간 : 17분
시도 횟수 : 1회
실행 시간 : 212ms
메모리 : 112408kb



Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: sort쓰자 ! 어렵지 않군
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : 간단해서 바로함
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 할필요 ㄴㄴ
"""

"""
n * n 명의 학생
n * n 크기의 격자 모양으로 생긴 놀이기구에 순서대로 탑승
처음에는 놀이기구의 모든 칸이 비어져있습니다.

각 학생별로 좋아하는 학생이 정확히 4명씩 정해져 있습니다.
자기 자신을 좋아하는 학생은 없고, 동일한 학생에 대해 좋아하는 학생의 번호가 중복하여 주어지는 경우도 없습니다.

입력으로 주어진 순서대로 다음 조건에 따라 가장 우선순위가 높은 칸으로 탑승
항상 비어있는 칸으로만 이동합니다.

1. 격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로
2. 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 / 격자 벗어나는 경우는 비어있다고 간주 x
3. 그 중 행 번호가 가장 작은 위치로 갑니다.
4. 그 중 열 번호가 가장 작은 위치로 갑니다.

최종 점수는 모든 학생들이 탑승한 이후, 각 학생마다의 점수를 합한 점수
 각 학생의 점수는 해당 학생의 인접한 곳에 앉아 있는 좋아하는 친구의 수로 
 0 - 0
 1 - 1
 2 - 10
 3 - 100 
 4 - 1000
"""

def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N
#입력
N = int(input())
arr = [[0]*N for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
like_arr = [None]*(N*N+1)
for _ in range(N*N):
    num, *like_lst = map(int, input().split())
    like_arr[num] = like_lst
    # print(num, like_lst) ############ 입력 확인
    candi_lst =[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]: continue
            blank_cnt = 0
            like_cnt = 0
            for di, dj in DIR:
                du, dv = i+di, j+dj
                if oob(du, dv): continue
                if arr[du][dv] ==0:
                    blank_cnt+=1
                elif arr[du][dv] in like_lst:
                    like_cnt+=1
            candi_lst.append((like_cnt, blank_cnt, i, j))
    candi_lst.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

    r, c = candi_lst[0][2], candi_lst[0][3]
    arr[r][c] = num

answer = 0

for i in range(N):
    for j in range(N):
        cnt = 0
        num = arr[i][j]
        for di, dj in DIR:
            du, dv = i+di, j+dj
            if oob(du, dv): continue
            if arr[du][dv] in like_arr[num]:
                cnt+=1
        answer += int(10**(cnt-1))
print(answer)
"""
총 풀이시간 21분
2117 문제 읽기 시작 + 주석으로 문제 복사해갔다

2121 주석으로 구상
    문제가 다소 간단하고 절차가 명확해서 주석으로만 설계하는 걸로도 충분

2128 구현시작
    큰 막힘 없이 성공 ~!

피드백
     - 잘한점
        문제 긁어와서 주석에다 표기하며 설계한 것
     - 못한점
        처음에 만족도 총합 부분 문제 제대로 안읽어서 한번 수정함..


자리 정하기 규칙
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로
    자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
    그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


학생 순서대로 자리 정하기
1. 빈칸 중 인접한 칸의 좋아하는 학생 수 세기 + 빈칸 수 세기
2. 좋아하는 학생 수가 많은 칸대로 SORT + 빈칸 수 + 행렬 순
가장 앞 칸에 학생 넣기

위 과정 반복 ..


다 앉히고 만족도 구하기
인접 칸에 앉은 좋아하는 학생 수의 합

시간복잡도는?
N*N*NlogN
"""

dir = (-1, 0), (0, 1), (1, 0), (0, -1)
n = int(input())
arr = [[0]*n for _ in range(n)]
favorite = {}
for i in range(n**2):
    num, *lst = list(map(int, input().split()))
    favorite[num] = lst

    blank_lst = []
    #arr 탐색하면서 빈자리 넣기
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                blank = 0
                like = 0
                #상하좌우로 빈칸과 좋아하는 친구 세기
                for di, dj in dir:
                    du = i+di
                    dv = j+dj
                    if du<0 or dv<0 or du>=n or dv>=n:
                        continue
                    if arr[du][dv] ==0:
                        blank+=1
                    elif arr[du][dv] in lst:
                        like+=1
                blank_lst.append((like, blank, i, j))

    blank_lst.sort(key = lambda x:(-x[0], -x[1], x[2], x[3]))
    r, c = blank_lst[0][2], blank_lst[0][3]
    arr[r][c] = num

good = 0

for i in range(n):
    for j in range(n):
        lst = favorite[arr[i][j]]
        like = 0
        for di, dj in dir:
            du = i+di
            dv = j+dj
            if du<0 or dv<0 or du>=n or dv>=n:
                continue
            if arr[du][dv] in lst:
                like+=1
        if like>0:
            good+= 10**(like-1)


print(good)