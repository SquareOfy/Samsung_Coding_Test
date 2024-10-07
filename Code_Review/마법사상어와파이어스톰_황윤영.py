
"""
1차
풀이 시간 : 35분
시도 횟수 : 1회
실행 시간 :844ms
메모리 : 125988kb

2차
풀이 시간 : 40분
시도 횟수 : 1회
실행 시간 : 1263ms
메모리 : 30mb

- 실수 모음
    빙하 크기 구할 때 bfs 시작값 실수
    동시성 실수
    회전할 때 기존 배열 사용해서 회전하고 거기에 붙여서 실수..
    continue로 아래 로직까지 건너뛰어버리는 실수

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: 회전을 하는데 그 안의 구역은 회전이 안된다? 배열돌리기4에선가 썼던 방식 써봐야지
: 빙하 녹일 때 조심하자 동시!
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 할필요 ㄴㄴ
"""
"""
=================== 2차 코드 리뷰 ===================
1408 문제 읽기 + 주석정리 
1414 설계 시작
    회전 안에는 모양 유지한체 할 방법 바로 생각 안나서 조금 버벅임,, 
    그래서 회전 구현할 때 중간테스트 꼭 함,, 
1437 디버깅
    q ==0 일 때 continue 시키는 실수 함 

아쉬운 점
    내가 사용한 배열 회전 방식은 시간이 너무 오래걸린다. 
    그냥 하드코딩으로 갖다 붙였어도 됐겠다. 
"""
"""
빙하를 회전하는 범위를 레벨

레벨이 L일 때 2**L * 2**L만큼 격자를 선택하여 2**(L-1) * 2**(L-1)만큼 잘라 4등분하여 시계방향 90도회전 

각각의 회전이 모두 끝나고 난 뒤에는 빙하에 속한 얼음이 녹습니다. 
한 칸을 기준으로 상하좌우 인접한 칸에 얼음이 3개 이상 있는 경우에는 녹지 않습니다.
그렇지 않은 경우에는 1이 줄어듭니다. 

인접한 칸이 격자를 벗어나는 경우나 해당 칸의 값이 0인 경우에는 얼음이 존재하지 않는다고 생각합니다. 
얼음이 녹는 것은 동시에 진행됩니다.

출력
모든 회전을 끝내고 난 뒤에 남아있는 빙하의 총 양과 가장 큰 얼음 군집의 크기
빙하의 총 양이란 격자에 남은 숫자의 총 합을 뜻하며 얼음 군집이란 연결된 칸의 집합
"""

from collections import deque
def rotate_(L, flag):
    rotate_tmp = [[0]*N for _ in range(N)]
    #큰 사각형 회전
    for i in range(0, N, L):
        for j in range(0, N, L):
            tmp = [[0]*L for _ in range(L)]
            for k in range(L):
                tmp[k] = arr[i+k][j:j+L]
            if flag:
                tmp = list(map(list, zip(*tmp[::-1])))
            else:
                tmp = list(map(list, zip(*tmp)))[::-1]

            for k in range(L):
                rotate_tmp[i+k][j:j+L] = tmp[k][:]
    return rotate_tmp


def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

def bfs(i, j):
    visited[i][j] = 1
    q = deque([(i, j)])
    size = 0

    while q:
        cr, cc = q.popleft()
        size+=1
        for di, dj in DIR:
            du, dv = cr+di, cc+dj
            if oob(du, dv) or arr[du][dv] ==0 or visited[du][dv]:
                continue
            q.append((du, dv))
            visited[du][dv] =1
    return size
n, Q = map(int, input().split())
N = 2**n
#배열 받기
arr = [list(map(int, input().split())) for _ in range(N)]
order_lst = list(map(int, input().split()))
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
ice = [[0] * N for _ in range(N)]

for q in order_lst:
    if q!=0:
        L = 2**q
        arr = rotate_(L, 1)
        #부분 사각형 반시계 회전
        arr = rotate_(L//2, 0)

  #############################부분체크
    # for i in range(N):
    #     print(arr[i])
    # print()
    ############################
    for i in range(N):
        for j in range(N):
            if arr[i][j]==0: continue
            cnt = 0
            #상하좌우 인접 빙하 개수 체크
            for di, dj in DIR:
                du, dv = i+di, j+dj
                if oob(du, dv): continue
                if arr[du][dv] ==0: continue
                cnt+=1
                if cnt==3:
                    break
            if cnt<3:
                ice[i][j] -=1
    for i in range(N):
        for j in range(N):
            arr[i][j] += ice[i][j]
            ice[i][j] = 0



mx_size = 0
ice_sum = 0
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        ice_sum += arr[i][j]
        if arr[i][j]>0 and not visited[i][j]:
            mx_size = max(mx_size, bfs(i, j))

print(ice_sum)
print(mx_size)
"""
풀이시간 총 35분

1459 문제 읽기 시작 (문제이해 10분 소요)
     문제 읽으면서 회전 다 시키고 얼음 녹여야지, q번 l list 돌고 출력값 구할 것 생각함
     얼음이 있는 칸 3개이상 또는 그 이상과 인접해있지 않는 칸 부분 이해가 잘 안됐었음
1507 문제 이해 안되는 부분 추가 이해
     문제 이해를 위해 일단 입력 받고 초기 배열의 전체 합을 찍어봄
     문제 반복해서 읽다보니 처음에 0인 칸이 없어도 모서리 4칸은 무조건 2개만 인접해서
     얼음이 녹을 거라는 생각이 들어서 해결

1509 구현시작 (10분 소요)
     - 회전 구현 시, list(zip(배열[::-1]) 사용하는데,
       튜플을 리스트로 바꾸는게 서툴러 조금 버벅임
     - 중간중간 출력해서 회전 잘 되는지 확인해봄

1519 회전구현 완료 / 얼음 녹이기 구현 시작 (8분소요)
    - 얼음을 사방 탐색 후 그 자리에 녹인 것 바로 반영해서 테케 안맞는 문제 발생했음
    - 따로 배열 마련해서 다시 했음
    - 0인 칸도 매번 돌지 말고 녹은 얼음은 dict나 1차원 list로 리팩토링해도 좋겠다

1527 출력부분 구현 (6분 소요)
    - bfs에서 result=1로 하고 q에서 꺼낼때마다 1을 더하여 결과값이 1 차이나는 문제 발생
    - result =0 으로 해결
    - bfs 실행을 0인 곳에서도 해버린 것 디버깅

* 잘한점
    팀별 문제풀이 루틴에 따라 문제 조건 체크, 문제 다시 읽기, 중간 출력을 잘 수행함
* 아쉬운점
    문제 풀이 전 시간 계산 전혀 안함
    로직 흐름 사이사이에 생기는 실수와 빈틈,,
    실행시간이 다소 오래걸린다 리팩토링 해보자 .

"""
from collections import deque
def bfs(r, c):
    q = deque([(r,c)])
    visited[r][c] = 1
    result = 0
    while q:
        cr, cc = q.popleft()
        result+=1
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            du = cr+di
            dv = cc+dj
            if du<0 or dv<0 or du>=N or dv>=N:
                continue
            if visited[du][dv] or arr[du][dv] == 0:
                continue
            visited[du][dv] = 1
            q.append((du, dv))
    return result
n, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
lst = list(map(int, input().split()))
N = 2**n
for q in range(Q):
    l = 2**lst[q]

    #l만큼 나눠서 시계방향 회전하기
    for r in range(0, N, l):
        for c in range(0, N, l):
            #r,c가 길이가 2**l인 사각형의 시작점
            tmp = [arr[k][c:c+l] for k in range(r, r+l)]
            tmp = [list(k) for k in list(zip(*tmp[::-1]))]
            for k in range(l):
                arr[r+k][c:c+l] = tmp[k]

    #회전 구현 완료

    ice = [[0]*N for _ in range(N)]
    #얼음 녹이기 완료
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                continue
            cnt = 0
            for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                if cnt ==3:
                    break
                du = r+di
                dv = c+dj
                if du<0 or dv<0 or du>=N or dv>=N:
                    continue
                if arr[du][dv] !=0:
                    cnt += 1
            if cnt<3:
                ice[r][c] -=1
    for r in range(N):
        for c in range(N):
            arr[r][c] += ice[r][c]
            ice[r][c] = 0
#모든 파이어볼 완료

#출력값 준비하기

#전체 합
s = 0
for i in range(N):
    s+= sum(arr[i])
print(s)
#전체합 일치 확인


#제일 큰 얼음덩어리의 칸 개수
answer = 0
visited = [[0]*N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if visited[r][c] or arr[r][c]==0:
            continue
        size = bfs(r, c)
        answer = max(size, answer)
print(answer)