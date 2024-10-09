"""
1차
풀이 시간 : 48분
시도 횟수 : 2회
실행 시간 : 388ms
메모리 : 28mb

2차
풀이 시간 : 33분
시도 횟수 : 1회
실행 시간 :692ms
    이후 약간 수정 후 재제출 : 515ms
메모리 :28mb

- 실수 모음
오타
로직 누락


Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 6일 때 멈추는거 주의 !! break !!
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""
"""
======================= 2차 코드 리뷰 ========================
1553 문제읽기 + 주석정리 
1558 설계
1605 구현시작
1615 디버깅 시작
    시작하자마자 인덱스 에러. 룩업테이블 오타 바로 발견 0, 1, 2, 3을 1, 2, 3, 4로..
    또 답 틀림
    프린트로 visited 찍어봄. 6이 잇는데도 쭉 가는 것 발견해서 break 추가
    그래도 답 다름. 
    문제 다시 읽어보며 생각
    겹치는 경우 처리 if문이 좀 지저분했음. 또 무조건 1이라 놓는게 아니라 겹쳐지는 거라 +하고 -하자고 생각
    거기다가 시간 충분하므로 차라리 ㄷㅏ 뽑고 난 후 visited 보고 처리하자는 생각이 들어 코드 고침
    정답
    
총평
- 1차 때랑 했던 실수 그댕애애애애로 똑같이 했다. 내 머리 어디 안간다 ..


"""
"""

각각의 말들은 네 방향 중 한 가지 방향을 선택
선택하는 방향에 따라 이동할 수 있는 격자의 범위가 달라집니다.
 체스판에 놓인 말들의 방향을 적절히 설정하여 갈 수 없는 격자의 크기를 최소화

 본인의 말은 뛰어넘어서 지나갈 수 있습니다.
 다만 상대편의 말은 뛰어넘어서 지나갈 수 없습니다
이후 갈 수 없는 격자의 크기를 계산할 때 상대편 말이 있는 격자는 계산하지 않습니다.

1~5의 경우 자신의 말의 종류를 의미
6은 상대편의 말을 의미



1 ≤ n, m ≤ 8
자신의 말의 개수는 최대 8개를 넘지 않는다고 가정해도 좋습니다.
최대 4**8 보다 작음

비어있음에도 자신의 말을 이용해서 갈 수 없는 체스판의 영역 넓이의 총 합의 최솟값

"""

"""

각각의 말들은 네 방향 중 한 가지 방향을 선택
선택하는 방향에 따라 이동할 수 있는 격자의 범위가 달라집니다.
 체스판에 놓인 말들의 방향을 적절히 설정하여 갈 수 없는 격자의 크기를 최소화

 본인의 말은 뛰어넘어서 지나갈 수 있습니다.
 다만 상대편의 말은 뛰어넘어서 지나갈 수 없습니다
이후 갈 수 없는 격자의 크기를 계산할 때 상대편 말이 있는 격자는 계산하지 않습니다.

1~5의 경우 자신의 말의 종류를 의미
6은 상대편의 말을 의미



1 ≤ n, m ≤ 8
자신의 말의 개수는 최대 8개를 넘지 않는다고 가정해도 좋습니다.
최대 4**8 보다 작음

비어있음에도 자신의 말을 이용해서 갈 수 없는 체스판의 영역 넓이의 총 합의 최솟값

"""


def oob(i, j):
    return i<0 or j<0 or i>=N or j>=M

def check_visited(r, c, dir_lst, v):
    cnt = 0
    for d in dir_lst:
        di, dj = DIR[d]
        du, dv = r + di, c + dj
        while not oob(du, dv) and arr[du][dv] != 6:
            if arr[du][dv] == 0:
                visited[du][dv] += v
            du += di
            dv += dj
            if oob(du, dv) or arr[du][dv]==6:
                break
    return cnt
# dfs
def dfs(level):
    if level == K:
        global answer
        cnt = 0
        for k in range(N):
            for v in range(M):
                if not visited[k][v] and arr[k][v] ==0:
                    cnt += 1
        answer = min(answer, cnt)

        return

    r, c = my_mal_lst[level]
    mal_num = arr[r][c]

    for dir_lst in dir_dict[mal_num]:

        check_visited(r, c, dir_lst, 1)

        dfs(level+1)
        check_visited(r, c, dir_lst, -1)





# input
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# dict 준비
dir_dict = {1: ((0,), (1,), (2,), (3, )), 2: ((0, 2), (1, 3)), 3:((0, 1), (1, 2), (2, 3), (3, 0)), \
    4: ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)), 5 : ((0, 1, 2, 3), )}
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

# blank, my_mal_lst 준비
blank = 0
my_mal_lst = []
answer = N*M
for i in range(N):
    for j in range(M):
        if arr[i][j]==0:
            blank += 1
        elif arr[i][j] <6 :
            my_mal_lst.append((i, j))


K = len(my_mal_lst)
dfs(0)
print(answer)

"""
1502 문제읽기 시작
1506 문제정리 완료. 구상시작
1550 구현+디버깅 완료 정답처리

=============오늘 실수===============
6은 count 안하는 것 놓침
dir 룩업테이블 오타 ... 그래도 쓰면서 여기서 오타 날 수 있겠다고 인지해서
비교적 빠르게 찾음

===============구상==================
갈 수 없는 칸 합의 최솟값이므로
visited로 방문 가능한 칸 1 처리 후 sum(visited)를 최대로 만든 후,
최종적으로 n*m - sum(visited)를 출력하기

1~5인 칸의 (행, 열) list로 받아두고
상하좌우 중 어디를 바라볼지 백트래킹으로 정하기
1~5가 각각 갈 수 있는 방향 미리 룩업테이블에 저장해두기

정할 때마다 그 방향에서 볼 수 있는 곳 체크 (0에서 1로바꿀 경우 cnt로 들고다니기)

5인 경우는 그냥 어딜 봐도 상하좌우이므로 실행

갈 수 있는 방향으로 쭉 가다가 oob거나 6만나면 stop
while문으로 동작하기

===============문제 정리=============
1 한쪽
2 양쪽(반대로)
3 두방향(수직)
4 세방향
5 네방향

각 말이 바라보고 있는 방향에 따라 이동할 수 있는 방향, 범위 달라짐
각 말들이 바라보는 방향을 설정하여 갈 수 없는 격자의 크기 최소화하기
최대한 많이 갈 수 있게 만들기

본인의 말 뛰어넘기 가능
상대의 말 뛰어넘기 불가

입력 n, m (직사각형 주의)
6은 상대편 말

arr에 1~5의 말 종류가 주어짐  0은 빈칸

"""
def dfs(level):
    global answer
    if level==chess_len:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and arr[i][j] != 6:
                    cnt+=1
        answer = min(cnt, answer)

        return

    cr, cc = lst[level]
    chess =arr[cr][cc] #chess 종류
    range_num = dir_range_lst[chess] #체스 종류에 따른 백트래킹 후보 종류 range 범위

    for j in range(range_num):
        #이 방향으로 바라봐보기
        check_visited(cr, cc, j, 1)
        visited[cr][cc]+=1
        dfs(level+1)
        visited[cr][cc]-=1
        check_visited(cr, cc, j, -1)

def check_visited(r, c, j, k):
    cnt = 0

    # visited[r][c] += k
    for di, dj in dir[arr[r][c]][j]:
        du, dv = r, c
        #d방향으로 갈 수 있을 때까지 체크하기
        #체크한 경우 값도 count
        while 1:
            du+= di
            dv+= dj

            if du <0 or dv<0 or du>=n or dv>=m:
                break
            if arr[du][dv]==6:
                break
            # if visited[du][dv] ==0 and k>0:
            #     cnt+=1
            visited[du][dv]+=k




#각 말 별(index번호별) 바라보는 방향에 따른 d list
dir = [[], \
       [[(-1, 0)],[(0, 1)], [(1, 0)],[(0, -1)]],\
        [[(-1, 0), (1, 0)],[(0, -1), (0, 1)],[(1, 0), (-1, 0)],[(0, 1), (0, -1)]],\
       [[(-1, 0), (0, -1)],[(-1, 0), (0, 1)],[(1, 0), (0, -1)],[(1, 0), (0, 1)]],\
       [[(1, 0), (0, -1), (0, 1)],[(-1, 0), (1, 0), (0, 1)],[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, -1)]],\
       [[(1, 0), (0, -1), (-1, 0), (0, 1)]]]
dir_range_lst = [-1, 4, 2, 4, 4, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
chess_len = 0
lst = []
answer = n*m

#체스 말 리스트 받아두기
for i in range(n):
    for j in range(m):
        if arr[i][j]!=0 and arr[i][j]!=6:
            lst.append((i, j))
            chess_len += 1
        elif arr[i][j]==6:
            visited[i][j]=6

#체스 말이 보고 있을 방향 정하기 (dir_range_lst가 for문의 범위)
dfs(0)

print(answer)


