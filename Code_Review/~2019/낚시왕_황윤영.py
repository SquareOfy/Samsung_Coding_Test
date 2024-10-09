"""
0900 문제읽기 시작

0906 입력받기 + 구현시작
    - 상어들을 queue에 넣어두고 꺼내어 구현하기로 설계
    - 상어 이동 구현
        - 중간 테스트하자마자 에러
        - 왔다갔다 핑퐁 식으로 이동한다는 것 다시 이해해서 수정
    - 바꾼방향으로 이동하고 큰놈에게 잡아먹히거나 먹거나 아니면 그냥 이동하거나 구현
    - 테케 안맞음 이슈 -> 프린트 해보니 상어 위치가 아주 제멋대로
        - 하나씩 잡아내보자! 코드 뜯어보기!
        - 오타 발견 ! d 가리키는 배열 %2 가 아니라 %4
    - 또 안맞
        - 프린트 과정 하나씩 뜯어봄
        - 상어 제대로 잡는지 확인 + 상어 위치 확인
        - 상어가 동시에 짠 하고 움직여야한다는 것 깨달음(기존 배열에 원래 있던 상어가 방해됨)
        - move 배열 새로 만들어서 넣어두고 다 움직이고 arr에 복사했음
        - 상어 목록은 list에 새로 들어가는 상어 위치 append 후 한꺼번에 q 에 extend
     - 또. 안. 맞
        - 무한 뜯어보기 + 무한 문제읽기 + 무한 로직 따라가기
        - list에 상어 위치 넣어서 관리하면 상어를 잡아먹은 경우 위치가 중복으로 들어간다는 사실 발견
        - set으로 변경해서 관리했음
1059 정답....

피드백
- 잘한점
    1. 디버거 + condition 사용
    2. 코드를 뜯어보는 기술이 꽤나 향상됏을지도 .. 그래도 많은 실수ㅠ
- 개선할 점
    1. 코드를 뜯어보기 전에 뜯어볼 필요가 없게 설계 잘하기
        - 동시에 움직이는 경우에 진짜 실수가 잦음을 느낌. 이럴 때 각성할 것
    2. 종이에 뭘 막 적긴 하는데 활용도가 낮다. 유의미한 것만 적자.
        종이 메모는 문제에서 유의미해서 꼭 기억하고 싶을 때 한번 더 나에게 강조시키는 용도
        그림이 복잡하거나 테케 혼자 테스트해볼 때 활용
        슈더코드 작성할 때 !

"""
from collections import deque
#입력
r, c, m = map(int, input().split())
shark = {}
arr = [[0] * (c+2) for _ in range(r+1)]
q = deque([])
directions = (-1, 0), (0, 1), (1, 0), (0, -1)
d_change = [0, 0, 2, 1, 3] #위 아래 우 좌를 상 우 하 좌로 change
# 1 위 / 2 아래 / 3 오른쪽 4 왼쪽
answer =0
for i in range(1, m+1):
    sr, sc, s, d, z = map(int, input().split())
    arr[sr][sc] = i
    shark[i] = (s, d_change[d], z)
    q.append((sr, sc))

for x in range(1, c+1): #오른쪽 한칸 이동 구현
    #이 열에서 가장 가까운 상어 잡기
    for y in range(1, r+1):
        if arr[y][x] == 0:
            continue
        answer += shark[arr[y][x]][2]
        # print(x)
        # print(f"잡았당 : {arr[y][x]} {shark[arr[y][x]][2]}")
        arr[y][x] = 0
        break
    #상어 이동
    move = [[0] * (c + 2) for _ in range(r + 1)]
    new_shark = set()
    for k in range(len(q)):
        #꺼낸 상어
        cr, cc = q.popleft()
        #상어 정보

        num = arr[cr][cc]
        #이미 잡힌 상어

        if num == 0:
            continue
        s, d, z = shark[num]

        #바꾼 방향으로 가다가 자리 벽 만나면 방향 반대로 남은 칸 가는 거임
        nr = cr
        nc = cc
        di, dj = directions[d]
        for p in range(s):
            nr+=di
            nc+=dj
            # 상어가 범위 벗어나면 방향 반대로 바꿈
            if nr < 1 or nr > r or nc < 1 or nc > c:
                di*=-1 #방향바꾸기
                dj*=-1 #방향바꾸기
                d= (d+2)%4 #바꿀 방향 저장해야해서 d 관리
                nr += di*2 #되돌아오기 + 반대로 방향바꿔 한칸
                nc += dj*2
        #이동 마쳤으면 새로운 방향정보 업데이트
        shark[num] = (s, d, z)

        #바꾼 방향으로 이동하는데 이미 상어가 있다면? 큰놈이 잡아먹기
        #아니면 이동
        if move[nr][nc] !=0:
            #이미 상어가 있고 그 상어가 나보다 크면
            b_size = shark[move[nr][nc]][2]
            if b_size>z:
                #나는 죽음
                continue

        #상어 있어도 내가 더 크거나, 상어 없으면
        #내가 들어가기
        move[nr][nc] = num
        #다음 상어 위치
        new_shark.add((nr, nc))
    q.extend(list(new_shark))

    #상어 이동정보 업데이트
    for i in range(r+1):
        arr[i] = move[i][:]
print(answer)




