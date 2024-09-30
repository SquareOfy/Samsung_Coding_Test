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