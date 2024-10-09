"""
총 풀이시간 1시간 49분
1차
시간 728 ms
메모리 126956 kb

리팩토링
- blow 함수 불필요. 수정하자 => 막상 보니 이게 더 나은 것 같기도? 그냥 두기 ..
- 매번 온풍기가 이동하는 모습은 똑같다! 이거 저장해두자
시간 248 ms
메모리 113996 kb


???1456???(주사위굴리기 제출시간,,)  문제 읽기 시작 : 으악 다른 창에 시간이 가려졌다 ..............................
    - 처음 문제를 보고 딱봐도 복잡(온풍기가 퍼져나가는 모양과 사이사이 벽;;과 같은요소)해서 다음부터 품(좋은 판단)
    - 온풍기가 퍼져나가는 모양, 방법에 대한 이해는 쉬웠음
    - 벽 관련 내용 보자마자 구현 어떻게 하지 고민됨
    - 어제 오늘 풀었던 문제에서 계속 동시에 적용해야하는 부분을 당장 적용해서 디버깅에 실수한 경험이 쌓여,
        인접 온도 조절 동시 라는 단어 보자마자 파워 메모 해놓고 주의하려고 함
    - 문제 읽으면서 문제의 조건이 다양하고 많아서 어느거 하나 놓칠까 조마조마했음 => 결국 실수 꽤나 함;


1507 구현할 내용 주석 정리 + 바람 나올 때 벽 처리 구상
    - 구현할 단계가 매우 많으므로 까먹지 않기 위해 미리 주석으로 코드 작성할 영역 지정해놓음
    - 이 때 함수로 구현할 내용까지 함께 지정해놨으면 왔다갔다 하느라 정신 없는 상황도 줄고,
        그럼 실수도 줄일 수 있지 않았을까 생각;;
    - 벽 처리 구상은 도무지 깔끔하게 할 자신 없어서 하드코딩하기로 결심함 ..^^

1522 온풍기 바람 나오는거 구현시작 / 비교적 쉬운 while문 종료조건 구현
    - 처음엔 함수로 설계하지 않았는데 온도 5부터 1까지 점점 3칸씩 늘어나는 모양이
    - 재귀가 적절하다고 중간에 판단되어 함수 구현으로 수정
    - (지금 생각해보니 sys.set~ 필요한지 생각 또 안해봤었네 ,,)
    - 첫 칸 이동을 blow로 거기서부터 3개씩 펼쳐나가는 함수를 blow_split으로 구현
        - 굳이 blow 함수 없이 아래서 한칸 이동해보고 blow_split() 바로 호출했어도 괜찮았을듯
        - 함수를 구현하면서 그때그때 필요하면 매개변수 추가하는 습관 별로인듯,
        - 설계 부족이 여기서 느껴짐. 처음부터 이 함수의 동작과 그에 필요한 매개변수 세팅 생각하자
    - 하도 문제 복잡+뒤에도 범위체크할 구간이 꽤 있음을 생각하고 평소 사용 안하던 oob 함수 활용
    - 구현 완료 후 테스트 했는데 이상한 곳에 막 벽이 생기고,, 있던 벽은 안생기고,,!!
        - 코드 다시읽기 시도 -> temp 배열에 넣어야 하는데 arr 배열에 넣은 오타 발견
        - 여러번 더하는 문제 발견 -> visited 처리로 해결
        - 어딘가 구멍이 뚫린다,, 벽이 잇는 것처럼 온도가 안오르는 문제
            - 미친듯이 코드 뜯어보기 + 문제 다시 읽기 + 벽 잘 들어갔는지 체크+ 어디가 구멍이 뚫리는지 분석 + 디버거 = 원인 발견
            - 좌일 때만, 우일때만 벽 체크하도록 로직 추가함
1613 : 바람 불기 끝 온도조절 /바깥온도 구현시작
    - 동시에! 매우 강조한 덕에 바로 tmp 배열 만들어서 반영
    - 이때 temp 배열 또 arr로 씀(자주 사용하지 않던 변수명의 폐해)
    - 구현 완료후 테스트했더니 또 안맞음
    - print 디버깅 중 음수 발견. 띠용. 바깥온도 감소할 때 음수 되면 0 으로 만드는 처리 안한 것 발견 후 수정

1620 : 본격적인 디버깅의 시작
    - 테케가 안맞아서 단계별로 보려고(어디가 문제인지,,) 단계 끝날 때마다 온도 배열 출력해봄
    - min -> max, 1 -> 0 오타 수정
    - 하나를 해결하면 다른 하나가 터진다 엉망진창 실수투성이 코드(하지만 다 찾았쮸 ..? )
    - 온도조절 때 벽 체크 안한 것 발견 ! 바로 적용!!
    - 그래도 안맞죠 ..?
    - 테케 딱 하나인가가 안맞다.  다시 코드 문제랑 맞춰가며 조건 빠뜨린 것 없는지 뜯어봄
    - 테케 규모가 너무 커서 찾기가 어렵다
    - 디버거의 condition 조절하는 것 활용해서 딱 53일 때 테케 답이랑 비교해봄
    - 뭔가 요상하게 다르다... 다시 코드 뜯어보기
    - 외곽 1 뺄 때 네 꼭짓점 중복해서 뺏다는 사실 알아차리고 수정
1645 제출 그리고 정답


오늘의 피드백
- 잘한점
    1. 디버거 활용능력이 좋아졌다?
        대체로 테케 규모나 동작 횟수가 커서 세부동작을 print로는 찾아내기 어려울 때 활용하기 좋은듯
    2. 중간 체크를 그래도 하려고 계속 함
        단계가 너무 많을 땐 꼭꼭! 근데 그래도 실수투성이였다... 다음부턴 중간체크 확실히 하고 가자
    3. print 디버깅과 디버거의 적절한 조합 디버깅
        단계 살필 땐 print
        세부동작 살필 땐 디버거
    4. 함수 잘 활용함
        oob같이 평소에 잘 사용 안했지만 자주 오타를 내는 부분이기도 하고 자주 등장할 것 같아 사용
        앞으로 꾸준히 사용해보자. 왜? 오타 자주내니까 ^^ .. 확인 한군데에서만 할 수 있도록 !
- 못한점
    1. 문제 조건 왜 놓치냐고
        읽었잖아... 왜 놓치냐고...벽체크 왜 안하냐고...
        => 개선방향 : 중요한 조건, 자주 놓치는 그런 조건은 종이가 아니라 주석으로 적자.
                     디버깅에 초집중하다보면 종이에 눈이 안간다...
                     주석으로 코드 구현할 영역을 미리 적어두고 그곳에 거기 구현하면서 주의해야할 점 미리 적어보기
    2. 논리 빈틈이 많다
        - visited를 미리 체크할 생각 못한 것
        - 외곽 꼭짓점 겹치는 것 파악 못한 것
    3. 오타는... 어쩔 수 없다 뇌를 더 챙겨서 문제풀기

"""

"""
주의사항
- R,C
- 온풍기 바람 이동 시 벽 (대각도 벽에 막힘)
- 온도 조절은 동시에
"""


def higher_k():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 5 and temp[i][j] < K:
                return False
    return True


def oob(r, c):
    return r < 0 or r >= R or c < 0 or c >= C


def blow(r, c, d):
    dir = directions[d]
    di, dj = dir[1]
    # 5부터 시작
    nr = r + di
    nc = c + dj
    tmp[nr][nc] += 5
    visited[nr][nc] = 1
    blow_split(nr, nc, dir, d, 4)


def blow_split(r, c, dirs, d, k):
    if k == 0:
        return
    for di, dj in dirs:
        nr = r + di
        nc = c + dj
        if oob(nr, nc):
            continue
        if visited[nr][nc]:
            continue
        # 벽 체크
        # 직선 방향이면
        if di == 0 or dj == 0:
            if d in wall[r][c]:
                continue
        # 좌우를 보고 있고 대각일 때
        elif d % 2 != 0:
            # 상 우 하 좌
            if r - 1 >= 0 and di == -1 and (2 in wall[r - 1][c] or d in wall[r - 1][c]):
                continue
            if r + 1 < R and di == 1 and (0 in wall[r + 1][c] or d in wall[r + 1][c]):
                continue
        # 상하를 보고 있고 대각일때
        else:
            if c - 1 >= 0 and dj == -1 and (1 in wall[r][c - 1] or d in wall[r][c - 1]):
                continue
            if c + 1 < C and dj == 1 and (3 in wall[r][c + 1] or d in wall[r][c + 1]):
                continue

        tmp[nr][nc] += k
        visited[nr][nc] = 1
        blow_split(nr, nc, dirs, d, k - 1)


R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
wall = [[[] for _ in range(C)] for i in range(R)]
temp = [[0] * C for _ in range(R)]

# 해당 칸에서 벽이 있어서 못가는 칸 기록
for w in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        wall[x][y].append(0)
        wall[x - 1][y].append(2)
    else:
        wall[x][y].append(1)
        wall[x][y + 1].append(3)

#머신 저장
machine = []
dir_idx = [0, 1, 3, 0, 2] #내가 사용할 방향 순서대로 d값 변환해줄 용도
for i in range(R):
    for j in range(C):
        if arr[i][j] != 0 and arr[i][j] != 5:
            d = dir_idx[arr[i][j]]
            machine.append((i, j, d))

answer = 0
# 방향 상우하좌 별로 퍼지는 곳
directions = ((-1, -1), (-1, 0), (-1, 1)), \
    ((-1, 1), (0, 1), (1, 1)), \
    ((1, -1), (1, 0), (1, 1)), \
    ((-1, -1), (0, -1), (1, -1))
# wind 가는 모양 온풍기 별로 저장
wind_arr = []

for i, j, d in machine:
    tmp = [[0] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    blow(i, j, d)
    wind_arr.append(tmp)

tmp = [[0] * C for _ in range(R)]

while 1:
    answer += 1

    #저장해둔 온풍기 별로 온도 올리기
    for i in range(len(machine)):
        for r in range(R):
            for c in range(C):
                temp[r][c] += wind_arr[i][r][c]


    # 온도 조절 #임의 배열 만들어서 동시에 반영
    for i in range(R):
        for j in range(C):
            for di, dj in (1, 0), (0, 1):
                if (di, dj) == (1, 0) and 2 in wall[i][j]:
                    continue
                if (di, dj) == (0, 1) and 1 in wall[i][j]:
                    continue
                ni = i + di
                nj = j + dj
                if oob(ni, nj):
                    continue

                gap = abs(temp[i][j] - temp[ni][nj]) // 4
                if temp[i][j] < temp[ni][nj]:
                    tmp[i][j] += gap
                    tmp[ni][nj] -= gap
                else:
                    tmp[i][j] -= gap
                    tmp[ni][nj] += gap
    for i in range(R):
        for j in range(C):
            temp[i][j] += tmp[i][j]
            tmp[i][j] = 0

    # 바깥 온도 1씩 감소
    for i in range(1, R - 1):
        temp[i][0] = max(temp[i][0] - 1, 0)
        temp[i][C - 1] = max(temp[i][C - 1] - 1, 0)
    for j in range(1, C - 1):
        temp[0][j] = max(temp[0][j] - 1, 0)
        temp[R - 1][j] = max(temp[R - 1][j] - 1, 0)
    temp[0][0] = max(temp[0][0] - 1, 0)
    temp[0][C - 1] = max(temp[0][C - 1] - 1, 0)
    temp[R - 1][0] = max(temp[R - 1][0] - 1, 0)
    temp[R - 1][C - 1] = max(temp[R - 1][C - 1] - 1, 0)

    # 온도 조사(5인 칸이 모두 K 이상)
    if higher_k() or answer >= 101:
        break

print(answer)
