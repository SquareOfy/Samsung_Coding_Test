"""
1차
풀이 시간 : 38분
시도횟수 : 1회

2차
풀이 시간 : 40분
시도 횟수 : 1회

실수 모음

1. 문제 잘못 파악
변수 내 입력값 잘못 파악
로봇 청소기 첫 위치 조건 잘못 파악

2.로직 누락
rotate_cnt 후진할 때 reset 누락

"""

"""
======================== 2차 코드 리뷰 ========================
1450 문제 읽기 시작, 주석에 조건 정리, 주의할 사항 체크
1455 손설계 + 주석으로 설계할 영역 준비
1502 구현시작 
1507 구현완료 후 디버깅 시작.
    - 무한루프 돌길래 print 찍었음. 너무 많이 찍히길래 break_cnt 값 넣고 break 걸었음
        4번 다 회전했고, 후진 못할 때 break 시키는 if문 안으로 안들어오는 문제 확인
    - rotate_cnt, 이동할 후보 함께 출력하며 문제 파악하려함 
        이 때 문제 해결하고 break_cnt 때문에 answer 더 안가고 중간에 끊겼는데 
        생각 못하고 조금 헤맸다 .
        rotate_cnt를 후진할 때 reset 안해주는 문제 발견 
    - 해결 

1529 정답

총평 
    슈더코드 미흡하게 작성했더니 바로 구현할 때 로직 오류 생겼음; 
    디버깅하는 속도가 조금 느리다 .. 



"""
"""
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : oob 불필요. 방향 좌회전 우선!! 종료조건 주의
5. 종이에 손설계
6. 주석으로 구현할 영역 정리 :
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 :
9. 예외될 상황 테스트케이스 만들어서 확인 :
10. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!


Debugging CheckPoint
- N, M / 행 열 index 오타 실수 점검
- max, min 구할 때 초기값 체크
- 인덱스 디테일 확인( dfs 종료 level이나 범위 경계값)
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
n * m 크기의 도로에 1 * 1 크기의 자율주행 자동차


절차 
1. 현재 방향을 기준으로 왼쪽 방향으로 한 번도 간 적이 없다면 좌회전해서 해당 방향으로 1 칸 전진합니다.
2. 만약 왼쪽 방향이 인도거나 이미 방문한 도로인 경우 좌회전하고 다시 1번 과정을 시도합니다.
3. 2번에 대해 4방향 모두 확인하였으나 전진하지 못한 경우에는
 바라보는 방향을 유지한 채로 한 칸 후진을 하고 다시 1번 과정을 시도합니다.

4. 3번 과정을 시도하려 했지만 뒷 공간이 인도여서 후진조차 하지 못한다면 작동을 멈춥니다.

 d(바라보는 방향)는 0부터 3까지 숫자로 주어지고 북동남서
 인덱스 0부터 시작 

 0 도로
 1 인도 
 자율주행 자동차가 있는 칸은 도로일 것이라 가정해도 좋습니다.
격자의 첫번째 행과 마지막 행, 첫번째 열과 마지막 열은 항상 인도일 것이라고 가정해도 좋습니다.

oob 체크 불필요!!!!!!!!!!!!!!11 

"""

# 입력받기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# DIR, answer, visited, rotate_cnt 준비
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
answer = 1
rotate_cnt = 0
visited = [[0] * M for _ in range(N)]
break_cnt = 0

visited[r][c] = 1
# while
while 1:

    # 방향 회전 (rotate_cnt 증가)
    d = (d - 1) % 4
    rotate_cnt += 1

    # 앞칸 이동 가능 확인 => 이동하면 answer+, rotate_cnt = 0
    di, dj = DIR[d]
    nr, nc = r + di, c + dj
    if arr[nr][nc] == 0 and not visited[nr][nc]:
        visited[nr][nc] = 1
        r, c = nr, nc
        rotate_cnt = 0
        answer += 1

    # 4번 회전했으면 후진 시도하고 인도면 break. 아니면 후진
    if rotate_cnt == 4:
        nr, nc = r - di, c - dj
        if arr[nr][nc] == 1:
            break
        r, c = nr, nc
        rotate_cnt = 0

print(answer)



"""
======================== 1차 코드 리뷰 ========================
로봇청소기 코드 리뷰
총 풀이시간 : 38분 
문제읽기 3시 16분 ~ 20분
구상 20분 ~23분
구현시작 23분 ~32분 구현 완료
        엉망진창 테케 결과로 디버깅 시작
33분 ~

1516 문제읽기
1520 구상시작
1523 구현완료했으나 테케 결과 안맞음. 디버깅 시작
1549 arr값 제대로 이해 못했음을 발견 ( 문제 잘 읽어야함...)
1554 로봇청소기의 초기 위치가 항상 청소된 상태임을 착각. 테케에 의존하지 말것. 구현완료. 제출


======================== 구상 ========================
인덱스 0부터 시작
모두 청소 안된상태 ( visited 0으로 )
현재 칸 청소
현재 칸에서 사방 탐색해서 청소되지 않은 빈칸 여부 체크하기
빈칸 없다?
    바라보는 방향(d) 유지한체 후진하고 다시 사방탐색 반복
    벽이면 작동 멈추기(break)

빈칸 있다 ? 반시계 회전 (direction : 상 좌 하 우 로 만들고 +1 module)
앞에 빈칸이면 전진 아니면 회전
"""
def need_clean():
    for di, dj in directions:
        du = r+di
        dv = c+dj
        if obb(du, dv):
            return False
        if arr[du][dv] == 0:
            return True
    return False
def obb(du, dv):
    if du < 0 or dv < 0 or du >= n or dv >= m:
        return True
    return False
#input 받기
n, m = map(int, input().split())
r, c, d = map(int, input().split())

#d : 0 - 북(상)/ 1 - 동(우) /2- 남(하)  / 3(좌)
#arr배열 입력받기 => visited로 함께 활용할 것
arr = [list(map(int, input().split())) for _ in range(n)]
directions = (-1, 0), (0, 1),  (1, 0),(0, -1)  #direction 상우하좌로 준비 반시계 회전하려면 +3 mod
answer = 0
while 1:
    if arr[r][c] == 0:   #현재칸 청소

        arr[r][c] = 2
        answer+=1

    #사방탐색 청소된칸 여부 확인 (함수화)
    result = need_clean()
    #없으면 후진 후 continue
    if not result:
        du = r- directions[d][0]
        dv = c- directions[d][1]
        if obb(du, dv) or arr[du][dv]==1:
            break
        r = du
        c = dv
        continue

    #있으면 반시계회전 for문.
    #청소안된 곳이면 전진 후 break
    for i in range(4):
        d = (d + 3) % 4
        du = r+ directions[d][0]
        dv = c+ directions[d][1]
        if obb(du, dv) or arr[du][dv] == 1:
            continue
        #전진 후 청소
        if arr[du][dv] == 0:
            r = du
            c = dv
            break


print(answer)