"""
1차
풀이 시간 : 19분
시도 횟수 : 2회
실행 시간 : 196ms
메모리 : 114724kb

2차
풀이 시간 : 24분
시도 횟수 : 2회
실행 시간 : 180 ms
메모리 : 114700 kb


- 실수 모음
    - 문제 조건 놓침 : 병원은 cnt 안올리고 그냥 지나갈 수 있는 것 간과 
    - bfs visited 누락
    - bfs return 값 실수


Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : visited선언 bfs에서 매전 해도 괜찮을지 체크
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : no 구현할 양이 너무 간단했음
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok. 테케 안맞아서 프린트해서 확인해봄
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""


"""
====================== 2차 코드 리뷰 ====================
1406 문제 읽기 시작 + 주석 정리 
1410 설계시작 
1413 구현시작 
1421 테케 안맞음. time + 하는 시점 조정 + 아예 바이러스 없을 때 처리
1426 오답
    테케를 보니 병원을 지나칠 수 있음을 알고 bfs에서 continue 조건문 수정해서 해결

"""
"""
N×N 크기의 도시
병원과 벽을 제외한 모든 지역에 바이러스
M개의 병원을 적절히 고르기

골라진 병원들을 시작으로 매 초마다 상하좌우로 인접한 지역 중 벽을 제외한 지역에
백신이 공급되기 때문에 그 자리에 있던 바이러스는 사라지게 됩니다.


M개의 병원을 적절히 골라 바이러스를 전부 없애는데 걸리는 시간 중 최소 시간을 구하는 프로그램


0 : 바이러스
1 : 벽
2 : 병원

3≤N≤50
1≤M≤10

출력
M개의 병원을 적절히 골라 모든 바이러스를 없애는 데 필요한 최소 시간을 출력
모든 바이러스를 없앨 수 있는 방법이 없다면 −1을 출력
"""


def bfs(lst):
    q = lst[:]
    visited = [[0]*N for _ in range(N)]
    for i, j in q:
        visited[i][j] = 1
    cnt = 0
    time = 0
    while q:
        nq = []

        for cr, cc, in q:
            for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                du, dv = cr+di, cc+dj
                if du<0 or dv<0 or du>=N or dv>=N:
                    continue
                if visited[du][dv] or arr[du][dv] ==1:
                    continue
                visited[du][dv] = 1
                nq.append((du, dv))
                if arr[du][dv] == 0:
                    cnt += 1
        time+=1
        if cnt==virus_cnt:
            break
        q = nq

    return cnt==virus_cnt, time


def dfs(level, idx, lst):
    global answer
    if level==M:
        flag, time = bfs(lst)
        if flag:
            answer = min(answer, time)
        return

    for i in range(idx, len(hospital_lst)):
        dfs(level+1, i+1, lst+[hospital_lst[i]])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hospital_lst = []
virus_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            hospital_lst.append((i, j))
        elif arr[i][j] == 0:
            virus_cnt+=1
answer=  N*N
if virus_cnt!=0:
    dfs(0, 0, [])
else:
    answer = 0
print(answer if answer != N*N else -1)


"""
총 풀이시간

1358 문제 읽고 조건 정리 + 슈더코드 작성
    - 시간 될 지 생각해 봄 굿굿
    - 활성 바이러스 비활성 바이러스 무슨 말인가 싶어서 주어진 테케 설명 보면서 하나하나 짚어봄

1407 구현시작

1414 구현완료 및 디버깅 시작
    테케 안맞음
    전반적으로 값이 중구난방 + 어떤 테케에서는 무한루프 돌길래 살펴보다 처음부터 다 퍼져있었을 상태를 고려하여 추가조건 넣음
    bfs visited 누락 발견 = >  추가
    테케가 맞아간다 !
1417 제출 => 틀림
    출력 조건 다시 읽어봄
    로직 전반적으로 다시 뜯어보기
    lst 출력해보며 bfs 로직 확인
    bfs에서 rank가 return이 안될 때 -1이 반환되는데 최소시간을 갱신하는 과정에서 -1이 갱신되겟다고 생각
    고침

피드백
- 잘한점
    시간복잡도 생각한번 해봤음
- 못한점
    bfs에서 visited 자주 누락하는군
    bfs에서 return 값을 활용할 때! bfs 로직 중에 return이 이뤄지지 않았을 때 -1을 쓰는 버릇이 있음.
    근데 이거 위험한듯. bfs 값이 max 처리 되는지 min인지 또는 어떤 처리를 거쳐 활용되는지를 생각하며 반환값 정하자
    


=====================================================================
처음 모든 바이러스 비활성 상태

활성 바이러스 상하좌우 빈칸을 "!!!동시!!!" 복제
복제에 1초 소요

바이러스 M개 활성상태로 변경하려고 함
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 => 활성 됨

0 빈칸
1 벽
2 바이러스



모든 빈칸에 바이러스를 퍼뜨리는 최소 시간 ...

빈칸 개수 세고 바이러스 퍼질 때마다 -1 시켜서 0될때 시간 min 갱신하자 .


바이러스 M개 고르기 2500 C 10 ? 시간 내에 되나
virus = []
dfs(level, idx, lst)
    level == M:
        bfs(lst)

    for i in range(idx, len(virus)

"""
from collections import deque
def dfs(level, idx, lst):
    global answer
    if level == M:
        s = bfs(lst)
        answer = min(s, answer)
        return
    for i in range(idx, v):
        dfs(level+1, i+1, lst+[i])

#lst에 고른 바이러스들 활성화시켜서 퍼뜨리고 전체 소요된 시간 반환
def bfs(lst):
    q = deque([])
    visited = [[0]*N for _ in range(N)]
    b = blank
    for i in lst:
        r, c = virus[i]
        q.append([r, c, 0])
        visited[r][c] = 1

    while q:
        r, c, rank = q.popleft()
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            du = r+di
            dv = c+dj
            if du<0 or dv<0 or du>=N or dv>=N:
                continue
            if visited[du][dv] or arr[du][dv]==1:
                continue
            if arr[du][dv] == 0:
                b-=1
                if b==0:
                    return rank+1
            visited[du][dv] = 1
            q.append((du, dv, rank+1))
    return N*N+1
N, M = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
blank = 0
answer = N*N+1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            blank+=1
        elif arr[i][j]==2:
            virus.append((i, j))
v = len(virus)
if blank == 0:
    print(0)
else:
    dfs(0, 0, [])
    print(answer if answer!=N*N+1 else -1)