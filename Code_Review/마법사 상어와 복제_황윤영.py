"""
총 풀이시간 1시간 38분
1차 시도
실행시간
메모리

리팩토링
실행시간
메모리

0900 문제 읽기 시작
    - 단계가 명시돼있어서 주석으로 복사해서 하나씩 뜯어보고, 중요한 조건 남겨놓음
    - 물고기 / 상어 / 냄새 세 종류나 있어서 각각을 어떻게 관리할지 고민
    - 종이에는 주의할 것들 별표하며 적었고, 단계별로 적으면서 그 단계를 어떻게 구현할지,
        그 때의 주의점, 물고기/상어/냄새를 뭘로 두고 관리할 지 등을 적어둠

0920 구현할 영역 나눠서 주석 정리 (구현할 단계, 방법+ 주의점)

0924 구현 시작
    - 계획한대로 구현 시작
    - 처음엔 물고기, 물고기 냄새, 상어를 한 배열에 다 넣고 구현하려고 시도 햇으나
    - 구현하다 중간에 배열크기 4인 것도 실수할까봐 N에 넣어두기..
    - oob 쓸 단계 많으니까 함수화 햇음
    - 물고기 이동 시 냄새 / 상어 존재를 체크하는 단계에서 한 배열에 넣으면
        굳이 필요없는 물고기도 매번 체크해야함을 깨닫고 물고기만 lst에 저장하는 방식으로 바꿈
    - lst에 저장돼있는 물고기 값을 수정하는 식으로 물고기 이동 초기 구현 (추후 변경됨,,)
    - 중간중간 그 줄이 의미하는

0936 상어 이동 구현시작
    - dfs 선택 / 사전순임을 반영하기 위해 max는 반드시 클 때만(같을 때 x) 갱신할 것 주의하려고 함
    - 상어이동 구현하려다가 상어는 하나기 때문에 굳이 배열에 넣어둘 필요 없겠구나 하고 깨달아서 변수 형식으로 바꿈
    - 먹을 물고기도 배열에 3차원으로 관리하는게 편하다고 다시 생각이 들어 물고기 배열로 변환
    - 처음엔 물고기 dfs에서 바로 죽일뻔; 개수만 세면 됐다 ..1 (가 아니었다 디버깅하며 깨달음)

0953 냄새 삭제 / 복제된 물고기 반영 구현 + 물고기 이동 수정
    - 여긴 어렵진 않았다
    - 물고기 배열형식으로 바꾸면서 물고기 이동도 tmp 배열 만들어서 저장해두고 반영하는 방식으로 코드 수정

1003 테케 테스트 및 디버깅 시작
    - 시작하자마자 인덱스 에러 => 시작 인덱스가 1인것 놓침 바로 알고 수정
    - 테케가 하나도 안맞길래 단계별 프린트 디버깅 시작
    - 초기 물고기 위치에서 물고기가 이동을 안한다? 물고기 이동 불가 조건 틀린 것 발견하여 수정
    - 상어의 이동이 나랑 다르다? => dfs에서 상어가 갱신될 때의 조건들 프린트 디버깅해봄
    - 이미 먹은 물고기가 안사라져서 또 먹는 걸로 카운트하는 문제 발견해서 배열 복사하여 지워서 해결
    - (지금 생각하니 배열복사보다 그냥 visited를 썼으면 좋았겠다 ...
        그리고 이 과정을 dfs for문에서 방향 고를 때 했으면 더 빨랐겠다 리팩토링 하자 ..)
    - 특정 테케에서 또 인덱스 에러 발생
        - 상어 인덱스 -1 안한 것 발견
        - 그래도 발생
        - dfs 결과 후 상어 좌표 출력
        - 음수가 나온다 이상하게 ;;?
        - 자꾸 상어 움직임으로 상상상 나온 게 이상해서 dfs 로직+프린트 꼼곰히 살핌
        - ㅇ ㅏ.. max 갱신할 때 등호 안넣어놓고 초기값 0 설정한게 화근이었음
        - 0일 때 selected가 갱신이 안돼 ㅠㅠ  => 수정해서 해결
    - 물고기 / 상어 이동 잘함 확인했는데 또 안돼서 냄새 부분 살펴봄
        - 냄새 rank를 올리지 않고 물고기 냄새가 추가되어 오류가 발생했을 것을 깨달음
        - 상어가 물고기를 죽이고 냄새를 0번rank에 올리기 전에, rank를 위로 밀어올려주기
1038 정답

피드백
- 잘한점
    1. 목표했던 대로 미리 구현할 단계+주의점을 단계에 정리해두어 조금이지만 실수를 줄였을지도..
    2. 프린트 디버깅을 꽤나 깔끔하게 쓰기 시작한듯ㄱ..?
        그리고 에러 보고, 테케랑 비교해보고, 어딜 봐야 할 지 찾는 속도가 조금씩 빨라진 것 같기도
    3. 중간 주석을 달아놔서 수정할 게 있을 때 빠르게 찾아갈 수 있었음
- 개선할 점
    1. 오늘 중간체크 진짜 안했다 ;; 실수 더 많이 했으면 못 헤어나왔을지도 모른다는 생각이 듦
        그래도 문제 꼼꼼히 읽고 이해해서 빠르게 잡을 수 있었음,,
    2. 중간 시간을 많이 안봤다
        시간 분배에 좀 더 신경을 써봐야할듯





좌 좌상 상 우상 우 우하 하 좌하
(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1,0), (1, -1)


1. 모든 물고기에게 복제 마법
    5번에서 물고기가 복제되어 칸에 나타난다.
2. 모든 물고기가 한 칸 이동
 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동불가
 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을
 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다.


3. 상어가 연속해서 3칸 이동
 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다.
 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다.
 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면,
 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다.
 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며,
 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다.
 사전 순에 대한 문제의 하단 노트에 있다.

4. 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.

5. 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.




"""


def oob(i, j):
    return i < 0 or i >= N or j < 0 or j >= N


def fish_print():
    for i in range(N):
        for j in range(N):
            print(fish_arr[i][j])
        print()


def smell_print():
    for i in range(N):
        for j in range(N):
            print(smell_arr[i][j])
        print()


def dfs(level):
    global move, max_fish
    if level == 3:
        # print('============dfs 종료 체크 ========')
        # print(selected)
        # 사전 순으로 갱신
        # 죽일 수 있는 물고기 체크
        r, c = sr, sc  # 상어 초기 위치
        cnt = 0
        erase = [[[0] * 3 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                erase[i][j] = fish_arr[i][j][:]
        for d in selected:
            di, dj = shark_d[d]
            r += di
            c += dj

            # print("dfs 속 상어 이동 체크")
            # print(r, c)
            if oob(r, c):
                # print("범위 아웃")
                return
            # 물고기 수 cnt
            cnt += len(erase[r][c])
            erase[r][c] = []
        # print("cnt : ", cnt)
        # print("max_fish: ", max_fish)
        if cnt > max_fish:
            max_fish = cnt
            move = selected[:]
        return

    for i in range(4):
        selected[level] = i
        dfs(level + 1)


# input
M, S = map(int, input().split())
N = 4
smell_arr = [[[0] * 3 for _ in range(N)] for _ in range(N)]
fish_arr = [[[] for _ in range(N)] for _ in range(N)]
directions = (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)
shark_d = (-1, 0), (0, -1), (1, 0), (0, 1)
# fish_lst = []
for m in range(M):
    r, c, d = map(int, input().split())
    fish_arr[r - 1][c - 1].append(d - 1)
    # fish_lst.append([r, c, d-1])
sr, sc = map(int, input().split())
sr -= 1
sc -= 1
# print("초기 상어 위치 : ", sr, sc)
# arr[sy][sx].append([1])
for s in range(S):
    # 1. 모든 물고기에게 복제 마법
    #     물고기 탐색해서 복제 lst에 넣어두고 5에서 뿌릴것
    copy_lst = []
    # copy_lst = fish_lst[:]
    for i in range(4):
        for j in range(4):
            lst = fish_arr[i][j]
            for d in lst:
                copy_lst.append([i, j, d])

    # 2. 모든 물고기가 한 칸 이동
    #     상어 / 물고기 냄새 / 격자 범위 체크하기
    #     동시 이동이므로 tmp배열 만들기 취소취소 물고기 리스트로 관리하면 상관없을듯 .!
    #     방향 반시계 회전 (d-1)%8
    tmp_fish = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for w in range(len(fish_arr[r][c])):  # 이 칸에 있는 물고기들을
                # 그 방향부터 반시계 회전한 방향까지 돌리며 이동 가능한지 체크
                d = fish_arr[r][c][w]
                # print("이 물고기 이동할거야 ")
                # print(r, c, d)
                for k in range(8):
                    new_d = (d - k) % 8
                    di, dj = directions[new_d]
                    du = r + di
                    dv = c + dj
                    # print("다음 고려 위치 : ", du, dv)

                    if oob(du, dv):  # 범위
                        # print("범위 아웃돼서 그대로")
                        continue
                    # if smell_arr[du][dv]: #물고기냄새 존재
                    #
                    #     continue
                    smell_flag = False
                    for u in range(3):
                        if smell_arr[du][dv][u] != 0:
                            smell_flag = True
                            break
                    if smell_flag:
                        # print("냄새 있음 ㅠ ")
                        continue
                    if du == sr and dv == sc:
                        # print("상어 ㅠㅠ")
                        continue
                    tmp_fish[du][dv].append(new_d)  # 물고기 이동
                    break
                else:
                    tmp_fish[r][c].append(d)

    # 동시 이동
    for i in range(N):
        for j in range(N):
            fish_arr[i][j] = tmp_fish[i][j][:]

    # print("=============물고기 한 칸 이동 ==========")
    # fish_print()

    # 3. 상어가 연속해서 3칸 이동
    #    3칸 순서는 combination으로. 상좌하우 순.
    #    사전 순으로 앞서는 것 우선이므로 갱신할 때 등호 안넣기
    #   max_fish 값은 for문 돌아올 때마다 새로 0으로 갱신해둬야함
    #   제외된 물고기 [0, d] 를 [2, rank(초기값 1)]로 바꿔 넣기

    # 상어가 이동할 칸 뽑아오자
    max_fish = -1
    selected = [0] * 3
    move = [0] * 3
    dfs(0)

    # print("상어 움직임 ")
    # print(move)
    # print()

    #냄새 올리기
    for i in range(N):
        for j in range(N):
            smell_arr[i][j][2] = smell_arr[i][j][1]
            smell_arr[i][j][1] = smell_arr[i][j][0]
            smell_arr[i][j][0] = 0
    # move에 있는 대로 움직이기
    for d in move:
        di, dj = shark_d[d]
        sr += di
        sc += dj
        # print("sr, sc : ", sr, sc)
        # 물고기 냄새 남기고 죽이기

        for k in range(len(fish_arr[sr][sc])):
            smell_arr[sr][sc][0] += 1
        fish_arr[sr][sc] = []
    # print()
    # print("==============상어 움직인 후 위치 ===========")
    # print(sr, sc)
    #
    # print()
    # print("============상어 움직인 후 물고기 ===========")
    # fish_print()

    # print("================상어 움직인 후 냄새 ===========")
    # smell_print()
    # 4. 물고기 냄새 삭제
    #   물고기 냄새 돌면서 rank ==2 인 것 삭제
    #   아니면 rank +1 시키기
    for i in range(N):
        for j in range(N):
            smell_arr[i][j][2] = 0
            # smell_arr[i][j][1] = smell_arr[i][j][0]
            # smell_arr[i][j][0] =
            # 물고기 냄새 텀 올려놓기
            # for k in range(2):
            #     smell_arr[i][j][k + 1] = smell_arr[i][j][k]
            # smell_arr[i][j][0] = 0
    #  5. 1에서 담아둔 lst 배열에 뿌리기
    for fish in copy_lst:
        r, c, d = fish
        fish_arr[r][c].append(d)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(fish_arr[i][j])
print(answer)
