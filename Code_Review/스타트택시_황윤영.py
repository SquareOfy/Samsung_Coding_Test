"""
1차
풀이 시간 : 1시간 3분
시도 횟수 : 5회
실행 시간 : 196 ms
메모리 : 115564 kb

2차
풀이 시간 : 35분
시도 횟수 : 1회
실행 시간 : 192 ms
메모리 : 115076 kb

- 실수 모음
    - 설계 디테일 부족(다양한 케이스 고려 못했었음)
    - 함수 return 누락 (None 나와서 TypeError)
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 매 이동마다 거리 보기. 승객 못찾는 경우, 목적지 못가는 경우 주의

5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""

"""
========================= 2차 코드 리뷰 ==================
보자마자 이거 와장창 실수 가득했던 문제다 하고 생각남
1500 문제 주의해서 읽기 시작 + 주석
1506 설계
    승객찾는 함수, 승객 데려다 주는 함수로 나눠서 설계
    이 때 return 뭐할지, info 어떻게 활용할지 적음
    
1515 주석 정리 및 구현
1528 구현완료 후 디버깅
    답이 다르게 나옴.
    단계별로 프린트해서 승객 잘 찾는지, 이동거리 일치하는지 확인
    gr, gc가 이상하다?
    arr 찍어봄. arr에 음수로 해놓고 그냥 idx 활용한 것 발견해서 -붙여줌
    그러고 나서도 답이 달랐음 
    태우고 난 승객 안없앤 것 확인 => 수정 후 정답.
    

"""
"""
n * n 격자의 도로
차가 지나갈 수 없는 벽의 위치와 m명의 승객의 위치가 주어질 때

승객을 태우러 출발지에 이동할 때에나 태우고 목적지로 이동할 때 항상 최단 거리로 이동
자율주행 전기차는 한 칸을 이동할 때 1만큼의 배터리를 소요
승객을 목적지로 무사히 태워주면 그 승객을 태워서 이동하며
소모한 배터리 양의 두 배만큼을 충전한 뒤 다시 이동
이동하는 도중에 배터리가 모두 소모되면 그 즉시 종료

만일 승객을 목적지로 이동시킨 동시에 배터리가 모두 소모되는 경우에는
 승객을 태우며 소모한 배터리의 두 배만큼 충전되어 다시 운행을 시작할 수 있습니다.

 승객이 여러명일 경우 현재 위치에서 최단 거리가 가장 짧은 승객을 먼저
 만약 그런 승객이 여러 명일 경우에는 가장 위에 있는 승객을,
 그런 승객이 여러 명일 때는 가장 왼쪽에 있는 승객을

"""
from collections import deque


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


def find_passenger():
    q = deque([(tr, tc, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[tr][tc] = 1
    pr, pc = N, N
    dist = N * N
    while q:
        cr, cc, rank = q.popleft()
        if arr[cr][cc] < 0:
            if dist > rank:
                dist = rank
                pr, pc = cr, cc
            elif dist == rank and (pr, pc) > (cr, cc):
                pr, pc = cr, cc
                dist = rank
            continue
        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv) or arr[du][dv] == 1 or visited[du][dv]:
                continue

            q.append((du, dv, rank + 1))
            visited[du][dv] = 1
    return pr, pc, dist


def bfs_to_goal(sr, sc, idx):
    gr, gc = p_info[idx]
    result = -1
    q = deque([(sr, sc, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    while q:
        cr, cc, rank = q.popleft()
        if cr == gr and cc == gc:
            return rank
        for di, dj in DIR:
            du, dv = cr + di, cc + dj
            if oob(du, dv) or visited[du][dv] or arr[du][dv] == 1:
                continue
            q.append((du, dv, rank + 1))
            visited[du][dv] = 1
    return result


def change_idx(i):
    return int(i) - 1


# 입력
N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tr, tc = map(change_idx, input().split())
p_info = [-1]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
for m in range(1, M + 1):
    sr, sc, er, ec = map(change_idx, input().split())
    arr[sr][sc] = -m
    p_info.append((er, ec))

# for문
for m in range(M):
    # 태울 승객 찾기
    pr, pc, rank = find_passenger()

    # 못찾거나 C <0 가 되면 ans -1로 바꾸고 break
    if pr == N or C - rank < 0:
        C = -1
        break

    # 승객 태워다주기
    C -= rank
    idx = -arr[pr][pc]
    gr, gc = p_info[idx]
    dist = bfs_to_goal(pr, pc, idx)
    arr[pr][pc] = 0
    p_info[idx] = -1

    # 못태워다주거나 C<0 되면 BREAK
    if dist == -1 or C - dist < 0:
        C = -1
        break
    C += dist
    tr, tc = gr, gc

print(C)

"""
코드리뷰

풀이 시간 : 1시간 3분
실행 시간 : 196 ms
메모리 : 115564 kb

1003 문제 읽기 시작 + 구상 + 설계
     종이에 조건들 정리
     종이에 설계 내용 말로 정리
1017 구현할 내용 주석으로 정리 + 구현
1033 구현완료 => 테케 틀려서 디버깅 시작
    sort할 때 passenger 형식이 잘못된걸 보고 append 한 곳 찾아가며 잘못넣은 것 확인해서 수정
    조건 맞춘 후, dist, p 뭐가 잘못됐는지 보다가 dist가 더해지는 경우에 대해 문제를 잘못 이해했음 깨달음
    이 외에도 문제 조건 놓치거나 다양한 상황 고려 못해서 엄청 틀림
    - 목적지로 못 가는 경우나 아예 승객을 태우러 갈 수 없는 경우 생각 못함
    - 태우러가는 길, 목적지까지 가는 길 중 어떤 dist를 더해야하는 지 많이 혼동함

피드백
    - 잘한점..
        음? ㅎ
    - 아쉬운 점
        문제를 깊이 이해하지 않고 다양한 조건 상황 생각해보지 않음

    한참 전에 풀었던 문제를 이제 와서 리뷰하니, 내가 문제를 푸는 루틴이나
    내가 실수를 덜하거나 빨리 잡기 위한 방법을 꽤나 잡아가고 있다는 느낌이 들었다.
    이 당시에는 문제도 대강 읽고 이해한 대로 빨리 구현하고
    엉망진창인 코드에서 디버깅이 어디가 문제인지 찾는지 애를 먹은게 영상으로도 많이 느껴져서. .

    이로써 빚 청산 완료 .............................
"""
from collections import deque

def oob(i, j):
    return i>=N or i<0 or j>=N or j<0
def find_passenger():
    q = deque([(r, c, 0)])
    visited = [[0]*N for _ in range(N)]
    visited[r][c] = 1
    result = N*N

    lst = []
    while q:
        cr, cc, rank = q.popleft()
        if arr[cr][cc]>=1 and result >= rank:
            lst.append(arr[cr][cc])
            result = rank
            continue

        for di, dj in dir:
            du = cr+di
            dv = cc+dj
            if oob(du, dv) or visited[du][dv] or arr[du][dv] == -1:
                continue
            q.append((du, dv, rank+1))
            visited[du][dv] = 1
    #lst 정렬
    if not lst:
        return -1, -1
    lst.sort(key=lambda x : (passenger[x][0], passenger[x][1]))
    # print(lst)
    return lst[0], result

def go(i, j, y, x):
    #i, j 출발지
    #y, x 목적지
    q = deque([(i, j, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    while q:
        cr, cc, rank = q.popleft()
        if cr ==y and cc==x:
            return rank

        for di, dj in dir:
            du = cr+di
            dv = cc+dj
            if oob(du, dv) or arr[du][dv] == -1 or visited[du][dv]:
                continue
            visited[du][dv] = 1
            q.append((du, dv, rank+1))
    return -1




#input
N, M, K = map(int, input().split()) #n*n / M 승객수 / K : 현재 연료
arr = [list(map(int, input().split())) for _ in range(N)]
dir = (-1, 0), (0, 1), (1, 0), (0, -1)
#arr에서 1을 -1로 변환
for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            arr[i][j] = -1

#택시 위치
r, c = map(int, input().split())
r, c = r-1, c-1


#승객 입력 받기
#인덱스 1부터 시작
passenger = {}
for m in range(1, M+1):
    st_r, st_c, ed_r, ed_c = map(int, input().split())
    passenger[m] = (st_r-1, st_c-1, ed_r-1, ed_c-1)
    arr[st_r-1][st_c-1] = m


#승객 수 for문
for m in range(M):
    #승객 찾기
    #현재 택시 위치에서 BFS. -1 : 벽   / 0 이면 그냥 Go / >=1 이면 lst에 담기
    #lst sort (x, dict[i][1]) 번호 작은순 / 출발지 열 작은순
    p, dist1= find_passenger()
    if p==-1:
        K = -1
        break
    pr, pc, dr, dc = passenger[p]
    arr[pr][pc] = 0 #태운 손님 표시


    #그 위치부터 목적지까지 BFS
    dist2 = go(pr, pc, dr, dc)
    #dist += 최단 거리

    #택시위치 변환
    r, c = dr, dc
    K -= dist1+dist2
    #현재연료 - dist <0 이면 현재 연료 -1로 하고 break
    # print("dist 1 : ", dist1)
    # print("dist2 " , dist2)
    if K<0 or dist2<0:
        K = -1
        break
    #아니면 *2 해서 더하기
    K += dist2*2
    # print(K)

print(K)