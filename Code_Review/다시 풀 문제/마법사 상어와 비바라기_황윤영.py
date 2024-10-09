"""
1차
풀이 시간 : 36분
시도 횟수 : 1회
실행 시간 : 172 ms
메모리 : 117932KB


2차
풀이 시간 : 54분
시도 횟수 : 1회
실행 시간 : 179 ms
메모리 : 26 mb


- 실수 모음 (2차 때 더 못함; )
    - 동시성 실수 : 영양제 옮기자마자 거기서 계산 때림 ( 동시 ㅠㅠㅠ)
    - 설계 실수 : 영양제 바로 1 안먹이고 대각 세고 나서 나중에 먹이려고 함(대각 세는 데에서 오류생김)
    - 변수명 중복 실수 (ㅠ ㅠ 파이썬 우씽)
    - 인덱스 1 안빼는 실수(방향벡터)
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: 동시성 => 생각했다가 갑자기 할필요 없다고 판단해서 뺌. 왜그랬니
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리  ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 하기 직전 찾음
"""

"""
=================== 2차 코드 리뷰 ======================
2001 문제읽기 + 주석정리
2008 구현영역 정리 + 구현
2028 디버깅 시작
    테케 안맞음
    방향벡터 1 안 빼서 방향 죄다 이상하게 가는거 발견 => 수정 
    두번째 테케부터 답 안맞아서 무한 프린트 체크 ... 
    프린트 만으로는 파악이 어려워서 문제 조건, 코드 뜯어보다 
    동시성 놓친 것 생각해서 1차로 대각 더하는 것만 나눴음
    근데 대각 값 확인을 위해서 cnt 더하는 것도 분리해야해서 단계 나눔 ,, ㅠㅠ
    
총평 
    - 왜 후퇴하지? ;;;;;;;;;;;;;
    - 보자마자 ㅇㅋ 30분 내에 다 풀자 했는데 엉뚱한 수렁에 빠지기 
    - 엉엉 정신똑바로 차리고 풀자 오늘 왜그러니 
"""
"""

 n x n 격자 칸
 서로 다른 높이를 가진 리브로수

 특수 영양제는 1 x 1 땅에 있는 리브로수의 높이를 1 증가시키며,
 만약 해당 땅에 씨앗만 있는 경우에는 높이 1의 리브로수를 만들어냅니다.

 이동 방향의 경우 1번부터 8번까지 → ↗ ↑ ↖ ← ↙ ↓ ↘으로 주어지며
 이동 칸 수만큼 특수 영양제가 이동
 격자의 모든 행,열은 각각 끝과 끝이 연결되어 있습니다.


 1. 특수 영양제를 이동 규칙에 따라 이동시킵니다.


2. 특수 영양제를 이동 시킨 후 해당 땅에 특수 영양제를 투입합니다.
    투입 후 투입된 특수 영양제는 사라지게 됩니다.
3. 특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에 높이가 1 이상인 리브로수가 있는 만큼
    높이가 더 성장합니다. 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다
4. 특수 영양제를 투입한 리브로수를 제외하고 높이가 2 이상인 리브로수는
    높이 2를 베어서 잘라낸 리브로수로 특수 영양제를 사고, 해당 위치에 특수 영양제를 올려둡니다.

출력
해당 년수가 모두 지나고 난 뒤 남아있는 리브로수 높이들의 총 합을 구하는 프로그램을 작성하세요.

"""
def pr(string):
    print(f"=============={string}===============")
    for i in range(N):
        print(arr[i])
    print("=====================================")
    print()
# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)
diagonal = (-1, 1), (-1, -1), (1, 1), (1, -1)
nutrition_lst = [(N - 2, 0), (N - 1, 0), (N - 2, 1), (N - 1, 1)]
visited = [[0] * N for _ in range(N)]

for m in range(M):
    visited = [[0] * N for _ in range(N)]

    # 이동 입력
    d, p = map(int, input().split())
    d -= 1
    di, dj = DIR[d]
    # 영양제 이동!! OOB안하고 모듈!
    # 이동한 위치에서 visited 처리하고, +1, 상하좌우 개수 세서 개수만큼 +
    move_lst = []
    for r, c in nutrition_lst:
        nr, nc = r + di * p, c + dj * p
        nr %= N
        nc %= N
        arr[nr][nc] += 1
        visited[nr][nc] = 1
        move_lst.append((nr, nc))
    new_move_lst = []
    for rr, cc in move_lst:
        cnt = 0
        for ddi, ddj in diagonal:
            du, dv = rr + ddi, cc + ddj
            if du < 0 or dv < 0 or du >= N or dv >= N:
                continue
            if arr[du][dv]>0:
                cnt +=1
        new_move_lst.append((rr, cc, cnt))
    for r, c, value in new_move_lst:
        arr[r][c] += (value)

    # visited 아닌곳, 2이상인 곳을 새로운 영양제로!!
    # 영양제 배열 교체
    nutrition_lst= []
    for i in range(N):
        for j in range(N):
            if visited[i][j] or arr[i][j]<2:
                continue
            arr[i][j]-=2
            nutrition_lst.append((i, j))
answer =0
for i in range(N):
    answer += sum(arr[i])
print(answer)

from collections import deque

"""
1430 문제읽기 시작
1437 열쇠로 코드 고쳐주기... 다른코드 ..
1442 간략 구상 완료 
    => 대각에 물이 있는 개수를 세야 함을 파악해서 q 2개로 전환
    => visited에 cnt 기록하는 것으로 전환
1500 구현완료했으나 테케 안맞음
1506 q에 구름 이동 전 위치로 잘못 넣은 것 확인해서 고침
     변수 및 코드의 흐름 늘 파악하면서 코드 짤 것 ㅠㅠ 

풀이시간 : 36분
실행시간 : 172 ms
메모리 : 117932KB




=========================================
좌 / 좌상 / 상 / 우상/ 우 / 우하 / 하 / 좌하  순
1. 초기 구름 q에 넣기
2. for문 m번 
    2-1. q에 있는 구름을 모두 꺼내서 d방향으로 s만큼 이동/ 이동완료 후 그 칸에 +1
        visited체크하기 / 범위 넘어가면 mod 처리
    2-2. visited에 대각에 있는 물 개수 기록해두고 q에 다시 넣기
         q에서 꺼낸 곳의 visited값이 0 아니면 arr에 더하기
    2-3. 전체 탐색=> arr[r][c]>=2 and not visited[r][c]이면
         구름에 추가
3. sum 구해서 출력
"""


n, m = map(int, input().split())

q = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])
q2 = deque([])
directions = (0,-1),(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)
diagonal = (-1, -1), (-1, 1), (1, -1), (1, 1)
arr = [list(map(int, input().split())) for i in range(n)]
for t in range(m):
    d, s = map(int, input().split())
    d-=1 #인덱스 편하게 쓰기 위해 미리 1 빼기
    visited = [[0]*n for _ in range(n)]
    #구름 이동
    while q:
        cr, cc = q.popleft()
        nr, nc = cr+directions[d][0]*s, cc+directions[d][1]*s
        nr%=n
        nc%=n
        arr[nr][nc]+=1
        q2.append((nr, nc))
    #구름 주변 대각 증가
    while q2:
        cr, cc = q2.popleft()
        if visited[cr][cc]!=0:
            arr[cr][cc] += visited[cr][cc]-1
            continue
        value = arr[cr][cc]
        cnt = 0
        #대각 이동
        for di, dj in diagonal:
            nr = cr+di
            nc = cc+dj
            if nr<0 or nc <0 or nr>=n or nc>=n:
                continue
            if arr[nr][nc] != 0:
                cnt+=1
        visited[cr][cc] = cnt+1 #주변에 물이 없어도 구름이었던 곳은 1 기록해야 하므로 +1
        if cnt !=0:
            q2.append((cr, cc))

    for r in range(n):
        for c in range(n):
            if arr[r][c] >=2 and not visited[r][c]:
                q.append((r,c))
                arr[r][c] -= 2



answer = 0
for lst in arr:
    answer+=sum(lst)
print(answer)
