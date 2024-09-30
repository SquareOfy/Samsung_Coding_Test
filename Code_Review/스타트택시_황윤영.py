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