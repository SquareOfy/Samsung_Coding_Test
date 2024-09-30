"""
1914 문제 읽기 + 조건 주석으로 정리 (복사함)
1916 주석 슈더코드 작성 및 추가 구상
      처음엔 뱀 머리 꼬리만 인덱스로 가지고 있으려했는데
      꼬리가 움직일 방향을 알 수 없다 생각해서 deque 사용하기로 결정
      함수로 구현할 파트도 이 때 정함

1929 구현시작

1937 디버깅 시작
    테케가 너무 크게 나온다. 원인이 뭘까 문제와 코드 뜯어보기 시작
        while문의 now, x 조건 조절해봤는데 하면서도 처음 내 코드가 맞다는 생각, 처음이 맞았음
        for문의 방향 전환 값과 배열 출력해봄
        영상 보다보니 tr,tc 값 출력해서 확인 후 계속 print남겨두는 것 발견
        확인이 끝났다 싶은 print는 지우고 그 때 확인할 print만 남겨도 될듯. 디버깅에 방해요소
        arr[r][c]==1에서 ==1 누락 발견
    두번째 테케가 너무 터무니 없이 안맞는다. 21인데 13
        출력해봤을 때 크게 뱀의 움직임엔 문제가 없어보여서
         문제 읽다가 주어진 방향전환에서 무조건 게임이 끝난다는 보장이
        없다는 걸 깨달음
        => 뒤에 추가 while 문 추가
    그래도 테케가 안맞고 특히 세번째 테케가 너무 이상하다 .
        while문은 반드시 앞에서 게임이 종료되지 않은 경우에만 들어와야한다.
        flag 도입
    그래도 테케 안맞네. 주어진 print 가지고 손 그림 그려봤지만 테케 답이 안맞다(모순)
    내가 이상할 것.원인을 찾자. => 인덱스 1 시작 확인 ;; 어휴
        이 과정에서 oob 조건 바꿔보는 등 별별 삽질 시도
    다 고쳤는데 테케 안맞다?
        인덱스 때문에 안맞는 문제 해결해보려고 했던 oob 시도가 아직 남아있음 발견
        이동방향 전환 내에 끝나는 테케 1,3과 달리 2만 답과 1차이 나길래
        바로 for문 이후 while문을 봤음

피드백
- 잘한점
    답과 다른 테케가 있으면 다른 것과 구별되는 요소를 찾아 그 부분의 코드를 찾아 디버깅한것
    함수 미리 설계

- 못한점
    코드가 답과 안맞는다고 문제를 이렇게? 저렇게? 해석해보며 고친 것. .
    제대로 문제를 이해하고 딱 고칠 부분을 정하고 고치도록 해보자..
    주먹구구로 고치다가 마지막에 다 고쳤어도 앞에 주먹구구가 수정되지 않아
    답이 안맞는 상황이 왔음



=================== 구상 ======================
뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다
뱀은 처음에 오른쪽을 향한다

뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
    몸길이는 변하지 않는다.

꼬리의 방향을 모르므로 몸인 부분 전체를 저장해둬야한다 .
deque 사용 ?
[(머리), (중간1), ... (중간..) , (꼬리)]
=> 사과 있으면 새로운 머리를 맨 앞에 끼워넣어준다
=> 사과 없으면 새로운 머리 맨 앞 끼워넣고 + 꼬리 끝에 하나 없앤다.

# 몸 옮길 때마다 배열에 표시하자 ! ? 아니면 (좌표) in deque로 확인하기 ..


now = 현재시간
for x, d 방향 변환정보 :

    ###############여기 함수화##################
    while now < x: #현재 방향 변환 정보의 시간과 일치할 때까지
        현재 머리 위치
        hr, hc = q[0]
        hr += di
        hc += dj
        now +=1
        #oob 체크. 몸 체크
            return False
        배열에 몸 체크
        사과 있으면 continue
        사과 없으면 꼬리 삭제 q.pop()

    # x초가 됐다 !
    # 방향 전환하기
    if d == L:
        d= (d-1)%4
    else:
        d= (d+1)%4
"""
from collections import deque


def oob(i, j):
    return i < 0 or j < 0 or i >= N or j >= N


def move(x):
    global now, flag
    # x초까지 움직이기
    di, dj = dir[d]
    while now < x:
        hr, hc = q[0]
        hr += di
        hc += dj
        now += 1
        if oob(hr, hc) or arr[hr][hc] == 1:
            return False

        if arr[hr][hc] != -1:
            tr, tc = q.pop()
            # print(tr, tc)
            arr[tr][tc] = 0

        q.appendleft((hr, hc))
        arr[hr][hc] = 1

    return True


dir = (0, 1), (1, 0), (0, -1), (-1, 0)
N = int(input())
K = int(input())

arr = [[0] * N for _ in range(N)]
for i in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = -1

L = int(input())
change = [list(input().split()) for _ in range(L)]
now = 0
q = deque([(0, 0)])
d = 0
flag = True
for x, change_d in change:
    x = int(x)
    if not move(x):
        flag = False
        break

    if change_d == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
di, dj = dir[d]
while flag:
    hr, hc = q[0]
    hr += di
    hc += dj
    now += 1
    if oob(hr, hc) or arr[hr][hc] == 1:
        break
    if arr[hr][hc] != -1:
        tr, tc = q.pop()
        # print(tr, tc)
        arr[tr][tc] = 0

    q.appendleft((hr, hc))
    arr[hr][hc] = 1

print(now)
