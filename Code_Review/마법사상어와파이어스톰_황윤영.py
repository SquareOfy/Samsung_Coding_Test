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