"""
1차
풀이 시간 : 1시간 2분
시도 횟수 : 1회
실행 시간 : 868 ms
메모리 : 114940 kb

2차
풀이 시간 : 1시간 + 부분리셋 + 1시간 + 리셋 + 48분
시도 횟수 : 엄처어어엉 많이
실행 시간 : 276 ms
메모리 : 115480 kb

- 실수 모음
    - 설계 실수. lst index로 탐색하는데 함부로 없애면 안된다 ! 중력 밀기 사용했어야함
    - 연속인 개수 찾는 로직 연결해서 해보려다가 대차게 실패!

"""
"""
=============================== 2차 코드 리뷰 ==============================
총평
1시간 
    - 설계 후 디버깅 실패 
    - 달팽이를 펼쳐서 1차원 리스트에 넣어두다 보니 디버깅이 어려웠음. 
    - lst를 매번 리셋하는 과정에서 끝에가 잘 안들어감.............
1시간 
    - 리셋, 부분리셋 고민
    - 달팽이 부분은 잘 돼서 그 뒤 싹 밀기로 결심하고 새로 구현
    - 기존 설계 유지하다보니 비슷한 문제 반복,, 
    - 해결 후 제출 메모리 초과
    - 중력 배열 붙이는 부분이 문제인가 싶어서 다시 했으나 또 메모리 초과
    - 매번 리스트를 새로 만들고 갈아끼우는게 문제일 것 같아 아예 설계 엎기로 함
48분
    - 기존 배열을 달팽이 루트를 따라 꺼내오고 바꾸기로 함;; 
    - 성공 ㅠㅠ..........
    
왜 왜 왜 왜ㅗ애왜왜왱 그래 
진짜 모의때 고생한 문제보다 수월하게 푼 문제에서 재풀이 때 고생하는듯.. 
뭔가 뇌가 팽팽 안돌아가는 느낌 ,, 
리셋하길 잘했고,, 초반 설계 때 디버깅 난이도까지 같이 고민하자 ㅏ.


"""
"""

n x n으로 이뤄진 나선형 미로
1. 플레이어는 상하좌우 방향 중 주어진 공격 칸 수만큼 몬스터를 공격하여 없앨 수 있습니다.
2. 비어있는 공간만큼 몬스터는 앞으로 이동하여 빈 공간을 채웁니다.

3. 이때 몬스터의 종류가 4번 이상 반복하여 나오면 해당 몬스터 또한 삭제됩니다. 해당 몬스터들은 동시에 사라집니다.
    삭제된 이후에는 몬스터들을 앞으로 당겨주고,
    4번 이상 나오는 몬스터가 있을 경우 또 삭제를 해줍니다.
    4번 이상 나오는 몬스터가 없을 때까지 반복해줍니다.

4. 삭제가 끝난 다음에는 몬스터를 차례대로 나열했을 때 같은 숫자끼리 짝을 지어줍니다.
    이후 각각의 짝을 (총 개수, 숫자의 크기)로 바꾸어서 다시 미로 속에 집어넣습니다.
    새로 생긴 배열이 원래 격자의 범위를 넘는다면 나머지 배열은 무시

1과 3 과정에서 삭제되는 몬스터의 번호는 점수에 합쳐집니다.
모든 라운드가 끝난 후 플레이어가 얻게되는 점수

"""


# 달팽이 준비 함수
def make_route_arr():
    r, c = N // 2, N // 2
    l = 1
    cnt = 0

    while 1:
        for di, dj in (0, -1), (1, 0), (0, 1), (-1, 0):
            for t in range(l):
                r+=di
                c+=dj
                route_lst.append((r, c))
                if r==0 and c==0:
                    return
            cnt+=1
            if cnt==2:
                l+=1
                cnt=0


# 배열 당기는 함수
def pull_arr():
    for i in range(N*N-1):
        r, c = route_lst[i]
        #당길 숫자 찾기 !!
        if arr[r][c] ==0:
            nk = i+1
            while nk<N*N-1:
                nr, nc = route_lst[nk]
                if arr[nr][nc] !=0:
                    break
                nk+=1
            if nk<N*N-1 and arr[nr][nc]!=0:
                arr[r][c] = arr[nr][nc]
                arr[nr][nc] = 0
            else:
                return


# 같은 숫자 탐색해서 개수 반환
def find_cnt(i):
    r, c = route_lst[i]
    num = arr[r][c]
    cnt = 1
    for j in range(i+1, N*N-1):
        nr, nc = route_lst[j]
        if num != arr[nr][nc]:
            return cnt
        cnt+=1
    return cnt

# 입력
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
route_lst = []
make_route_arr()
DIR = (0, 1), (1, 0), (0, -1), (-1, 0)
sr,sc = N//2, N//2
answer = 0

for m in range(M):
    d, p = map(int, input().split())
    di, dj = DIR[d]
    nr, nc = sr, sc

    #1번 죽이기
    for t in range(p):
        nr+=di
        nc+=dj
        if nr<0 or nc <0 or nr>=N or nc>=N: continue
        answer += arr[nr][nc]
        arr[nr][nc] = 0
    #죽인후 당기기
    pull_arr()

    while 1:
        flag = False
        for i in range(N*N-1):
            cr, cc = route_lst[i]
            if arr[cr][cc]==0: continue
            cnt = find_cnt(i)
            if cnt>=4:
                for t in range(cnt):
                    r, c = route_lst[i+t]
                    answer += arr[r][c]
                    arr[r][c] = 0
                    flag = True
        if not flag:
            break

        pull_arr()

    #숫자 새로 매기기
    new_lst = []
    for i in range(N*N-1):
        r, c = route_lst[i]
        if arr[r][c] ==0: continue
        cnt = find_cnt(i)
        new_lst.extend([cnt, arr[r][c]])
        if len(new_lst)>=N*N-1:
            new_lst = new_lst[:N*N]
            break
        for t in range(cnt):
            nr, nc = route_lst[i+t]
            arr[nr][nc] = 0



    arr = [[0]*N for _ in range(N)]
    for i in range(len(new_lst)):
        nr, nc = route_lst[i]
        arr[nr][nc] = new_lst[i]
print(answer)

"""
코드리뷰

총 풀이시간 1시간 2분
실행시간 868 ms
메모리 114940 kb

1523 문제 읽기 시작 / 구상
    주사위 윷놀이로부터 1시간 만에 도망침
    일단 읽기
    문제조건 정리 (종이)
    대략적인 설계 종이에 메모
1528 구현 시작
    입력 우선 받고
    함수화할 파트, 구현할 파트 자리 남기고 주석으로 정리
    그리고 구현하면서 채워갔음
    단계별로 중간 확인 하며 디버깅 함께 함
1602 구슬폭발 디버깅
    arr '====' 으로 구분해서 프린트 해가며 단계적으로 그림이랑 어디가 어떻게 다른지 체크
    비교하면서 문제도 다시 읽음
    연속인 것의 개수를 세는 부분을 함수화 해서 구슬 폭발에 재수정하며 구슬폭발  로직 수정

1625 정답처리

피드백
- 잘한점
    함수화 굿
    달팽이 능숙해진 것 같다. 좀 더 템플릿 확고하게 가져가자
- 아쉬운 점
    밀거나 당기는 로직 항상 템플릿화가 아니라 그 때 생각해서 한다 ;
    좀 더 반복해ㅠㅠ





"""

def fill_point_lst():
    sr, sc = N//2, N//2
    cnt = 0
    l = 1
    # idx = 1
    # idx_arr[sr][sc] = idx
    # idx+=2
    point_lst.append((sr, sc))
    for k in range(N//2+1):
        for di, dj in (0, -1), (1, 0), (0, 1), (-1, 0):
            for i in range(l):
                sr+=di
                sc+=dj
                # idx_arr[sr][sc] = idx
                # idx+=1
                point_lst.append((sr, sc))
                if sr==0 and sc==0:
                    return
            cnt+=1
            if cnt==2:
                l+=1
                cnt=0

def find_continuous(k):
    # 이점에서 연속인 것 찾기
    y, x = point_lst[k]
    if ball_arr[y][x] == 0:
        return k
    num = ball_arr[y][x]
    ed = k + 1
    while 1:
        if ed >= N * N:
            break
        dy, dx = point_lst[ed]
        if ball_arr[dy][dx] != num:
            break
        ed += 1
    return ed

def bomb():
    global answer
    flag = False
    # . 폭발하는 구슬은 4개 이상 연속하는 구슬이 있을 때 발생한다.
    # while문으로 끝점 찾기 . st, ed 구해서 0만들기
    # 한번도 폭발 안했으면 return
    for k in range(1, N*N-4):
        ed = find_continuous(k)
        y, x = point_lst[k]
        num = ball_arr[y][x]
        if ed == k:
            continue
        if ed-k >=4:
            answer += num*(ed-k)
            for j in range(k, ed):
                u, v = point_lst[j]
                ball_arr[u][v] = 0
            flag= True
    if flag:
        pull_ball()
        bomb()
    return False

def pull_ball():
    k = 1
    while k < N * N - 1:
        y, x = point_lst[k]
        if ball_arr[y][x] == 0:
            nk = k + 1
            # 땡겨올 지점 찾기
            while nk < N * N:
                dy, dx = point_lst[nk]
                if ball_arr[dy][dx] != 0:
                    break
                nk += 1
            ball_arr[y][x] = ball_arr[dy][dx]
            ball_arr[dy][dx] = 0
        k += 1

def change_ball():
    tmp = [[0] * N for _ in range(N)]
    k = 1
    idx = 1
    while k < N * N:
        ed = find_continuous(k)

        cy, cx = point_lst[k]
        num = ball_arr[cy][cx]
        if num==0:
            break
        cnt = ed - k
        y, x = point_lst[idx]
        tmp[y][x] = cnt
        idx += 1
        if idx == N * N:
            break
        y, x = point_lst[idx]
        tmp[y][x] = num
        idx += 1
        if idx==N*N:
            break
        k =ed
    for t in range(N):
        ball_arr[t] = tmp[t][:]


N, M = map(int, input().split())
# idx_arr = [[0]*N for _ in range(N)]
ball_arr = [list(map(int, input().split())) for _ in range(N)]
point_lst = []
#달팽이 모양 돌며 point_lst 만들기
fill_point_lst()
#d값에 따른 방향 (위 아래 좌 우)
dir = (-1, 0), (1, 0), (0, -1), (0, 1)

r, c = N//2, N//2
answer = 0
# print(len(point_lst))
#구술 깨부시기
for m in range(M):
    d, s = map(int, input().split())
    di, dj = dir[d-1]
    #구슬 깨부시기
    for t in range(1, s+1):
        du = r+di*t
        dv = c+dj*t
        if du<0 or dv<0 or du>=N or dv>=N:
            break
        ball_arr[du][dv] = 0
    # print("구슬 깨기 확인")
    # for i in range(N):
    #     print(ball_arr[i])
    # print()
    #point_lst순으로 돌며 0인 곳이 있으면 while 0이 아닌 곳까지 가서 당겨오자!
    pull_ball()
    # for i in range(N):
    #     print(ball_arr[i])

    #구슬 채우기 확인 완료
    bomb()
    #구슬 폭발 : 재귀로 해야겠다


    #구슬 변화
    change_ball()

    # print("=======================")
    # for i in range(N):
    #     print(ball_arr[i])
    # print()
print(answer)