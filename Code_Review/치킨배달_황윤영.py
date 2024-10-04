"""
1차
풀이 시간 :
시도 횟수 : 1회
실행 시간 : 168ms
메모리 : 115204kb

2차
풀이 시간 : 14분
시도 횟수 : 1회
실행 시간 : 250ms
메모리 : 27mb

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 고려해야할 사항 생각해보기 + 설계에 반영
    : 택시거리임에 주의 !! bfs로 착각하지 말것!!!
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : 디버깅 불필요했음
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!

"""
"""
================= 2차 코드리뷰 ====================
2011 문제읽기 주석정리 
2014 설계 시작  
    택시 거리만 나왔다하면 바보같이 bfs로 하려고 하는 바보 같은 나
    이제 그러지 않는다 !!!
    
2017 구현시작
2025 구현완료 후 제출

총평 
택시거리만 주의하니 별로 어렵지 않은 문제였다 
거리 공식 나오면 바로 bfs생각 말고 한번 더 고민할 것!! 
"""
"""
사람, 병원 혹은 빈 칸으로 이루어져 있는 n×n 크기의 도시
각 사람의 병원 거리는 가장 가까운 병원까지의 거리
두 점 사이의 거리 = abs(x1-x2)+abs(y1-y2)

m개의 병원만을 남겨두고 나머지를 폐업
남은 m개의 병원에 대한 각 사람들의 병원 거리의 총 합이 최소
병원 m개를 남겼을 때 가능한 각 사람들의 병원 거리 총 합 중 최솟값

빈 칸인 경우 0,
사람인 경우 1
병원인 경우 2
"""
#dfs 구현하기
def dfs(level, idx):
    global answer
    #종료조건
    if level == M:
        tmp = 0
        #사람으로부터 병원 거리 탐색해서 최솟값의 합 구하기
        for pr, pc in people_lst:
            mn = N*2+1
            for k in range(K):
                if not visited[k]: continue
                hr, hc = hospital_lst[k]
                mn = min(get_dist(pr, pc, hr, hc), mn)
            tmp += mn
        answer = min(answer, tmp)
        #answer 갱신
        return
    #병원 후보들 탐색하며 고르기
    for i in range(idx, K):
        visited[i] = 1
        dfs(level+1, i+1)
        visited[i] = 0

def get_dist(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)

#입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#사람 lst, 병원 lst 준비하기
hospital_lst = []
people_lst = []
answer = float("inf")

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            people_lst.append((i, j))
        elif arr[i][j] == 2:
            hospital_lst.append((i, j))
K = len(hospital_lst)
visited = [0]*K
#dfs
dfs(0, 0)
print(answer)
"""
1533 문제 이해 완 + 대략 구상 완료 ( 백트래킹 사용할 것)
1554 구현 완료 코드트리 제출했지만 시간초과 ...
1614 백트래킹완료 후 최단거리 계산하는 방식 병원 위주로 코드 변경 후 제출

1614 백준 문제 파악 시작
1618 치킨집으로부터 집과의 최단거리 배열 갱신하는 부분에서 continue 추가함 => 정답

==============================================================================
초기 제출 : 시간이 매우 몹시 많이 들었다. 아무래도 한집배달 아니고 알뜰배달인듯 ..! 개선해보자!
메모리 : 151048KB
시간 : 2268ms

개선 시도 1회차
난 왜 굳이 bfs를 했는가....
수학 전공을 다시 좀 붙잡아보자 ...
그냥 계산하면 될 걸 다 컴퓨터한테 돌리지 말자 ㅠ
메모리 : 116392kb
시간 : 208ms

개선 시도 2회차
dist배열을 가지고 매번 갱신 및 갱신한 dist배열을 한번 더 탐색하는게 비효율적
치킨 집에서 가장 가까운 집을 갱신하면,
각 집은 더 가까운 치킨집이 있을 수 있다는 점이 문제이므로,
거꾸로 집에서 가장 가까운 치킨집을 찾고 끝내기
메모리 : 115204kb
시간 : 168ms

=================================== 구상 =====================================

전체 치킨 집 중 폐업시키지 않을 치킨집 m개 고르기
다 고른 후 그 치킨집으로부터 집 거리 갱신.


"""
#def : 병원들 중 m개 고르는 함수
def pick_hospitals(level, idx):
    global answer
    if k-idx < m-level:
        return
    #종료 조건 : m개 다 고르면 고른 병원들로 사람들 사이의 최단 병원거리 갱신
    if level == m:
        tmp = 0
        for p in people:
            d = inf
            for h in selected:
                d = min(get_distance(p, h), d)
            tmp += d
        answer = min(tmp, answer)

        answer = min(answer, tmp)
        return

    for i in range(idx, k):
        h = hospitals[i]
        selected[level] = h
        pick_hospitals(level+1, i+1)


def get_distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

#input
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
hospitals = []
people = []
selected = [(0,0)]*m
inf = 50*2*100


k=0
answer = inf
#arr에서 병원인 경우 list에 넣기 (뽑을 병원 후보군)
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            hospitals.append((i,j))
            k+=1
        elif arr[i][j] == 1:
            people.append((i,j))
#병원 m개 뽑기
pick_hospitals(0, 0)
print(answer)