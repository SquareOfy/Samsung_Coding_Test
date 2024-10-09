"""
==================== 1차 =====================
풀이 시간 :  1시간 20분
1차
시도 횟수 : 1회
실행 시간 :  240 ms
메모리 : 116060kb

2차 코드개선 : 코드리뷰 때 조언받은 visited clean 방식, 기준 블록 선정 방식 수정
실행 시간 : 224ms
메모리 : 116404kb

3차 코드개선 : 고치고 보니 find_rainbow함수 굳이다 싶어서 없앰 오잉 근데 더 걸리네 ..
실행 시간 : 232ms
메모리 : 115880kb


==================== 2차 ====================
풀이 시간 :  1시간 1분
시도 횟수 : 2회
실행 시간 :  304 ms (코드트리)
메모리 : 27 mb


- 실수 모음
    - 중력할 때 땡겨온 후 원래 자리 빈칸 만들기 깜빡함
    - 문제조건(우선순위) 누락
    - 구현 디테일 놓침,, 중력할 때 while문으로 하면 r -1바로되는데 생각 못하고 r 바로 봐야할 값으로 보냄
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: 빨간색 visited되돌릴것
: 우선순위 주의하기
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리  ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 할필요 ㄴㄴ

"""
"""
=================== 2차 코드 리뷰 ===========================
1705 문제읽기+주석정리
1715 설계시작 
    gravity -1 요소 땜에 어려워서 주의하려함
    처음 풀 당시 기준점 비효율적으로 찾았던거 생각나서 바로 for문으로 적용해야지 생각함 => 가차없이 실수함
    
1724 구현할 내용 주석 정리 + 구현시작
1737 디버깅 시작
    테케 안맞음. pr 함수 만들어서 찍어보기 
    중력 이상하군 => 내리고 나서 그자리 -2로 채우기 추가 
    ㅇㅋ 됐군 제출 => 오답 
    와 진짜 안보였다 중력도 잘 동작하고 회전도 잘되고 폭탄도 잘 찾는데 ,, 
    아무리 봐도 안보임... 리셋할까 싶을 때 밥먹으러 가야했음 
    ~1803
1936 다시 디버깅 시작
    고민하다가 딱 한번만 더 봐보자 하고 문제 쭉 다시읽고 코드 뜯어봄
    테케 출력한건 규모도 너무 크고 눈아파서 힘들겠다고 생각해씅ㅁ
    로직 하나하나 한줄한줄 따라가다가 중력에서 r이 nr -1 가리켜야하는데 while 문 들어가면 바로 또 -1 하는 것 발견 ㅠ
    이때 못찾았으면 리셋이 옳았겠군. . 

"""
"""
-1, 0, 그리고 1이상 m이하의 숫자로만 이루어진 n * n 크기의 격자

-1은 해당 칸에 검은색 돌
0은 빨간색 폭탄
1이상 m이하의 숫자는 빨간색과는 다른 서로 다른 색의 폭탄

폭탄묶음
2개 이상의 폭탄으로 이루어져 있어야 하며
모두 같은 색깔의 폭탄으로만 이루어져 있거나
빨간색 폭탄(0)을 포함하여 정확히 2개의 색깔로만 이루어진 폭탄
빨간색 폭탄으로만 이루어져 있는 경우는 올바른 폭탄 묶음이 아니며
모든 폭탄들이 전부 격자 상에서 연결

1. 현재 격자에서 크기가 가장 큰 폭탄 묶음을 찾습니다.
    가장 많은 수의 폭탄들로 이루어진 폭탄 묶음
    크기가 큰 폭탄 묶음이 여러 개라면 다음 우선순위에 따라 폭탄 묶음을 선택
    빨간색 폭탄이 가장 적게 포함된 것
    각 폭탄 묶음의 기준점 중 가장 행이 큰 폭탄 묶음
    폭탄 묶음의 기준점 중 가장 열이 작은 폭탄 묶음

    기준점
    해당 폭탄 묶음을 이루고 있는 폭탄들 중 빨간색이 아니면서 행이 가장 큰 칸
2. 선택된 폭탄 묶음에 해당되는 폭탄들을 전부 제거
     중력이 작용하여 위에 있던 폭탄들이 떨어지지만, 여기서 유의해야 할 점은
    돌은 특이한 성질을 띄고 있기 때문에 중력이 작용하더라도 떨어지지 않습니다.

3. 반시계 방향으로 90' 만큼 격자 판에 회전

4. 다시 중력이 작용하며, 이때 역시 돌은 절대로 떨어지지 않습니다.

더 이상 폭탄 묶음이 존재하지 않을 때까지 반복

폭탄 묶음의 폭탄 개수 C 이면 C*C 만큼 점수얻음
"""


from collections import deque
#bfs
    # 빨간색 lst 받아서 visited 해제 + len 반환
def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    lst = []
    red_lst = []

    while q:
        cr, cc = q.popleft()
        lst.append((cr, cc))

        for di, dj in DIR:
            du, dv = cr+di, cc+dj
            if oob(du, dv) or visited[du][dv] or arr[du][dv] < 0: continue
            if arr[du][dv]>0 and arr[du][dv]!=arr[i][j]: continue

            if arr[du][dv] == 0:
                red_lst.append((du, dv))
            q.append((du, dv))
            visited[du][dv] = 1
    #빨간색 체크 해제
    for r, c in red_lst:
        visited[r][c] = 0
    if len(lst) <2:
        lst = []

    return lst, len(red_lst)
#gravity
    #밑에서부터 -2 찾아서 끌어내릴 숫자 찾으면 끌어내리는 방식
def gravity(arr):
    for c in range(N):
        #밑에서부터 보면서 빈칸이 나오는 순간(r)에 땡겨올 폭탄(0 또는 1~M)(nr) 찾아서 땡기기
        r = N # 1빼고 시작할거라 1부터 시작
        while r>0:
            r -= 1
            if arr[r][c] != -2: continue
            nr = r-1
            while not oob(nr, c) and arr[nr][c] == -2:
                nr -= 1
            #땡겨올 애가 없으면 다음칸 보기
            if oob(nr, c) or arr[nr][c] == -1:
                r = nr
                continue
            arr[r][c] = arr[nr][c]
            arr[nr][c] = -2
    return arr

#oob
def oob(r, c):
    return r<0 or c<0 or r>=N or c>=N

def pr(string):
    print(f"================={string}=============")
    for i in range(N):
        print(arr[i])
    print("=======================================")
    print()
#입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

answer = 0
#while
while 1:
    visited = [[0]*N for _ in range(N)]
    bomb_cand_lst = []
    #1. 폭탄 리스트 찾아서 터질 폭탄 구하기
    #전체 돌며 visited
    for i in range(N-1, -1, -1): #행이 클수록 기준점
        for j in range(N): #열이 작을수록 기준점
            if not visited[i][j] and arr[i][j]>0:
                lst, cnt = bfs(i, j)
                if not lst: continue
                bomb_cand_lst.append((lst, cnt))


    #폭탄 후보 비어있으면 break
    if not bomb_cand_lst:
        break

    bomb_cand_lst.sort(key = lambda x:(-len(x[0]), x[1], -x[0][0][0], x[0][0][1]))
    bomb_lst = bomb_cand_lst[0][0]
    #2. 폭탄 터뜨리기 + 중력
    for r, c in bomb_lst:
        arr[r][c] = -2
    # pr("폭탄 터트린 후 ")

    arr = gravity(arr)
    # pr("1차 중력 후 1!!")
    #3. 회전
    arr = list(map(list, zip(*arr)))[::-1]
    # pr("회전 후")
    #4. 중력
    arr = gravity(arr)
    # pr("마지막 중력 후 ")
    #점수 더하기
    answer += (len(bomb_lst))**2
print(answer)

"""
풀이 시간 :  1시간 20분
1차
실행 시간 :  240 ms
메모리 116060kb

2차 코드개선 : 코드리뷰 때 조언받은 visited clean 방식, 기준 블록 선정 방식 수정
실행 시간 : 224ms
메모리 : 116404kb

3차 코드개선 : 고치고 보니 find_rainbow함수 굳이다 싶어서 없앰 오잉 근데 더 걸리네 ..
실행 시간 : 232ms
메모리 : 115880kb


1416 문제읽기 시작 + 손설계
    기준이나 절차 복사해와서 필요한 부분만 남기는 정리했음
    각 절차별로 어떤 방식으로 구현할지 손으로 설계 + 슈더코드 작성
1419 구현할 부분 주석으로 정리해놓기
    이 과정에서 구현 계획 관련 설명 + 주의사항도 적어두고 해당 파트 문제도 다시 읽어봄

1439 구현시작

1506 중력이동 구현 후 틀려서 print+디버거 활용한 디버깅
    -1일 때는 끌어내리지 않도록 추가처리
    nr 의 초기값+ 선언 위치 문제 발견해서 수정 ! (nr은 끌어내릴 숫자의 위치 가리키는 변수)

1521 디버깅
    점수가 왜 다르지?
    블록별 개수 때문인가해서 그 부분 수정해봄 : 아니었음
    점수 얼마나 추가되는지 print찍어보며 문제 탐색
    sort 조건 다시 살펴봄 무지개 블록개수 누락 발견 => 수정
    무지개블록은 여러블록에 재사용될 수 있음 발견 => 수정

1536 정답

피드백
- 잘한점
    전반적으로 주석을 적을 수 있을 정도로 설계하고 들어감

- 아쉬운점
    무지개블록 놓침..(문제 내용)
    그러다보니 코드에 비효율적인 부분 생김 -> 개선해보자
    행 열을 위, 왼쪽부터 탐색하면 기준 블록은 굳이 정렬하지 않아도 처음 그 i, j가 기준블록임 ;



"""
from collections import deque
def set_block():
    #같은 블록인 기준
    #     - 상하좌우 연결
    #     - 일반블록&무지개블록으로만
    #     - 무조건 일반블록 하나 이상 포함
    #     - 같은 색의 일반블록
    # 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.
    # 기준블록은 정렬해서 찾기
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if arr[i][j]>=1:
                cnt, lst = bfs(i, j, arr[i][j], visited)
                if len(lst)<2:
                    continue
                blocks.append(((i,j),cnt,  lst)) # 0 : 기준 블록 좌표, 1:블록목록

def clean_rainbow(clean_lst, visited):
    for i, j in clean_lst:
        visited[i][j] = 0


def oob(i, j):
    return i>=n or i<0 or j>=n or j<0


def bfs(r, c, color, visited):
    visited[r][c] = 1
    q = deque([(r, c)])
    lst = []
    clean_lst = []
    while q:
        cr, cc = q.popleft()
        lst.append((cr, cc))
        for di, dj in dir:
            du = cr+di
            dv = cc+dj
            if oob(du, dv) or visited[du][dv]:
                continue
            if arr[du][dv] == -1:
                continue
            if arr[du][dv] != 0 and arr[du][dv] !=color:
                continue
            visited[du][dv] = 1
            q.append((du, dv))
            if arr[du][dv] == 0:
                clean_lst.append((du,dv))

    clean_rainbow(clean_lst, visited)
    return len(clean_lst), lst




# #격자 중력 작용 함수 만들기
def gravity():
    # 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
    # (-1 제외하고 아래로 끌어내리기)

    for c in range(n):
        nr = n - 1
        r = n-1
        while r>0:
            if arr[r][c] !=-2:
                r-=1
                continue

            nr = min(r-1, nr)
            while nr>=0 and arr[nr][c]==-2:
                nr -=1


            if arr[nr][c]!=-1 and nr >=0:
                arr[r][c] = arr[nr][c]
                arr[nr][c] = -2

            r-= 1

def rotate_arr():
    return list(map(list, zip(*arr[::-1])))

def find_rainbow(lst):
    result = 0
    for i, j in lst:
        if arr[i][j] == 0:
            result+=1
    return result
#입력받기
dir = (-1, 0), (0, 1), (1, 0), (0, -1)
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

score = 0
while 1:

    #block setting 한다
    blocks = []
    set_block()
    if not blocks:
        break
    # print(blocks)
    #블록 세팅 검증 완료


    # 1. 크기가 가장 큰 블록 그룹을 찾는다.
    blocks.sort(reverse=True, key = lambda x : (len(x[2]), x[1], x[0][0], x[0][1]))
    big_block = blocks[0][2]

    # 2. 1에서 찾은 블록 그룹의 모든 블록을 제거. 점수 += 블록수**2
    score += len(big_block)**2
    for y, x in big_block:
        arr[y][x] = -2


    # 3. 격자에 중력이 작용
    gravity()

    arr = list(map(list, zip(*arr)))[::-1]

    gravity()

print(score)



