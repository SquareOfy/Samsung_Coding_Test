"""
총 풀이 시간 : 1시간 50분

1차 제출
실행 시간 : 7984ms
메모리 :128048 kb

2차 제출
실행 시간 : 4504 ms
메모리 : 125248 kb


1647 문제 읽기 시작 및 구상 (7분)
    - 이전에 풀이했던 기억을 최대한 죽이려고 했다. .
    - 잊혀지지 않는 내 기존 구상
    - 당시에 개선한 구상이 있어 한번 생각해보긴 함 ;
    - 약간 그리디한 방식의 구상이었는데, 앞에를 변화시키면 뒤에 변화되는 변수가 너무 많아서
        적합하지 않다고 판단해서 완탐을 고려함
    - 그렇게 기존 아이디어를 내려놓자 dfs로 충분히 가능하고 오히려 이 방법이 쉽구나를 느끼고 설계

---------중간에 잠깐 멈췄었음 왜 멈췄는지 기억안남------------------

1658 주석 설계
    - 가로선을 나타내는 배열은 세로선보다 열이 한칸 더 적으므로 인덱스가 헷갈릴 것
    - 명확히 하기 위해 주석으로 디테일하게 잡으려고 노력..
    - 이 때 시간복잡도도 계산해보며 살짝 아슬아슬할 것 같아 Combination으로 꼭 중복 없이 해야함 체크

1708 구현시작
    - 인덱스 주석에 달아놔서 비교적 덜 헷갈리며 구현
    - 사다리 내리는 부분 중간 프린트로 확인했음
1801 제출 -> 시간초과
    - 원인이 뭘까 찾아보기 ..
        - 뽑은 칸을 lst에 담아 들고다니며 중복은 없는지 체크
        - 그리고 코드 살펴보다 시간초과는 아니지만 index틀린 것들 찾음..
        - available을 매번 세팅하고 배열 복사하는게 원인일까 싶어서 available 배열 없애고
            그냥 그 칸에서 양쪽에 가로 사다리칸이 있는지 확인하는 방식 + 기존 배열 체크 해제하는 방식 사용
1808 제출 또ㄸ또또 시간초과 ...
    - 1개, 2개 ,3개 고를 때를 매번 각각 dfs로 새로 찾는다는 사실 발견
    - 그냥 쭉 3개를 고르고, 그 전에 1,2개 고를 때마다 원하는대로 사다리가 내려오는지 체크하는 방식으로 수정
    - 이후 시간초과 아니고 오답 나와서 코드 뜯어보다가 인덱스 틀린것 수정
    - 그리고 진짜진짜 멍청한 실수 ... 처음부터 조건 만족했을 때 -1 출력

피드백
    - 잘한점...
        내가 취약한 유형인가 싶어 일부러 문제 풀고 한참 있다가 다시 도전했다 !(?)
            조금이나마 처음 보는 느낌이고 싶어서 !

        없는데 굳이 뽑자면 내 아이디어가 안되는 점을 나중에라도 뜯어살핀 점....
            될 지도 모르지만,, 구현의 난이도가 화아아아악 올라가는 건 확실 ..
    - 못한점
        - 기본적인 출력 조건 제대로 확인 안해서 실수
        - 평소에 배열에 마진을 안넣어 인덱스를 늘 0으로 시작하는 편인데 이 문제에서는 편의상 1로 했다.
            그러자 인덱스 실수 와다다다ㅏㄷ ! 하던대로 하던가 어쩔 수 없이 패턴을 바꾼 문제는 종이에 대왕 별로 써놓기
        - 시간초과.. 아무리 시간이 넉넉한 구현문제라도 너어어무 비효율적으로 짜면 시간초과 난다
            시간복잡도 계산 + 너무 비효율적으로 짠건 아닌지 점검하자 ..!

    -
"""

"""
가로선을 나타내는 배열 만들기

i행 j열이 1이면 j번째 열과 j+1번째 열을 i행에서 연결하는 가로선..!
초기 입력값을 받아 1 ~ n 까지의 세로선에서 출발해서 도착하는 열을
arrived_lst 에 저장

arrived_lst[i]와 i의 관계
    arrived_lst[2] = 0
        : 0번 세로선에서 출발한게 2번 세로선에서 도착
        : arrived_lst[i] ~ i (range(0, 2))를 보며 그 라인 가로칸에
        가로칸 이미 추가했으면 continue.
        추가 안했고 다음에 만날 가로보다 행 값 더 낮은 칸에 추가 가능하면 추가.
        아니면 다음칸에 추가 가능한지 봐야함
available 로 가로선이 이미 있거나 양 옆에 있는경우 불가하다는 표시 해놓기.
    하지만 이렇게 하면 앞에 선택한 값이 뒤에도 영향을 주어 확신이 서지 않는다.
그리디하게는 어렵겠다. 위 방법으로 백트래킹 돌자 !!
    arrived_lst[i]에서 선을 놓을 때
    arrived_lst[i]+1에서 선 놓을 때

혹은 그냥 사다리 추가 한개 해보기
두개 해보기
3개 해보기...

시간복잡도 : 300개 중 1개 + 300개 중 2개 300개 중 3개
        Combi 로 해야 가능할 것 같다
        2차원이니까
        i, j 를 선택하고 나면 i, j+1부터 보도록 하고 ! 그 다음 i+1부터 다 보기
        j+1이 마지막이면 i+1, 0부터 보도록 하기


"""

import sys
sys.setrecursionlimit(10000)


def dfs(level, si, sj):
    global answer
    #이미 찾았으면
    if level >= answer or level == 4:
        return

    # down = (garo)
    # if check(down):down_ladder
    #     answer = level
    #     return
    if check_down_ladder():
        answer = level
        return

    #선택할 가로 사다리 탐색
    for j in range(sj, N):
        if garo[si][j]: continue
        if (j-1>=1 and garo[si][j-1]) or (j+1<N and garo[si][j+1]):
            continue
        garo[si][j] = 1
        nj = j+1 if j<N else 1
        ni = si if nj!=1 else si+1
        #여기 선택했으니 다음 선택 하러가기
        dfs(level+1, ni, nj)
        garo[si][j] = 0

    #아랫 줄도 보기
    for i in range(si+1, H+1):
        for j in range(1, N):
            if garo[i][j]:
                continue
            #왼쪽이나 오른쪽에 이미 가로선이 있으면
            if (j - 1 >= 1 and garo[i][j - 1]) or (j + 1 < N and garo[i][j + 1]):
                continue
            garo[i][j] = 1
            nj = j + 1 if j < N else 1
            ni = i if nj != 1 else i + 1
            # 여기 선택했으니 다음 선택 하러가기
            dfs(level + 1, ni, nj)
            garo[i][j]=0

def check_down_ladder():
    for i in range(1, N+1): #출발 세로선 번호
        sero = i
        for j in range(1, H+1):
            if sero<N and garo[j][sero]:
                sero+=1
                # print("오른쪽 이동")
            elif sero-1>=1 and garo[j][sero-1]:
                sero -=1
        if sero!=i:
            return False
    return True


# def check(down):
#     for i in range(1, N):
#         if down[i] != i:
#             return False
#     return True
#세로선 개수, 입력되는 가로선 개수, 세로선 마다 놓을 수 있는 위치의 개수(행 값)
N, M, H = map(int, input().split())

garo = [[0]*(N) for _ in range(H+1)]

#불가능한 곳 0으로 바꾸기
for i in range(M):
    #b번세로선과 b+1번 세로선을 a번 점선 위치에서 연결
    a, b = map(int, input().split())
    garo[a][b] = 1

if check_down_ladder():
    print(0)
else:
    answer = 4
    dfs(0, 1, 1)
    print(answer if answer<4 else -1)