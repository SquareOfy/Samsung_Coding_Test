"""
1차
총 풀이시간 : 1시간 29분
실행시간 : 100ms
메모리 : 110828ms

2차
풀이 시간 : 15분
시도 횟수 : 16분
실행시간 : 130ms
메모리 : 25mb

실수 모음 
설계 미흡
인덱스 /끝점 처리 미흡

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 
    : lst 거꾸로 돌아야한다는 것
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : 디버깅할게 없었음
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 
"""

"""
================== 2차 코드리뷰 ====================
1946 문제 읽기 시작 + 주석정리
    읽으면서 생각나는 아이디어 종이에 메모함

1955 설계 시작
1958 주석으로 구현 영역 정리 및 구현 시작
2002 인덱스 에러 간단하게 수정 후 제출 => 정답

총평
깔끔하게 풀었다. 이 문제 모의로 접했을 때 많이 헤맸는데
다른 사람 풀이 봤던게 떠올라서 그대로 다시 설계하고 구현했더니
기존 내 방법보다 훨씬 구현난이도도 쉽고 깔끔하게 풀 수 있었다.
"""
"""

#배열 인덱스 그대로 따라가면 되겠군
좌표평면은 x 값이 위에서 아래로 갈수록 증가하며 0에서부터 시작하며,
y는 왼쪽에서 오른쪽으로 갈수록 증가하며 0에서부터 시작


0차 드래곤 커브는 길이가 1인 선분
n차 드래곤 커브는 n-1차 드래곤 커브의 끝점에

n-1차 드래곤 커브를 복제한 뒤 시계 방향으로 90도 회전시킨 뒤 연결한 도형

n개의 드래곤 커브가 주어질 때 만들어지는 단위 정사각형의 개수
x값과 y값의 범위는 0 ≤ x, y ≤ 100
만들어지는 정사각형이란 정사각형의 네 꼭지점이 모두 드래곤 커브에 속하는 도형
"""
#입력
DIR = (0, 1), (-1, 0), (0, -1), (1, 0)
N = int(input())
arr = [[0]*101 for _ in range(101)]
#N번 반복
for n in range(N):
    #드래곤 커브 정보 입력
    x, y, d, g = map(int, input().split())
    lst = [d]
    #세대 수만큼 lst 거꾸로 돌면서 d 시계회전 시킨 값 넣기 (d+1)
    for ger in range(g):
        for k in range(len(lst)-1, -1, -1):
            cur = lst[k]
            lst.append((cur+1)%4)
    arr[x][y] = 1
    #lst 다 돌면서 arr에 찍기
    for cd in lst:
        di, dj = DIR[cd]
        x+= di
        y+= dj
        arr[x][y] = 1

answer = 0
#arr 다 돌며 단위정사각형 개수 세기
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            answer+=1
print(answer)

"""
26일 목요일 기록
1501 문제읽기 시작 : 딱봐도 어려움. 그리고 헤맸던 기억 나서 다음 문제로 넘어가보기1

9월 2일 월요일 기록
1635 문제 읽기 시작
1646 문제 이해 완료 및 커브 찍는 방법 외 다른 구상 완료 ( 커브 찍는 방법 고민)
1650 커브 관련 구상완료 및 구현 시작

1745 이때까지 테케 안맞고 회전의 방향 찾지 못했음
    문제 요인
        - 커브가 회전할 때 end지점을 잡아서 그 지점과 앞에 있는 점들과의
            차를 이용해 방향 계산하는 방향성은 맞았으나 정확히 어디를 빼고 어디를 더할지
            명확히 생각하지 못하고 뻬봤다가 더해봤다 하면서 왔다갔다 식으로 구현함
        - 앞에 있는 점들을 리스트에 넣어 관리하면서 pop했다가 임의의 stk에 append해놓은걸
            대체하는 방식으로 처음에 구현했는데, 모든 점을 다 끝점과 회전하도록
            모두 탐색하지 못함.
            => pop이 아니라 for문으로 탐색하는 방식으로 변환
            => 추가되는 점들을 따로 관리하여 list에 extend하는 형식으로 변환
            => 이 과정에서 빠르게 제대로 탐색하지 못한다는 사실을 캐치하지 못해 시간낭비함
1905 - 1924 디버깅 후 제출 -> 정답

총 풀이시간 : 1시간 29분
실행시간 : 100ms
메모리 : 110828ms

=====================개선할 점 ======================
방향을 회전하는 문제에 취약함을 느낌
많이많이 회전문제 풀어야겠다

============== 커브 idea ==============
드래곤 커브 범위 밖으로 안나가므로 범위 체크 불필요
1. 끝점 기억하기
2. 끝점 제외 stk에 넣고 꺼내면서 끝점에 연결해가기. .. ?
    끝점 : (ey, ex) / stk에서 꺼낸 점 : (cy, cx)
    방향은 (ex-cx, ey-cy)로 ! 거리는 항상 1. 앞세대는 앞에서 찍었음 !!
    즉 다음에 찍을 점은 (ey + (ex-cx), ex+(ey-cy))
3. stk이 비었다면 마지막 점을 끝점으로 갱신하고 다음 세대로 가기

처음 stk 세팅 및 끝점 세팅 어떻게 할까?
0세대 찍고 그 때 끝점 세팅해놓기

"""
arr = [[0]*101 for _ in range(101)]
dir = (0, 1), (-1, 0), (0, -1), (1, 0)
t= int(input())

for tc in range(t):
    x, y, d, g = map(int, input().split())
    #0세대 찍기
    arr[y][x] = 1
    di, dj = dir[d]
    arr[y+di][x+dj] = 1
    ey, ex = y+di, x+dj
    stk = [(y, x), (ey, ex)]
    ng = 0
    next_stk = []

    while ng<g:
        ey, ex = stk[-1]
        for i in range(len(stk)-1, -1, -1):
            ey, ex = stk[-1]
            cy, cx = stk[i]
            ny = ey-(ex-cx)
            nx = ex+(ey-cy)
            arr[ny][nx] = 1

            next_stk.append((ny, nx))
        stk.extend(next_stk)
        next_stk = []

        ng+=1

answer =0
#answer 찾기
for i in range(100):
    for j in range(100):
        #이 점에서 우, 하, 우하, 본인 체크
        if not arr[i][j] or not arr[i+1][j] or not arr[i][j+1] or not arr[i+1][j+1]:
            continue
        answer+=1
print(answer)