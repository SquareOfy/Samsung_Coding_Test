"""
코드리뷰

총 풀이시간 1시간 34분
실행시간 776 ms
메모리 28 mb

1500 문제 읽기 시작
    문제 길어보여서 일단 정독
    중간에 동시 조건 실수 잘해서 메모해둠
    해야되는 절차 종이에 살짝씩 메모하며 주의해야할 것들 (상언가 물고긴가 냄새 문제로 배운 것..)메모
    나무 전파되는 부분 글 읽고 생각한대로 계산해보며 그림과 함께 맞는지 점검
1510 손설계 시작
    주어진 절차대로 각 절차 어떻게 구현할지 꽤 상세하게 손으로 슈더코드 작성
    주의해야할 것들 네모 쳐둬서 나중에 봄

1521 정리한 내용 + 문제 내용 복사해서 다시 주석으로 정리하고 구현시작
    이 때 주의할 것들 느낌표 잔뜩해줌

1523 주석으로 구현할 영역 전반적으로 남겨두고 구현함
    성장, 번식, 제초제 감소 각 단계별로 중간 프린트로 체크함

1551 구현 완료 후 제출했으나 틀림
    규모가 또 큰 테케라 난감했고...
    토론방에서 가져온 것도 쉽지 않았다

    성장, 번식 순서대로 살펴보고 제초제 뿌릴 리스트 살펴봐도 틀린게 안보인다
    계에속 문제 다시읽기 코드 살펴보기 무한 반복. .

    이 디버깅만 40분을 넘게 했다.
    분명 제초제 쪽이 문제일 것 같은데(다른 부분은 너무 확실하게 잘 돌아가는게 보임)
    어디가 문제일지 감이 안잡힘
    결론 => 계속 살피다가 벽이 있는경우 가로막혀 제초제가 전파되지 않는다는 말이 의미심장하게 다가와서
    그 부분 코드를 다시 살펴봄

    제초제가 벽을 만났을 때 !!!!!!!!!!!!!! break가 아니라 continue를 했다
    k for문을 코드 구현하면서 나중에 추가했는데 이부분이 문제였다. .

피드백
    - 잘한점
        끝까지 설계하고 코드 들어갔따
        키보드 늦게 잡는거에 별로 초조해하지 않음
    - 못한 점
        슈더코드 너어어어어무 잘 적어놓고 왜 디버깅할 때 슈더코드랑 안맞춰봤을까?
            슈더코드에도 처음에 continue 적었다가 두줄 긋고 break한 흔적 있었음 ㅠㅠ
            중첩 for문을 쓰면서 continue, break쓸 때 걸리는 for문이 어떤 건지 꼭 살피자






"""

"""

1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어납니다.
2. 기존에 있었던 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에 번식을 진행
    나무 그루 수 // 상하좌우 중 빈칸의 수(벽, 나무, 제초제 x) 만큼
    "동시에!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

3. 나무가 가장 많이 박멸되는 칸에 제초제를 뿌립니다
    나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만,
    나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파
    단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지고
    그 이후의 칸으로는 제초제가 전파되지 않습니다.

     여기서 그 칸까지는 뿌려지는게 포인트1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가
     c+1년째가 될 때 사라지게 됩니다.
     제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.

     제초제 빼는 타이밍 주의 !!!!!!!!!!!!!!!!!!!!!!!!!!!!1
"""


def oob(r, c):
    return r < 0 or c < 0 or r >= N or c >= N


def print_arr():
    for i in range(N):
        print(arr[i])
    print()


# 입력 받기
N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dir = (-1, 0), (0, 1), (1, 0), (0, -1)
diagonal = (-1, -1), (-1, 1), (1, -1), (1, 1)
answer = 0

# M년 반복
for m in range(M):

    # 성장
    # 상하좌우 보고 나무 있는 칸 수 세서 그만큼 더하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt = 0
                for di, dj in dir:
                    du, dv = i + di, j + dj
                    if oob(du, dv): continue
                    if arr[du][dv] > 0:
                        cnt += 1
                arr[i][j] += cnt
    # print("==============성장확인")
    # print_arr()
    ##############체크 완

    # 번식
    # 리스트 만들어서 번식할 목록 넣어놓고 한번에 반영할 것
    # 제초제, 벽, 나무 없는지 확인하고 얘네 없는 칸에 그 칸 수 만큼 나눈 나무 더하기
    spread_lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and not visited[i][j]:
                cnt = 0
                lst = []

                for di, dj in dir:
                    du, dv = i + di, j + dj
                    if oob(du, dv): continue
                    if visited[du][dv]: continue  # 제초제 없고
                    if arr[du][dv] == 0:  # 나무 없는 칸(벽도 아니고 나무도 있는 것도 아님)
                        cnt += 1
                        lst.append((du, dv))
                if cnt == 0:
                    continue
                tree_cnt = arr[i][j] // cnt
                spread_lst.append((tree_cnt, lst))
    for tree_cnt, lst in spread_lst:
        for i, j in lst:
            arr[i][j] += tree_cnt

    # print("=============번식확인=================")
    # print_arr()
    # ############################확인 완
    # print('===============이 때 제초제 ================')
    # for i in range(N):
    #     print(visited[i])
    # print()

    kill_lst = []
    # 제초제 뿌릴 후보 찾자
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -1:
                continue
            # if visited[i][j]:
            #     continue
            lst = []
            kill_cnt = arr[i][j]  # 나무 있는 칸이면 나무개수 아니면 0
            lst.append((i, j))
            if arr[i][j] == 0:
                kill_lst.append((kill_cnt, i, j, lst))
                continue
            for di, dj in diagonal:
                du, dv = i, j
                # 대각선 방향으로 k칸만큼 간다
                for k in range(K):
                    du += di
                    dv += dj
                    if oob(du, dv) or arr[du][dv] == -1: break
                    if arr[du][dv] != -1 and arr[du][dv] != 0 and not visited[du][dv]:  # 나무가 있는 칸이면
                        kill_cnt += arr[du][dv]
                    lst.append((du, dv))
                    if arr[du][dv] == -1 or arr[du][dv] == 0 or visited[du][dv]:  # 벽이거나 나무가 없으면 이 칸까지만 하고 끝
                        break
            kill_lst.append((kill_cnt, i, j, lst))

    kill_lst.sort(key=lambda x: (-x[0], x[1], x[2]))
    # print("=========================제초제 후보 ==========================")
    # for t in kill_lst:
    #     print(t)
    # print("========================================================")

    # 제초제 감소
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                visited[i][j] -= 1

    # 제초제 뿌리기 : C로 갱신하기 위해 감소부터 해준다
    for i, j in kill_lst[0][3]:
        visited[i][j] = C
        arr[i][j] = 0
    # print("제초제 이후 =================")
    # print_arr()
    answer += kill_lst[0][0]

print(answer)