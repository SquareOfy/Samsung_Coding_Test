"""
총 풀이시간 1시간 38분
실행시간 264ms
메모리 117432kb

1448 : 어항정리 문제 잠깐 읽다가 이건 무조건 어렵다 싶어 원판돌리기로 도망와서 문제읽기
        - 컨베이어 벨트 문제처럼 pointer 배열 두고 실제 배열을 움직이지 않고, pointer 기록해서 구현하고자 생각함
        - 인접한건 파이썬은 -1 인덱스도 되고 +는 그냥 모듈해주면 되겠다 생각하고 구상 및 설계함
        - 원판에서 인접한 숫자가 같으면 그 숫자들을 지우기 / 하나도 지우지 않는 경우 동작과 같이 여러 단계로 동작이 많아서
          주의해야겠다고 생각함,,
1458 : 대략적인 설계 내용 주석에 쓰기 시작+구현시작
        - x 배수 때문에 편하게 하려고 인덱스 1부터 시작 -> 나중에 원형 연결 처리 인덱스 -1로 처리하려고 0으로 수정
            - 초기 설계 잘하기 ,,
        - 회전구현 완료 후 중간 테스트 했음
        - pointer로 설계해놓고 상하좌우 인접 확인할 때 pointer로 안찾고 그냥 arr[(i+1)%n][j] 이런식으로 해버리는 실수 함
            - 구현하다 중간에 발견하고 수정했으나 수정에 빈틈이 너무 많았음
            - 중간에 0만들기 잘했는지 테스트 한번 해봤으면 좋았을듯
1508 : 테케로 테스트해본 후 디버깅 시작
        - 위에서 pointer에 맞게 인덱스 변환하면서 생긴 빈틈들 위에서부터 찾아가며 수정
        - pointer와 arr 함께 출력해보며 어디가 겹쳤는지 확인하며 풀고자 함
        - pointer로 구현하다보니 인접한 부분을 체크하는게 매우 어려웠음;
            - 지금 생각해보니 슬라이싱 이용해서 인접 부분 보기 편하게 출력했다면 더 디버깅이 쉬웠겠다
        - 테케 1번은 맞고 2번은 틀리길래 여기저기 디버깅하고 문제 그림이랑 비교해봄
            - 회전을 k번이 아니라 1번시킨 것 발견 ^^ .. 진짜 바보;
1539 : 지운적 없는 경우 처리 이상해서 디버깅
        - 평균을 실수로 구해야 함을 알아차림
        - 수정 중 멍청한 오타도 생겼었음
        - 수정 후에도 안맞아서 그리고 인접한 숫자 찾기도 힘들어서 코드를 뒤엎어야하지 않을까 생각
1542 : 코드 뒤엎기 시작 . rotate 함수가 있는 deque활용하기로 함 => 재 구현
        - roate에 매개변수 0보다 클 때 작을 때 출력해서 확인해보고 사용함(잘해쓰)
1550 : 구현 완료 후 테스트했으나 안맞음
        - 회전까진 잘 돌아감
        - 평균 부분 이상함
        - 문제 다시 보니 평균이 특정 원판이 아니라 전체임을 알았고 수정

        그.런.데.도 안.맞.아. 무한디버깅,,
        회전한 원판 계속 출력해보며, 지워지지 않은 숫자, 빠진 숫자 등등 체크해 봄
        인접해있는데 0이되지 않고 살아있는 5를 발견...
        설계 미흡임을 깨닫고 바로 bfs 함수 만듦.... (1610 경)

        - bfs arr[r][c] 0으로 만들기 위한 리스트 반환했으나
            인접한 숫자 없을 때도 그 점은 반환돼서 모든 점 0 만들어버리는 문제 발생
            수정 후 원형이라 인덱스 끝점 연결되는거 놓친 것도 발견해서 고침

반성..
- 초기 설계 미흡하거나 잘못한 경우가 너무 많은 것 같다. 이런건 어떻게 고쳐야할 지 고민
- 한번 설계가 잘못됐다는 사실을 알고 나서 고치기 시작하면 당황해서인지 실수를 더 남발한다.
- 왜 꼭 구현난이도가 높은 방법을 택하는가. 원판이라는 요소, 여러 단계의 동작이 있었지만
  전반적으로 구현 난이도가 많이 높은 문제는 아니었다고 생각한다. 다만, 내가 택한 방법이 난이도를 높였다..
    => 아이디어가 떠오른다고 무조건 들어가지 말기
    => 가능한 한 두세개 떠올리고 구현 난이도가 더 쉬운걸로 들어가자.


그나마 잘한점
- 잘 뒤집어 엎었다 윤영아 ... 다음엔 더 빨리 엎자. 엎을 일을 되도록 만들지 말고;







"""
"""뒤집어엎기"""
from collections import deque

def bfs(i, j):
    q = deque([(i,j)])
    v = arr[i][j]
    visited[i][j] = 1
    lst = []
    while q:
        r, c = q.popleft()
        lst.append((r,c))
        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            du = r+di
            dv = c+dj
            if dv == -1:
                dv = M-1
            elif dv==M:
                dv = 0
            if du<0 or du>=N:
                continue
            if visited[du][dv]:
                continue
            if arr[du][dv] == v:
                visited[du][dv] = 1
                q.append((du,dv))
    return lst
N, M, T = map(int, input().split())
arr = [deque(list(map(int, input().split()))) for _ in range(N)]
# q = deque([0, 0, 1]) #rotate >0 시계방향 <0 반시계방향

for t in range(T):
    visited = [[0]*M for _ in range(N)]
    x, d, k = map(int, input().split())
    if d == 1:
        k *= -1
    for i in range(x-1, N, x):
        arr[i].rotate(k)

    change = False
    #인접 동일 숫자 지우기
    for i in range(N):
        for j in range(M):
            v = arr[i][j]
            if v==0:
                continue
            lst = bfs(i, j)
            # print(lst)
            if len(lst)==1:
                continue
            for r, c in lst:
                arr[r][c] = 0
                change = True
            # flag = False
            # #안쪽 원
            # if i-1>=0 and arr[i-1][j] == v:
            #     arr[i-1][j] = 0
            #     flag = True
            # if i+1<N and arr[i+1][j] == v:
            #     arr[i+1][j] = 0
            #     flag = True
            # if arr[i][(j+(M-1))%M] == v:
            #     arr[i][(j+(M-1))%M] = 0
            #     flag = True
            # if arr[i][(j+1)%M] == v:
            #     arr[i][(j + 1) % M] = 0
            #     flag= True
            # if flag:
            #     arr[i][j] = 0
            #     change = True
    # print("지운 후 ")
    # for k in range(N):
        # print(arr[k])
    # print("")
    #지워진 적 없으면 평균내기
    if not change:
        # print("지운 적 없음")
        sum_num = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]:
                    sum_num+= arr[i][j]
                    cnt+=1
        if cnt!=0:
            mean = sum_num / cnt
            # print(mean)
            for r in range(N):
                for c in range(M):
                    if arr[r][c]==0:
                        continue
                    if arr[r][c]>mean:
                        arr[r][c]-=1
                    elif arr[r][c]<mean:
                        arr[r][c]+=1

s = 0
for i in range(N):
    s += sum(arr[i])
print(s)

# """
#
# 원판 입력배열 유지
# pointer 배열로 0 번째에 있는 index를 관리해서 원판 회전 표현하기
# 시계방향은 -1 반시계는 +1
#
# 회전 후 인접하면서 같은 수 지우기
# 0 아니면
# arr[i-1][j] arr[(i+1)%rmod][j] arr[i][j-1] arr[i][(j+1)%cmod] 체크
#
# 지운적 없으면(flag)
# 평균 구해서 평균보다 큰 수들엔 -평균, 작은 수엔 +평균
# """
#
# # 입력
# N, M, T = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# pointer = [0] * N  # 0부터 M-1이 모듈로 들어감
# for t in range(T):
#
#     # x: x의 배수에 해당되는 애들만 회전 => 얘 땜에 인덱스 1 시작이 편하겠다
#     # d: 0 이면 시계 1이면 반시계
#     x, d, k = map(int, input().split())
#
#     for i in range(x - 1, N, x):
#         # 회전시키기 by pointer
#         if d == 0:
#             pointer[i] -= k
#         else:
#             pointer[i] += k
#         pointer[i] %= M
#     erase = False
#
#     # print("회전 구현 확인")
#     # for i in range(N):
#     #     print(arr[i])
#     # print()
#     # print(pointer)
#     # print()
#     # 구현실수 발견,, 인접이 그냥 처음 기준으로 보면ㅇ ㅏㄴ되고 포인트 관련지어서 봐야함,,
#     for i in range(N):
#         p = pointer[i]  # 현재 보고 있는 원의 pointer
#         for j in range(M):
#             cc = (j+p)%M #이번에 보는 r_index
#             v = arr[i][cc] #값
#             if v==0: #이미 지워진 적 잇으면 넘어가
#                 continue
#             # 현재 봐야할 index는 p + j
#             flag = False
#
#             # 안쪽 원
#             if i-1>=0 and arr[i - 1][(pointer[i - 1] + j)%M] == v:
#                 arr[i - 1][(pointer[i - 1] + j)%M] = 0
#                 flag = True
#
#
#             # 바깥쪽 원
#
#             if i+1<N:
#                 nr = (i + 1)
#                 nc = (pointer[nr] + j) % M
#                 if arr[nr][nc] == v:
#                     arr[nr][nc] = 0
#                     flag = True
#
#             #왼쪽
#             if arr[i][cc - 1] == v:
#                 arr[i][cc - 1] = 0
#                 flag = True
#             #오른쪽
#             if arr[i][(cc + 1) % M] == v:
#                 arr[i][(cc + 1) % M] = 0
#                 flag = True
#
#
#             if flag:
#                 arr[i][cc] = 0
#                 erase = True
#                 print(i, j, arr[i][j])
#                 print(pointer)
#                 for k in range(N):
#                     print(arr[k])
#                 print()
#     if not erase:
#         print("지운 적 없음")
#         for i in range(N):
#             circle_sum = 0
#             l = 0
#             for j in range(M):
#                 if arr[i][j] == 0:
#                     continue
#                 circle_sum += arr[i][j]
#                 l +=1
#             if l==0:
#                 continue
#             mean = circle_sum / l
#             print(circle_sum)
#             print(l)
#             for j in range(M):
#                 if arr[i][j] > mean:
#                     arr[i][j] -= 1
#                 elif arr[i][j] < mean and arr[i][j]!=0:
#                     arr[i][j] += 1
# s = 0
# for i in range(N):
#     print(arr[i])
#     s += sum(arr[i])
#
# print()
# print(pointer)
# print(s)
# # 배열 마진 중간체크
# # for i in range(N+1):
# #     print(arr[i])
