"""
1차
풀이 시간 : 30분
시도 횟수 : 2회
실행 시간 : 476ms
메모리 : 117604kb

2차
풀이 시간 : 30분
시도 횟수 : 3회
실행 시간 :796ms
메모리 : 214756kb

실수 모음
- 오타 
- 시간복잡도 계산 미흡


Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 
    : 죽은 애들은 나중에 바이러스 나이 다 먹이고 한꺼번에 처리하기 주의할 것
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 
"""

"""
======================= 2차 코드 리뷰 ==================
0833 문제 읽기 시작 + 주석정리
0839 구상 시작
    그냥 순차적으로 하라는거 구현하면 되겠군 생각함
    바이러스 담을 배열 3차원으로 관리해야지+ sort 써야지 생각
    
0845 구현 시작 
0857 구현완료 후 테스트케이스랑 프린트해서 비교 확인
0858 제출했으나 에러. (인덱스 에러) 
    => 해당 부분 가보니 arr선언할 때 행 값 5로 잘못 설정(오타)
0859 또 틀렸으나 수업 시작해서 일단 킵
1355 다시 찾기. 틀린 테케 단계별 프린팅해서 이상한 부분 없는지 점검
        나이가 아니라 그 땅의 값을 2로 나눠서 죽은 뒤 양분으로 더해주는 문제 발견 
        해결
        
총평
- 실수 ... 오타 .. 흑
- 전보다 못한 시간효율의 코드 
- 너무 한번 죽은 애가 등장하면 무조건 그 뒤가 다 죽는 것 생각 왜못했지 
- lst에 죽은 애들 따로 담지 말고 바로 양분에 더해줬어도 괜찮았는데 !! 동시라는 조건에 너무 푹 빠졌던듯




"""

"""
n * n 격자 무늬의 배지에 바이러스를 배양

초기에 각 칸에 5만큼의 양분  m개의 바이러스
입력으로 주어지는 바이러스의 위치는 모두 서로 다르다고 가정


k 사이클 이후에 살아남은 바이러스의 수

1.
각각의 바이러스는 본인이 속한 1 * 1 크기의 칸에 있는 양분을 섭취
본인의 나이만큼 양분을 섭취
같은 칸에 여러 개의 바이러스가 있을 때에는 나이가 어린 바이러스부터 양분을 섭취
양분을 섭취한 바이러스는 나이가 1 증가
양분이 부족하여 본인의 나이만큼 양분을 섭취할 수 없다면 그 즉시 죽습니다.

2. 모든 바이러스가 섭취를 끝낸 후 죽은 바이러스가 양분으로 변합니다.
죽은 바이러스마다 나이를 2로 나눈 값이 바이러스가 있던 칸에 양분으로 추가

3.  바이러스가 번식을 진행
번식은 5의 배수의 나이를 가진 바이러스에게만 진행
인접한  상하좌우와 대각선 8개의 칸에 나이가 1인 바이러스가 생깁니다.
배지 범위를 벗어난 곳에는 바이러스가 번식하지 않습니다.
주어진 양분의 양에 따라 칸에 양분이 추가됩니다.
"""


#입력받기
N, M, K = map(int, input().split())
plus = [list(map(int, input().split())) for _ in range(N)]
virus_arr = [[[] for _ in range(N)] for _ in range(N)]
arr = [[5]*N for _ in range(N)]
DIR = (-1, -1), (-1, 1), (1, -1), (1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)
for m in range(M):
    r, c, a = map(int, input().split())
    r-=1
    c-=1
    virus_arr[r][c].append(a)

for k in range(K):
    #양분 먹거나 죽거나
    die_lst = []
    for i in range(N):
        for j in range(N):
            if not virus_arr[i][j]: continue
            tmp = []
            for a in virus_arr[i][j]:
                if arr[i][j]-a <0:
                    die_lst.append((i, j, a//2))
                else:
                    arr[i][j] -= a
                    tmp.append(a+1)
            virus_arr[i][j] = tmp[:]

    #양분 뿌리기
    for i, j, v in die_lst:
        arr[i][j] += v
    # print("====================바이러스 나이먹고 양분 plus ==================")
    # print("죽은 바이러스 " , die_lst)

    # for i in range(N):
    #     print(arr[i])
    #
    # print(" == ")
    #
    # for i in range(N):
    #     print(virus_arr[i])
    #
    # print()
    # print("=======================")

    #바이러스 번식과 양분추가
    for i in range(N):
        for j in range(N):
            for a in virus_arr[i][j]:
                if a%5 == 0:
                    for di, dj in DIR:
                        du, dv = i+di, j+dj
                        if du<0 or dv<0 or du>=N or dv>=N:
                            continue
                        virus_arr[du][dv].append(1)
            arr[i][j] += plus[i][j]


    #바이러스 나이순 정렬
    for i in range(N):
        for j in range(N):
            if not virus_arr[i][j]: continue
            virus_arr[i][j].sort()

    # print("====================바이러스 번식. 양분추가. 정렬 ==================")
    # for i in range(N):
    #     print(arr[i])
    #
    # print(" == ")
    #
    # for i in range(N):
    #     print(virus_arr[i])
    #
    # print()
    # print("=======================")

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(virus_arr[i][j])
print(answer)

"""
1641 문제 이해완 구상완 / 구현시작
1700 구현완 제출 시간초과 heapq가 오히려 비효율적임을 인지하여 lst로 변환
1711 디버깅완료 제출 정답


피드백
- 잘한점
    heapq로 시간초과 바로 뜨긴 했지만, 그 직후 lst가 더 효율적일 거라고 바로 판단하긴 했다 !

- 개선할 점
    시간복잡도 계산 잘 안하던게 여기서 드러난다 ...
    제출 직전 시간초과 될 수도 있겠다고 살짝 느꼈었으나 한 번 더 체크하지 않고 일단 내 본 안일함;
"""
import heapq
N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for t in range(N)]
die_lst = [[[] for _ in range(N)] for t in range(N)]
ground = [[5]*N for _ in range(N)]
tmp = [[[] for _ in range(N)] for t in range(N)]
dir = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
for i in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)
    # heapq.heappush(trees[x-1][y-1], z)


year = 0
while year < K:
    year += 1
    #봄 : 나이만큼 양분 먹기
    for i in range(N):
        for j in range(N):
            trees[i][j].sort()
            l = len(trees[i][j])
            for k in range(l):
                if ground[i][j] >= trees[i][j][k]:
                    ground[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for t in range(k, l):
                        ground[i][j] += trees[i][j][t]//2
                    trees[i][j][k:] = []
                    break


    # #나이 먹이기
    # for i in range(N):
    #     for j in range(N):
    #         for t in range(len(tmp[i][j])):
    #             heapq.heappush(trees[i][j], tmp[i][j].pop())

    #
    # #여름
    # for i in range(N):
    #     for j in range(N):
    #         for t in range(len(die_lst[i][j])):
    #             ground[i][j]+= die_lst[i][j].pop()//2

    #가을

    for i in range(N):
        for j in range(N):

            for t in trees[i][j]:
                if t%5 == 0:
                    for di, dj in dir:
                        du = i+di
                        dv = j+dj
                        if du<0 or dv<0 or du>=N or dv>=N:
                            continue
                        trees[du][dv].append(1)


    #겨울
    for i in range(N):
        for j in range(N):
            ground[i][j] += a[i][j]

ans = 0
for i in range(N):
    for j in range(N):
       ans+= len(trees[i][j])
print(ans)