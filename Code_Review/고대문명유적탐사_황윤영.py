"""
코드리뷰
총 풀이시간 1시간 25분
실행시간 455MS
메모리 29MB


0900 문제 읽기 시작
    원래 읽다가 종이에 안썼는데 우선순위 좀 특이하길래 메모 해놓음 이걸로 실수할까봐

    조건 주석에 옮기기
    구현할 영역 바로 위에 !!! 근데 이거 어느 정도 구현하고 나서는 좀 치워야하나 싶다;
    코드 볼 때 꽤나 방해됨

0908 설계시작
    종이에 설계.
    함수화 자세히 설계 / 이 때 회전할 위치 고르는 우선순위가 꽤 복잡해서 처음에 설계에 애먹음
    전체적인 구조도 설계

0932 구현시작
    1) 입력받기 + 회전 위치 선정 구현 + 중간테스트 ( 16분)
        중간에 우선순위 조건문 쓰면서 for문으로 장치를 해두면 조건문 한번이면 되겠다고 생각이 들었음
        맨날 이걸 생각 못했는데 코드리뷰시간에 다른 팀원들이 저렇게 하는거 많이 보다보니 자연스레 떠올랐음
        bfs 설계를 개수 체크하는거 0 만드는거 따로 하려고 햇는데 막상 하다보니 합칠까 하는 생각이 들어서
        중간에 우왕좌왕햇었음. 결국 그냥 실수 안하게 따로하기로 결정
    2) 유적 지우고 값 answer에 더하는 로직 + 빈칸 채우는 로직 구현 - 16분
        유적 지우는 로직 조금 설계 덜 돼서 그 순간에 좀 생각해서 풀었음
        value를 다 구하고 3이상이면 해야하는데 냅다 그냥 0만들려다가 아차차차ㅏ 함!
    3) 유적 더 연쇄될 거 있나 하는 로직은 기존 함수 재활용 함 ~ 굿 ~~
1005 디버깅 시작
    회전 위치 잘 못받아온다? 그냥 for문 우선순위로 충분할 줄 알았는데 t는 그 위치마다 0, 1, 2가 다르므로
    다시 비교하는 조건문 추가해줌

    calculate로 종료시키는게 while문 뿐이라 for문을 한번 더 돌아서
    rotate위치를 못잡을 때 (없어지는게 없을 때) 한번 더 break 처리 해줌

1017 제출 후 오답
    뭐지 ! 난 맞았는데 .. 라고 생각했지만 아마 틀렸겠지
    적당한 테케 없길래 틀렸습니다 테케 가져와서 프린트 다시 찍어봄

    회전 돌아가는 거 보다가 오잉 ㅇ이상하다를 느꼈고
    로직 다시 살펴보니 회전 횟수 열심히 구해놓고 딱 한번만 회전시켜줘버림...
    해당 부분 수정 후 재제출. 정답

피드백
    - 잘한점
        어제 그제 마구마구 기출에 때려맞았지만 그래도 멘탈 유지하고 푼 것..^^
        주석으로 내 로직에 대한 설명을 중간중간 추가한 것.
    - 못한점
        중간테스트를 너무 못했다
        멘탈을 유지했다곤 하지만 조급함이 중간테스트를 놓치게 만드는 것 같다...
        충분히 절차가 있어서 테스트하기 괜찮은 문제였는데도 ,,!


"""

"""
    문제조건 정리
   # 5×5 격자 내에서 3×3 격자를 선택하여 격자를 회전
    # 시계 방향으로 90도, 180도, 270도 중 하나의 각도만큼 회전
    # 단, 선택된 격자는 항상 회전을 진행

    #  (1) 유물 1차 획득 가치를 최대화
    #  (2) 회전한 각도가 가장 작은 방법 -for문 순서
    # (3) 회전 중심 좌표의 열이 가장 작은 구간을, - for문 순서로 해결
    # 열이 같다면 행이 가장 작은 구간 - for문 순서로해결

    # [2] 유물 획득
    # 유적의 벽면에 써 있는 숫자를 사용한 이후에는 다시 사용할 수 없다
    # 이후 부터는 남은 숫자부터 순서대로 사용
    # 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결 => 조각들이 3개 이상 연결되면 유물 => 사라짐
    # 유물의 가치는 모인 조각의 개수 ( 조각의 수가 부족한 경우는 없다)
    # 물이 사라지고 난 이후 새로 생겨나는 조각 넣는 순서
    #  유적의 벽면에 적혀있는 순서대로 새로운 조각이 생겨납니다
    # (1) 열 번호가 작은 순으로 조각이 생겨납니다
    # (2) 열 같다면 행 번호가 큰 순으로 조각이 생겨납니다.
    # 2.  유물 연쇄 획득
    # 새로운 유물 조각이 생겨난 이후에도 조각들이 3개 이상 연결될 수 있으며
    # 앞과 같은 방식으로 조각이 모여 유물이 되고 사라진다
    # 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을 때까지 반복

"""
from collections import deque


def oob(i, j):
    return i >= 5 or j >= 5 or i < 0 or j < 0


def find_rotate():
    mx = 0
    selected_r, selected_c, rotate_cnt = -1, -1, -1
    # 배열 복사
    tmp = [[] for _ in range(5)]
    for t in range(5):
        tmp[t] = arr[t][:]
    for j in range(1, 4):
        for i in range(1, 4):
            # 회전할 부분 복사
            selected_tmp = [[] for _ in range(3)]
            for t in range(3):
                selected_tmp[t] = tmp[i - 1 + t][j - 1:j + 2]

            # 오른쪽으로 90도 회전 3번은 bfs 1번은 배열 원상복구용
            for t in range(4):
                # 오른쪽으로 90
                selected_tmp = list(map(list, zip(*selected_tmp[::-1])))

                # tmp 배열에 붙여넣기
                for tt in range(3):
                    tmp[i - 1 + tt][j - 1:j + 2] = selected_tmp[tt][:]

                if t == 4: break  # tmp 원상복구 해놓고 다음 경우 고려하러 가기
                value = calculate_value(tmp)

                if mx < value:
                    selected_r, selected_c, rotate_cnt = i, j, t
                    mx = value

                elif mx == value and t < rotate_cnt:
                    selected_r, selected_c, rotate_cnt = i, j, t

    return selected_r, selected_c, rotate_cnt


def check_bfs(i, j, tmp):
    q = deque([(i, j)])
    visited[i][j] = 1
    cnt = 0
    while q:
        cr, cc = q.popleft()
        cnt += 1
        for di, dj in DIR:
            du = cr + di
            dv = cc + dj
            if oob(du, dv) or visited[du][dv]:
                continue
            if tmp[du][dv] == tmp[i][j]:
                visited[du][dv] = 1
                lst.append((du, dv))
                q.append((du, dv))

    return cnt


def calculate_value(tmp):
    global visited
    visited = [[0] * 5 for _ in range(5)]
    value = 0

    for i in range(5):
        for j in range(5):
            if visited[i][j]: continue
            v = check_bfs(i, j, tmp)
            if v >= 3:
                value += v
    return value


def delete_value(num, i, j):
    visited[i][j] = 1
    q = deque([(i, j)])
    del_lst = []

    while q:
        cr, cc = q.popleft()
        del_lst.append((cr, cc))
        for di, dj in DIR:
            du = cr + di
            dv = cc + dj

            if oob(du, dv) or visited[du][dv]:
                continue
            if arr[du][dv] == num:
                q.append((du, dv))
                visited[du][dv] = 1
    if len(del_lst) >= 3:
        for r, c in del_lst:
            arr[r][c] = 0
        return len(del_lst)
    return 0


def get_value():
    global visited
    visited = [[0] * 5 for _ in range(5)]
    value = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j]:
                value += delete_value(arr[i][j], i, j)
    return value


def new_piece():
    global idx
    for j in range(5):
        for i in range(4, -1, -1):
            if arr[i][j] == 0:
                arr[i][j] = lst[idx]
                idx += 1


# 5×5 격자 형태  ||| 유물 조각은 총 7가지 종류 1부터 7
K, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
idx = 0  # 새로운 유물 조각 시작 idx
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
# 총 K 번의 턴에 걸쳐 진행
answer_lst = []
for k in range(K):
    answer = 0  # 매턴마다 출력이므로

    visited = [[0] * 5 for _ in range(5)]
    r, c, rotate_cnt = find_rotate()

    if r == -1 and c == -1:
        break

    # 회전할 부분 복사 후 회전 - 원배열에 붙여넣기
    selected_tmp = [[] for _ in range(3)]
    for t in range(3):
        selected_tmp[t] = arr[r - 1 + t][c - 1:c + 2]

    for tt in range(rotate_cnt + 1):
        selected_tmp = list(map(list, zip(*selected_tmp[::-1])))

    for tt in range(3):
        arr[r - 1 + tt][c - 1:c + 2] = selected_tmp[tt][:]

    while 1:
        # 유물 획득하기
        answer += get_value()
        # 새로운 조각 넣기
        new_piece()

        v = calculate_value(arr)
        if v == 0:
            break
    if answer == 0:
        break
    answer_lst.append(answer)

print(*answer_lst)

# 출력
# 각 턴마다 획득한 유물의 가치의 총합을 출력
# 아직 K번의 턴을 진행하지 못했지만,
# 어떠한 방법을 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료
# 위처럼 종료되는 턴에 아무 값도 출력하지 않음