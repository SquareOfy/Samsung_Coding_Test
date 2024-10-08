"""
1차
풀이 시간 : 53분
시도 횟수 : 1회
실행 시간 : 184 ms
메모리 : 113272 kb

2차
풀이 시간 : 59분
시도 횟수 : 1회
실행 시간 : 188 ms
메모리 : 113552 kb


실수 모음
    - 룩업테이블 실수
    - 달팽이 버벅임

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: 룩업 + 달팽이 ㅇㅋㅇㅋ
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : 간단해서 바로함 하지만 버벅임
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 할필요 ㄴㄴ
"""
"""
======================= 2차 코드 리뷰 =========================
1554 문제읽고 주석 정리
1603 설계
    - 내 헤맴의 시초.. 전에 쉽게 푼 문제인게 기억나서 대충 설계했다가
        구현 버벅임
1629 구현 + 디버깅 같이한 느낌 .. 
    일단 달팽이 템플릿 기억 속에서 희미해짐+ 하던대로 말고 다르게 해보려다가 뚝딱댐
    룩업테이블을 처음 풀었을 때와 달리 엄청 많이 틀림 ^^ .. 아익후 

피드백
- 달팽이 너무 오랜만에 풀었따 다시 복습하자 $!@#!@ㅆ$@#
"""


"""
바닥 먼지의 양을 담은 n * n 행렬
n은 항상 홀수
 처음에 정가운데 격자에는 먼지가 존재하지 않습니다. 
 정가운데부터 시작하여 아래 그림과 같이 나선형으로 왼쪽 - 아래쪽 - 오른쪽 - 위쪽 순서로 이동하며 청소

빗자루가 이동한 위치의 격자(Curr)에 있는 먼지가 함께 이동하는데 아래의 비율에 맞춰서 먼지가 이동하게 됩니다. 
이동한 먼지는 기존의 먼지 양에 더해지고, 빗자루가 이동한 위치(Curr)에 있는 먼지는 모두 없어지게 됩니다.
a%에 해당하는 먼지 양은 다른 격자에 이동한 먼지의 양을 모두 합한 것을 이동한 위치에 있던 먼지의 양에서 빼고 남은 먼지
비율을 곱해줄 때 소숫점 아래의 숫자는 버림
"""

"""
lst = [(-1, -1), (-1, 0), (-2, 0), (-1, 1), (1, 1), (1, 0), (2, 0),  (1, -1), (-2, 0)]

percent_lst = [10, 7, 2, 1, 1, 7, 2, 10, 5]

"""


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


point_lst = [
    [(-1, -1), (-1, 0), (-2, 0), (-1, 1), (1, 1), (1, 0), (2, 0), (1, -1), (0, -2)],
    [(1, -1), (0, -1), (0, -2), (-1, -1), (-1, 1), (0, 1), (0, 2), (1, 1), (2, 0)],
    [(1, 1), (1, 0), (2, 0), (1, -1), (-1, -1), (-1, 0), (-2, 0), (-1, 1), (0, 2)],
    [(-1, 1), (0, 1), (0, 2), (1, 1), (1, -1), (0, -1), (0, -2), (-1, -1), (-2, 0)]
]
percent_lst = [10, 7, 2, 1, 1, 7, 2, 10, 5]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
DIR = (0, -1), (1, 0), (0, 1), (-1, 0)
r, c = N // 2, N // 2
d = 0
answer = 0
test = []
l = 1
cnt = 0
while 1:
    for d in range(4):
        di, dj = DIR[d]
        for t in range(l):
            r += di
            c += dj
            tmp = arr[r][c]
            lst = point_lst[d]
            for k in range(9):
                ddi, ddj = lst[k]
                fly = tmp * percent_lst[k] // 100
                arr[r][c] -= fly
                du, dv = r + ddi, c + ddj

                if oob(du, dv):
                    answer += fly
                    continue
                arr[du][dv] += fly

            # a%
            ni, nj = r + di, c + dj
            if oob(ni, nj):
                answer += arr[r][c]
            else:
                arr[ni][nj] += arr[r][c]
            arr[r][c] = 0
            if r == 0 and c == 0:
                break
        cnt += 1
        if cnt == 2:
            l += 1
            cnt = 0
        if r == 0 and c == 0:
            break
    if r == 0 and c == 0:
        break
print(answer)

"""
총 풀이시간 : 53분
1400 문제 읽기 시작(21분)
        - 처음에 문제 보고 잘 이해가 안가서 당황함
        - 차분하게 한줄한줄 메모하고 읽음
        - 토네이도 회전할 때 모래 퍼지는 방향에 대한 구현 고민됨 ,,
        - 매번 방향을 좌표 바꾸기, - 바꾸기 하다가 실수가 잦을 거라 생각해서 룩업테이블 만들 생각함
1421 룩업테이블 구현 시작
        - 타이핑 하다가 실수하기 쉬운 케이스라 코드로 구현하기로 함
        - 실수를 가장 안할 수 있는 문제 속 그림을 타이핑으로 작성하고
        - 해당 dictionary를 회전하여 배열에 4방향에 대한 ditionary 저장
1429 대략적인 구현 주석 정리 및 구현 시작
        - 토네이도 구현 시, while 문 내에 for문 4개 쓰려다가
        - 코드 반복 시, 코드가 한 눈에 안들어와 자주 오타내고 실수하던 과거의 내가 생각나
        - 한번에 깔끔하게 짜보려고 노력함
        - 0,0 일 때 종료시키는 부분에서 약간 버벅임 => 인덱스 에러 많이 만남
            원인 : dir 배열에서 오타 발견
            조건을 while문이 시작되는 위치에 두는걸로 변경

1455 구현 완료했으나 일부 테케 안맞음
    - 수의 범위가 커질 수록 크게 안맞았음
    - 전반적인 로직 점검했으나 문제에서 시킨대로 잘 수행한듯 해 룩업테이블 의심하며 print 디버깅
    - 위쪽 2%가 누락된 것 발견하고 수정해서 해결


* 잘한 점
    - 평소 잘 사용하지 않던 dictionary를 활용해 봄 => 코드 리뷰의 효과 ..?
    - 룩업테이블을 적재적소에 잘 활용한 느낌
    - 문제 이해 어려웠으나 차분하게 한줄한줄 음미하며 읽은 것..
* 못한 점
    - 오 !! 타 !!!!!!!!!!!!!!!1

"""

# 0, 1, 2, 3일 때 dic 넣어서
# 각 좌표에서 몇 %인지 나오게 하기


# 좌 하 우 상 순
d_dict = [{(-2, 0): 0.02, (-1, -1): 0.1, (-1, 0): 0.07, (-1, 1): 0.01, (0, -2): 0.05, (1, -1): 0.1, (1, 0): 0.07, (1, 1): 0.01, (2, 0): 0.02},\
          {(0, -2): 0.02, (1, -1): 0.1, (0, -1): 0.07, (-1, -1): 0.01, (2, 0): 0.05, (1, 1): 0.1, (0, 1): 0.07, (-1, 1): 0.01, (0, 2): 0.02}, \
          {(2, 0): 0.02, (1, 1): 0.1, (1, 0): 0.07, (1, -1): 0.01, (0, 2): 0.05, (-1, 1): 0.1, (-1, 0): 0.07, (-1, -1): 0.01, (-2, 0): 0.02},\
          {(0, 2): 0.02, (-1, 1): 0.1, (0, 1): 0.07, (1, 1): 0.01, (-2, 0): 0.05, (-1, -1): 0.1, (0, -1): 0.07, (1, -1): 0.01, (0, -2): 0.02}]

dir = (0, -1), (1, 0), (0, 1), (-1, 0)
answer = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 토네이도 이동 구현하기
sr, sc = n // 2, n//2
l = 1
cnt = 0
d_idx = 0
while 1:
    if sr == 0 and sc == 0:
        break
    # 현재 방향으로 l만큼 토네이도 및 모래 이동하고
    # l만큼을 두번 갔다면! l+1시키기
    # 방향도 매번 회전하기
    di, dj = dir[d_idx]
    for i in range(l):
        # 토네이도 이동
        sr += di
        sc += dj
        sand = arr[sr][sc]
        # sr, sc에 있는 모래를 여기를 기준으로 이동
        for k, v in d_dict[d_idx].items():
            du = sr + k[0]
            dv = sc + k[1]
            spread_sand = int(sand * v)
            arr[sr][sc] -= spread_sand
            if du < 0 or dv < 0 or du >= n or dv >= n:
                answer += spread_sand
                continue
            arr[sr + k[0]][sc + k[1]] += spread_sand
        # 모래 다 옮기고 나서 alpha 칸으로 남은 모래 전부 옮기기
        du = sr + dir[d_idx][0]
        dv = sc + dir[d_idx][1]
        if du < 0 or dv < 0 or du >= n or dv >= n:
            answer += arr[sr][sc]
        else:
            arr[du][dv] += arr[sr][sc]
        arr[sr][sc] = 0

        if sr == 0 and sc == 0:
            break
    cnt += 1
    if cnt == 2:
        l += 1
        cnt = 0
    d_idx = (d_idx + 1) % 4
print(answer)

# 토네이도 이동 속의 모래 이동
# 현재 보는 방향의 y좌표를 중심으로 d_dict에서 꺼내서 계산하기
# 바운더리 벗어나면 answer에다 더하기


# 룩업테이블 만드는 코드
# first = {(-2,0):0.02, (-1, -1):0.1, (-1, 0): 0.07, (-1, 1): 0.01, \
#          (0, -2):0.05, (1, -1) : 0.1, (1, 0):0.07, (1, 1) : 0.01, (2,0):0.02}
# d_dict = [first]
# def rotate(point):
#     return -point[1], point[0]
# for i in range(3):
#     new_dict = {}
#     for k, v in d_dict[-1].items():
#         new_dict[rotate(k)] = v
#
#     d_dict.append(new_dict)
# print(d_dict)
