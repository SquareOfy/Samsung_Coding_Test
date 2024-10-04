"""
1차
풀이 시간 : 40분
시도 횟수 : 2회
실행 시간 : 316 ms
메모리 : 127036 KB

1차
풀이 시간 : 33분
시도 횟수 : 2회
실행 시간 : 304 ms
메모리 : 132256 KB

실수 모음
    - 인덱스 실수 (모듈)
    - 로직 누락

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : deque 쓰자
    : N칸 도착하자마자 내리는 거 놓치지 말기!!
5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인
    : 답 다르길래 deque 사람 움직이기 전 후로 프린트+종이테케 따라가기로
    틀린 부분 찾음
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!
"""
"""
==================== 2차 코드 리뷰 ====================
1646 문제읽기 
    문제 열심히 읽다가 주석 정리 까먹음 
1658 설계 및 구현 
1707 테케 안맞음 디버깅 
    왜 합쳐진후 분할된 원자가 아니라 엉망진창 뒤섞인 원자들이 있지 ? 
    원자 분할하는 로직 살핌. 합쳐져서 소멸돼야하는데 이 때 tmp 안비워준 실수 발견! 수정
1710 오답
    테케 찾아서 돌려봄 
    방향이 이상하게 잡히는 것 발견
    sum_d , multiple_d 구할 때 %2 해주는 것 누락함 
    고쳐서 실수; 

설계한대로 구현 빼먹지 말고 하자 ..


"""
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
DIR = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
for m in range(M):
    x, y, m, s, d = map(int, input().split())
    x -= 1
    y -= 1
    arr[x][y].append((m, s, d))
# print("=================초기 상태 ==================")
# for t in range(N):
#     print(arr[t])
# print("=============================================")
for k in range(K):
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue
            # print(arr[i][j])
            for t in range(len(arr[i][j])):
                m, s, d = arr[i][j][t]
                nr = (i + DIR[d][0] * s) % N
                nc = (j + DIR[d][1] * s) % N
                tmp[nr][nc].append((m, s, d))
    for i in range(N):
        for j in range(N):
            if len(tmp[i][j]) < 2: continue
            mm = 0
            ss = 0
            multiple_d = 1
            sum_d = 0
            for m, s, d in tmp[i][j]:
                mm += m
                ss += s
                multiple_d *= (d%2)
                sum_d += (d%2)

            new_m = mm//5
            new_s = ss//len(tmp[i][j])
            tmp[i][j] = []
            if new_m ==0:
                continue
            new_d = [0, 2, 4, 6] if sum_d==0 or multiple_d==1 else [1, 3, 5, 7]

            for k in range(4):
                tmp[i][j].append((new_m, new_s, new_d[k]))



    for i in range(N):
        for j in range(N):
            arr[i][j] = tmp[i][j][:]
    #     print(arr[i])
    # print("======================================")

answer = 0
for i in range(N):
    for j in range(N):
        for m, s, d in arr[i][j]:
            answer+= m

print(answer)

"""
코드리뷰
총 풀이 시간 40분
실행 시간 : 316 ms
메모리 : 127036 KB

1315 문제 읽기 시작 /구상
    - 1회독
    - 문제 절차 주석으로 복사해와서 이해 잘 되도록 정리
    - 구현 방법 주석으로 메모
    - 슈더코드 작성
1326 구현할 단계 주석 정리 후 구현시작
    중간에 주의할 내용 느낌표로 주석 표기

1340 구현완료 후 디버깅 시작
    테케 안맞아서 중간중간 프린트해서 각 단계 확인
    new_arr로 합쳐진 파이어볼 4개로 나누는 단계는 정상적으로 찍히는데 arr[i][j]에는 안들어가 있다는 문제 발견
    합치고 나누는 부분 구현한 코드 순서대로 살펴보기
    세부단계에서 arr에 잘 들어가는지 어디선가 없어진건 아닌지 보기 위해 디버거 사용
    파이어볼이 한개 뿐일 때 처리가 안된 것 확인 => 조건문 추가로 해결
    TypeError 발생. 바로 윗줄에 print 찍어보고 튜플이 아닌 -2가 나오길래 뭐지 했다가 오타 발견

1352 제출 했으나 런타임에러
    런타임 에러 보자마자 처음과 끝이 연결된 부분이 문제일거라고 생각
    문제 속 로직 말고 직접 배열에 음수 크게(-9) 넣어봐서 에러나는지 봄
    음수는 최대 한바퀴까지만 조회 가능하고 더 커지면 모듈 안된다는걸 알게됨!
    모듈 추가해서 해결
1356 정답

피드백 
    드디어 밀려있던 파이어볼 풀었다 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
    뒤에 토네이도 블리자드 이런 것들 풀다가 이거 푸니까 조금 할만 했다. .? 
    
    - 잘한 점
        문제를 잘 읽어서 에러가 났을 때 바로 어떤 요소겠다 의심 잘했음
        디버거 사용 굿
    - 못한 점
        오타 .............
        또 생긴 빈틈
        
=========================구상메모=================================

모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
    이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
    같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
    파이어볼은 4개의 파이어볼로 나누어진다.
    나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
        질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
        속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
        합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
        질량이 0인 파이어볼은 소멸되어 없어진다.

파이어볼 관리 방법 ,,
3차원으로 [m, s, d] 넣어서 관리하기  이걸로 ㄱ
dict에 (r, c)를 key로 넣어서 관리하기 ? 한 칸에 여러개 있을 수 있으므로 이건 안됨

for k in range(K)
    #파이어볼 이동시키기 (동시에 이동 돼야 하므로!!! 따로 배열 만들기)

    #배열 탐색 - 파이어볼 두개 이상이면
    개수 l
    질량 합 sm
    속력 합 ss
    모두 홀수, 짝수여부 확인

"""

#입력
#배열에 파이어볼 넣기..
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]

dir = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

###############33
# 1, N 연결됨 주의 !!!!!!!!!!!!!!!!!!!!!!!!

for k in range(K):
    # 파이어볼 이동시키기 (동시에 이동 돼야 하므로!!! 따로 배열 만들기)
    new_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue
            for m, s, d in arr[i][j]:
                di, dj = dir[d]
                du = i+di*s
                dv = j+dj*s

                # N-1과 0 연결. 1에서 더 가는건 어차피 음수로 처리됨
                du%=N
                dv%=N

                new_arr[du][dv].append([m, s, d])

    arr = [[[] for _ in range(N)] for _ in range(N)]

    #이동된 애들 (new_arr) 두개 이상이면 합치고 나누기
    for i in range(N):
        for j in range(N):
            if len(new_arr[i][j])==1:
                arr[i][j] = new_arr[i][j][:]
            elif len(new_arr[i][j]) >=2:
                l = len(new_arr[i][j]) #개수
                sm = 0
                ss = 0
                d_remainder = 0
                for m, s, d in new_arr[i][j]:
                    sm+=m
                    ss+=s
                    d_remainder += d%2

                next_m = sm//5
                next_s = ss//l
                if next_m == 0:
                    continue
                if d_remainder == l or d_remainder==0:
                    d_lst = [0, 2, 4, 6]
                else:
                    d_lst = [1, 3, 5, 7]
                for d in d_lst:
                    arr[i][j].append([next_m, next_s, d])
answer = 0
for i in range(N):
    for j in range(N):
        for m, s, d in arr[i][j]:
            answer+=m
print(answer)


    # 배열 탐색 - 파이어볼 두개 이상이면
#     개수 l
#     질량 합 sm
#     속력 합 ss
#     모두 홀수, 짝수여부 확인