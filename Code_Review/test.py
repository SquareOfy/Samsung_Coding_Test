# 0932 풀이 시작
# 1, 1 시작

# 종료(출력값)
# 게임이 끝났을 때 각 산타가 얻은 최종 점수를 1번부터 P번까지 순서대로 공백을 사이에 두고 출력합니다.

# 함수화
# 1. 거리 계산하기
# 2. 루돌프 움직이기
# 3. 산타 움직이기
# 4. 충돌하기
# 5. 상호작용하기

# 흐름 -> 루돌프, 충돌, 상호작용, 산타, 충돌, 상호작용이니까 주의

# 자료 구조 선택
# 산타 죽었는지 확인해야 하니까 기절, 사망 배열 만들자
# 산타 맵에 라벨링
dr = [-1, 0, 1, 0, -1, 1, -1, 1]  # 상우하좌 우선순위에 맞춰 움직입니다.
dc = [0, 1, 0, -1, 1, 1, -1, -1]


def oob(r, c):
    return r < 0 or r >= N or c < 0 or c >= N


def cal_dist(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2


def Rmove():
    min_dist = INF
    Sr, Sc = 0, 0  # 가장 가까운 산타 위치
    for i in range(1, P + 1):
        if survived[i] == -1: continue  # 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택해야 합니다.
        r, c = santas[i]

        cur_dist = cal_dist(Rr, Rc, r, c)
        # r 좌표가 큰 산타를 향해 돌진합니다. r이 동일한 경우, c 좌표가 큰 산타를 향해 돌진합니다.
        if min_dist > cur_dist or min_dist == cur_dist and (Sr, Sc) < (r, c):
            min_dist = cur_dist
            Sr, Sc = r, c

    min_dist2 = cal_dist(Rr, Rc, Sr, Sc)
    nRr, nRc, Rdir = 0, 0, 0  # 다음 루돌프의 위치

    for i in range(8):
        nr, nc = Rr + dr[i], Rc + dc[i]
        if oob(nr, nc): continue

        cur_dist2 = cal_dist(nr, nc, Sr, Sc)

        # 가장 우선순위가 높은 산타를 향해 8방향 중 가장 가까워지는 방향으로 한 칸 돌진합니다.
        if min_dist2 > cur_dist2:
            min_dist2 = cur_dist2
            nRr, nRc, Rdir = nr, nc, i

    if arr[nRr][nRc]:  # 산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생합니다.
        S_num = arr[nRr][nRc]
        survived[S_num] = m  # 산타는 기절합니다.
        score[S_num] += C  # 해당 산타는 C만큼의 점수를 얻게 됩니다.

        nSr, nSc = nRr + C * dr[Rdir], nRc + C * dc[Rdir]  # 밀려난 산타 위치
        arr[nRr][nRc] = 0  # 산타 밀려나니까 비워두자
        interaction(S_num, nSr, nSc, Rdir)

    return nRr, nRc


def Smove():
    for i in range(1, P + 1):  # 산타는 1번부터 P번까지 순서대로 움직입니다.
        if survived[i] == -1 or m - survived[i] < 2: continue  # 기절했거나 이미 게임에서 탈락한 산타는 움직일 수 없습니다.
        Sr, Sc = santas[i]
        min_dist = cal_dist(Sr, Sc, Rr, Rc)
        nSr, nSc, Sdir = Sr, Sc, -1
        for j in range(4):
            nr, nc = Sr + dr[j], Sc + dc[j]
            if oob(nr, nc) or arr[nr][nc]: continue  # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
            if min_dist > cal_dist(nr, nc, Rr, Rc):  # # 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않습니다.
                min_dist = cal_dist(nr, nc, Rr, Rc)
                nSr, nSc, Sdir = nr, nc, j
        arr[Sr][Sc] = 0  # 이동할 수 있다는 말이니까 기존 위치 비워두고

        if (nSr, nSc) == (Rr, Rc):  # 산타가 루돌프한테 갖다 박았으면
            score[i] += D  # D만큼의 점수를 얻게 됩니다.
            survived[i] = m  # 산타는 기절합니다.
            nnSr, nnSc = nSr - D * dr[Sdir], nSc - D * dc[Sdir]  # 반대 방향으로 D 칸 만큼 밀려나게 됩니다.
            interaction(i, nnSr, nnSc, (Sdir + 2) % 4)

        else:
            arr[nSr][nSc] = i  # 맵에 갱신해주고
            santas[i] = [nSr, nSc]  # 산타 위치도 바꿔주고


def interaction(num, r, c, direction):
    nr, nc = r, c
    while True:
        if oob(nr, nc):
            survived[num] = -1
            return

        santas[num] = [nr, nc]

        if arr[nr][nc] == 0:  # 만약 비어있다면
            arr[nr][nc] = num  # 날라간 산타 그 위치로 이동
            return

        num, arr[nr][nc] = arr[nr][nc], num

        nr, nc = nr + dr[direction], nc + dc[direction]


N, M, P, C, D = map(int, input().split())
arr = [[0] * N for _ in range(N)]
santas = [[0, 0] for _ in range(P + 1)]
survived = [-5] * (P + 1)
score = [0] * (P + 1)
Rr, Rc = map(lambda x: int(x) - 1, input().split())
INF = float('inf')

for p in range(P):
    num, r, c = map(int, input().split())
    r -= 1
    c -= 1
    santas[num] = [r, c]
    arr[r][c] = num

for m in range(M):
    # -------------------------- 1. 루돌프 움직이기 -------------------------------
    # print('이동 전')
    # for r in range(N):
    #     print(arr[r])
    # print()
    Rr, Rc = Rmove()
    # print('루돌프 위치', Rr, Rc)
    Smove()
    # print('산타 위치', santas)
    # print(m,'번 째 라운드')
    # for r in range(N):
    #     print(arr[r])
    # print()
    for i in range(1, P + 1):
        if survived[i] != -1:
            score[i] += 1
    # print('점수', score)
print(*score[1:])