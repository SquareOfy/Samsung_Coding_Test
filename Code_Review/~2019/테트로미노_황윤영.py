"""
- 1차 : 약 1시간

- 2차
풀이 시간 :26분
실행 시간 : 374ms
메모리 : 28 mb

- 실수 모음
    - N,M 실수
    - 시간초과 : visited 선언 방식
    - dfs 종료조건에 return 누락
    - 코드 복사 후 수정 덜함 ,,
    - dfs 초기 level 설정
"""

"""
============================ 2차 코드 리뷰 ================================
1332 문제 읽기 시작 / 문제주석 / 설계
    강렬하게 괴로워했던 기억 떠오르며 문제 쏙쏙 읽힘
    설계 DFS, ㅏㅓㅗㅜ 모양 조건 분기로 함
1347 구현할 영역 주석 정리 후 구현시작
1356 구현완료 디버깅 시작 
    조건분기 복사 후 오타 
    dfs 초기에 들어가는 level 값
1358 정답
    

"""
"""
Routine
1. 문제 그냥 정독 OK
2. 문제 주석 복사 OK
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 :
5. 종이에 손설계
6. 주석으로 구현할 영역 정리
7. 구현
8.테스트케이스 단계별 디버깅 확인
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!


Debugging CheckPoint
- N, M / 행 열 index 오타 실수 점검
- max, min 구할 때 초기값 체크
- 배열 사용 목적 확인 후 배열 변수 실수 확인
- 조건분기문 복사한 경우 모두 바꿨는지 체크
- 디버깅해서 바꾼 코드 부분 혹은 로직이 있다면 그 부분 중심으로 전반적으로 재점검
- 문제 조건 + 코드 로직 같이 따라가며 이상한 로직 없는지 점검
- 로직이 맞는데 답이 이상하다면 아주 사소한 순서 문제는 없을지 점검

Reset Timing
- 1시간 ~ 1시간 반 : 코드 다 짰는데 테케 정답이 엉망진창?
    문제 이해 미흡, 설계 미흡일 확률 높으므로 문제 다시 읽고 리셋할 모듈 찾을지 전체 리셋할지 판단하기
- 1시간 반 쯤에 코드 대부분이 잘 돌아가는데 특정 포인트에서 안되는 것 같다?
    - 특수한 테케가 있는지 1차로 점검해보고 디버깅
    - 오타 찾아야할 것 같다 => 그냥 리셋해버리자


"""

"""
n×m크기의 이차원 영역의 각 위치에 자연수 하나가 적혀있습니다.

다섯가지 종류의 테트리스 블럭 중 한 개를 적당히 올려놓아
 블럭이 놓인 칸 안에 적힌 숫자의 합이 최대가 될 때의 결과를 출력
 주어진 테트리스 블럭은 자유롭게 회전하거나 뒤집을 수 있습니다.

 BFS로 4가지 모양 탐색. ㅏ ㅓ ㅗ ㅜ 는 조건분기문으로 해결


"""


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= M


# 함수 dfs
def dfs(level, r, c, s):
    global answer
    if s + (4 - level) * mx_arr <= answer:
        return

    if level == 4:
        answer = max(s, answer)
        return

    for di, dj in (-1, 0), (0, 1), (1, 0):
        du = r + di
        dv = c + dj
        if oob(du, dv) or visited[du][dv]:
            continue
        visited[du][dv] = 1
        dfs(level + 1, du, dv, s + arr[du][dv])
        visited[du][dv] = 0


# 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
mx_arr = 0
visited = [[0] * M for _ in range(N)]
# arr의 mx 계산
for i in range(N):
    for j in range(M):
        mx_arr = max(arr[i][j], mx_arr)

# dfs 실행
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1, i, j, arr[i][j])
        visited[i][j] = 0
# ㅏ ㅓ ㅗ ㅜ 조건분기 체크
for i in range(N):
    for j in range(M):
        s = arr[i][j]
        # ㅏ
        if not (oob(i - 1, j) or oob(i, j + 1) or oob(i + 1, j)):
            answer = max(answer, s + arr[i - 1][j] + arr[i][j + 1] + arr[i + 1][j])
        # ㅗ
        if not (oob(i - 1, j) or oob(i, j - 1) or oob(i, j + 1)):
            answer = max(answer, s + arr[i - 1][j] + arr[i][j - 1] + arr[i][j + 1])
        # ㅓ
        if not (oob(i - 1, j) or oob(i, j - 1) or oob(i + 1, j)):
            answer = max(answer, s + arr[i - 1][j] + arr[i][j - 1] + arr[i + 1][j])
        # ㅜ
        if not (oob(i + 1, j) or oob(i, j + 1) or oob(i, j - 1)):
            answer = max(answer, s + arr[i + 1][j] + arr[i][j + 1] + arr[i][j - 1])

print(answer)

"""
=============================1차 코드 리뷰 ===============================
풀이시간 : 약 1시간'

1502 문제 이해 및 간략 구상 완
1515 구현완
1520 디버깅 완 (bfs continue조건 rank값 실수)
1521 n,m범위실수..
1525 visited 처리 방식을 최댓값 기록으로 바꿔서 최단거리 방문 순서에 따라 고르지 못하는 경우 고려하도록 수정
1534 bfs로 풀던 풀이에서 visited방식을 방문처리로도, 최댓값 처리로도 어려움을 겪어 dfs로 재구현 후 제출
1537 dfs 종료 조건에 return 빼먹는 바보 나야나 ~
1544 백준은 시초가 난다 .. bfs rank로 visited기록하면 되겠다ㄱ는 아이디어 생각남@

이후 숱한 시간초과 제출

==================문제점=================
1. 꼼꼼하게 테케를 점검하지 못함 (아래 같은 경우, visited 그냥 1로 처리하면 최댓값 잘못 구하는 케이스 등)
    1 1 1 1
    2 2 1 1
    1 2 2 1
    1 1 1 1
2. 시간초과의 원인을 대략적인 시간복잡도를 계산했는데도 내 계산보다 높은 수치가 나온다면
    내 코드를 line by line으로 점검하며, 시간이 오버될 원인을 찾기
3. 고집부리지 않기
    내 로직이 맞을 순 있으나, 현재 방법으로 오류를 찾기 어렵다면 갈아엎을 줄도 알아야 함
==================구상=================
문제는 ㅏ ㅓ ㅗ ㅜ  모양
이 모양 제외 bfs or dfs 로 최댓값 찾기
bfs로 했을 때 겹치는 모양이 없을지 고려해볼것. 있겠군. 하지만 합이 최대인 경우니까 괜찮을듯

ㅏ ㅓ ㅗ ㅜ 는 분기문으로 해결하자


"""
import sys
def dfs(level, sm, r, c):
    global answer

    if level == 4:
        answer = max(answer, sm)
        return
    for di, dj in (-1, 0), (0, -1), (1, 0), (0, 1):
        du = r + di
        dv = c + dj
        if du < 0 or dv < 0 or du >= n or dv >= m:
            continue
        if not visited[du][dv] or visited[du][dv] >= level+1:
            visited[du][dv] = level+1
            dfs(level + 1, sm + arr[du][dv], du, dv)
            visited[du][dv] = 0


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]
answer = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(1, arr[i][j], i, j)
        visited[i][j] = 0
        # ㅏ ㅓ ㅗ ㅜ 체크
        # 가운데 갈림길인 부분을 기점으로 보겟음
        s = arr[i][j]
        # ㅏ / ㅓ
        if i + 1 < n and i - 1 >= 0 and j - 1 >= 0:  # ㅓ
            answer = max(answer, s + arr[i + 1][j] + arr[i - 1][j] + arr[i][j - 1])
        if i + 1 < n and i - 1 >= 0 and j + 1 < m:  # ㅏ
            answer = max(answer, s + arr[i + 1][j] + arr[i - 1][j] + arr[i][j + 1])
        if j + 1 < m and j - 1 >= 0 and i - 1 >= 0:  # ㅗ
            answer = max(answer, s + arr[i][j + 1] + arr[i][j - 1] + arr[i - 1][j])
        if j + 1 < m and j - 1 >= 0 and i + 1 < n:  # ㅗ
            answer = max(answer, s + arr[i][j + 1] + arr[i][j - 1] + arr[i + 1][j])




print(answer)
