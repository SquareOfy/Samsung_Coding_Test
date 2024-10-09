"""
1차
풀이 시간 : 28분
시도 횟수 : 1회
실행 시간 : 292 ms
메모리 : 111828kb

2차
풀이 시간 : 32분
시도 횟수 : 1회
실행 시간 : 300ms
메모리 : 111988kb

실수 모음
- nr, nc 갱신 누락 ;;

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 미세먼지 한번에 확산 처리 / 돌풍 oob뿐 아니라 down/ up 영역 침범일 때 break하기
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok !
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!

"""
"""
======================= 2차 코드 리뷰 ==============================

1510 문제 읽기 시작 + 주석정리
    돌풍이 이번에도 머리에 후딱 그려지진 않았따 항상 한번더 생각하는 부분인듯,, 

1516 설계 시작
    절차가 명확해서 먼지 확산 / 돌풍 두가지로 나눠서 설계
    첫 풀이때 down, up 영역일 때 방향 회전하게 안해서 디버깅했던 기억이 떠올라 신경써서 구현
    
1527 구현 영역 정리 및 구현
    먼지 확산 다 구현하고 중간 테스트 함
    
1537 구현완료 디버깅 시작
    무한루프를 돈다? 
    print했는데 0,0 반복
    cnt 값 올리고 break 걸어서 프린트 디버깅 했음 
    nr, nc 갱신 안되는 것 깨닫고 수정해서 정답
    

"""
"""
n * m 크기의 격자칸
돌풍은 항상 1번 열에 설치  크기는 두 칸을 차지

1초 동안 방에는 다음과 같은 일이 일어납니다.

1. 먼지가 인접한 4방향의 상하좌우 칸으로 확산됩니다.
    인접한 방향에 시공의 돌풍이 있거나, 
    방의 범위를 벗어난다면 해당 방향으로는 확산이 일어나지 않습니다.
    확산되는 양은 원래 칸의 먼지의 양에 5를 나눈 값이며, 편의상 소숫점은 버립니다.
    각 칸에 확산될 때마다 원래 칸의 먼지의 양은 확산된 먼지만큼 줄어듭니다.
    . 확산된 먼지는 방에 있는 모든 먼지가 확산을 끝낸 다음에 해당 칸에 더해지게 됩니다.

2. 시공의 돌풍이 청소를 시작합니다.
    시공의 돌풍의 윗칸에서는 반시계 방향으로 바람
    아랫칸에서는 시계 방향으로 바람
    바람이 불면 먼지가 바람의 방향대로 모두 한 칸씩 이동합니다.
    시공의 돌풍으로 들어간 먼지는 사라집니다

시공의 돌풍이 설치되어 있는 칸은 -1로 표시
 항상 맨 왼쪽에 위치하며, 두 칸을 차지

 출력 : t초가 지난 이후 방에 남아있는 먼지의 양

"""


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= M


def find_tornado():
    # 돌풍위치 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                return i, i + 1


# 입력
N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
up, down = find_tornado()

for t in range(T):
    tmp = [[0] * M for _ in range(N)]
    # 먼지 확산
    for i in range(N):
        for j in range(M):
            if arr[i][j] == -1:
                tmp[i][j] = -1
                continue
            v = arr[i][j] // 5
            cnt = 0
            for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                du, dv = i + di, j + dj
                if oob(du, dv) or arr[du][dv] == -1:
                    continue
                tmp[du][dv] += v
                cnt += 1
            tmp[i][j] += arr[i][j] - cnt * v

    # 임시배열 반영
    for i in range(N):
        arr[i] = tmp[i][:]

    # 돌풍

    cr, cc = up - 1, 0
    k = 0
    # 윗쪽
    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
        while 1:
            nr, nc = cr + di, cc + dj
            if oob(nr, nc): break  # 범위 아웃
            if nr == down: break
            if nr == up and nc == 0: break
            arr[cr][cc] = arr[nr][nc]
            cr, cc = nr, nc
    arr[cr][cc] = 0

    # 아랫쪽
    cr, cc = down + 1, 0
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        while 1:
            nr, nc = cr + di, cc + dj
            if oob(nr, nc): break  # 범위 아웃
            if nr == up: break
            if nr == down and nc == 0: break
            arr[cr][cc] = arr[nr][nc]
            cr, cc = nr, nc
    arr[cr][cc] = 0

# 출력
answer = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != -1:
            answer += arr[i][j]
    # print(arr[i])
print(answer)
"""

1614 문제 이해 완 / 구상시작
1618 코드 쓰기 시작 (돌풍청소 구현미흡,, 돌풍청소 부분 코드 머릿 속에 바로 안그려짐 )
1642 구현 및 돌풍 방향 변경 부분 디버깅 후 제출
===============조건================

1초 동안 발생하는 일
    1. 먼지 확산
        상하좌우로 먼지 확산(배열 범위 내 / 돌풍 아닌 곳)
        확산양 원래칸 // 5만큼 확산 + 확산된만큼 그 칸 -
        동시에 발생하므로 확산 배열 따로 만들어두고 확산량 다 계산 후
        한번에 연산해서 원본 배열에 반영해야 함
        원본 배열에 반영할 때 sum 구해두기

    2. 돌풍 청소
        윗칸 반시계 이동
        아랫칸 시계 이동

        while문 4번쓰기? 배열 index?
        돌풍 윗칸부터 시작해서 윗칸 값을 자기 자리로 내리기 반복
        첫 시작 값을 전체 sum에서 빼기
        윗칸 없으면 방향 옆칸으로 바꾸기
        옆칸 없으면 아래칸으로 바꾸기
        아랫칸이 돌풍 아래칸의 행과 같으면 왼쪽으로 바꾸기
        (상, 우, 하, 좌) 순으로 옆에 있는 거 땡겨올 것
        최종으로 왼쪽이 돌풍이면 0으로 만들고 종료

        돌풍 아래칸 청소
        (하, 우, 상, 좌)
        최종으로 왼쪽이 돌풍이면 0 으로 만들고 종료
"""
def find_storm():
    for i in range(n):
        if arr[i][0]==-1:
            return i
n, m, t = map(int, input().split())
tc = 0
arr = [list(map(int, input().split())) for _ in range(n)]
up= find_storm()
down = up+1
tmp = [[0] * m for _ in range(n)]

while 1:
    if tc == t:
        break

    #먼지확산
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                continue
            out = arr[i][j]//5
            for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
                du = i + di
                dv = j + dj

                if du<0 or dv<0 or du>=n or dv>=m:
                    continue
                if arr[du][dv]==-1:
                    continue
                tmp[i][j]-=out
                tmp[du][dv]+= out
    #확산 합치기
    for i in range(n):
        for j in range(m):
            arr[i][j]+=tmp[i][j]
            tmp[i][j] = 0

    #돌풍 청소
    s = 0
    #윗칸 돌풍 위에 있는거 땡겨오기

    sr = up
    sc = 0
    for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
        while 1:
            if sr+di <0 or sr+di == down:
                break

            if sc+dj >=m or arr[sr+di][sc+dj] == -1:
                break
            if arr[sr][sc] != -1:
                arr[sr][sc] = arr[sr+di][sc+dj]
            sr += di
            sc += dj
            arr[sr][sc] = 0
    sr = down+1
    sc = 0
    s -= arr[sr][sc]  # 아랫칸 빨려들어감
    for di, dj in (1, 0), (0, 1), (-1, 0), (0, -1):
        while 1:
            if sr + di >= n or sr + di == up:
                break
            if sc + dj == m or arr[sr+di][sc+dj]==-1:
                break
            if arr[sr][sc] != -1:
                arr[sr][sc] = arr[sr + di][sc + dj]
            sr += di
            sc += dj
            arr[sr][sc] = 0

    tc += 1
#먼지 양 세기
answer = 0
for i in range(n):
    answer += sum(arr[i])
print(answer+2)