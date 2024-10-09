"""
1차
풀이 시간 : 46분
시도 횟수 : 2회
실행 시간 : 380ms
메모리 : 199112 KB


2차
풀이 시간 : 44분
시도 횟수 : 2회
실행 시간 : 272 ms
메모리 : 115444 KB

- 실수 모음 (또옥같은 실수 함)
    - people_lst에 안움직이는 경우 다시 안넣어줌 *2
    - 문제 조건 누락(N-1 될 때마다 내리는거)
    - 문제 조건 누락(벨트에 올라타는 순서와 위에 있는 애들 옮기는 순서 틀림)

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
=================== 2차 코드 리뷰 ==========================
1549 문제 읽기 + 주석 정리 
    DEQUE 써야겠다는 생각은 드는데 풀이 잘 기억 안났음; 
    다시 다시 생각하기 ..
    
1555 설계
    n-1칸에서 바로바로 안내려줘서 틀린 기억이 나서 그 부분 주의함
    대신 다른거 놓침 ㅠ
1607 주석 구현영역 정리 + 구현
1615 테케 안맞아서 디버깅 시작 
    사람 안올린것 발견 -> 고침
    사람 옮기는 순서 잘못 설계해서 lst 추가 
    
    nxt와 비교할 게 N-1이 아니라 deque의 N-1번째에 있는 숫자라는 것 파악
    
    사람 안올린 것도 나중에 추가하면서,
     꼼꼼하게 확인 못하고 냅다 앞에다 올려서 테케 안맞은 이슈
    사람 옮기는 순서 잘못 설계하는 바람에 lst 추가한 이후 
    안움직일 때 그대로 원래 값을 lst에 append 하는 로직 누락해서 틀림
    
손설계 조금 대충했더니 바아아로 엉망진창 실수해버리기 !@~!@
어떤 로직이 누락돼서 코드를 수정할 땐 정확히 어디에 추가해야할지 
어떻게 변경해야할지 한번 더 짚고 수정하자 ! 
"""
"""
 무빙워크는 사람을 한 쪽 끝에서 반대쪽 끝으로 옮겨주는 기계
 다음과 같이 총 2n개의 판으로 구성
무빙워크의 레일은 시계 방향으로 회전 (1, 2N 연결됨)

각 사람은 1번 칸에 올라서서 n번 칸에서 내리게 됩니다.
사람이 어떤 칸에 올라가거나 이동하면
그 칸의 안정성은 즉시 1만큼 감소하게 되며 안정성이 0인 칸에는 올라갈 수 없습니다.

무빙워크가 한 칸 회전합니다.

가장 먼저 무빙워크에 올라간 사람부터 무빙워크가 회전하는 방향으로 한 칸 이동할 수 있으면 이동합니다.
만약 앞선 칸에 사람이 이미 있거나 앞선 칸의 안정성이 0인 경우에는 이동하지 않습니다.

1번 칸에 사람이 없고 안정성이 0이 아니라면 사람을 한 명 더 올립니다.

안정성이 0인 칸이 k개 이상이라면 과정을 종료합니다. 그렇지 않다면 다시 위의 과정을 반복합니다.

단, 1~3 과정 중 n번 칸 위치에 사람이 위치하면 그 즉시 내리게 됩니다.
각 칸의 안정성은 시간에 지남에 따라 다시 상승하지 않습니다.


무빙워크가 종료될 때 몇 번째 실험 중이었는지를 출력
"""
from collections import deque
#입력
N, K = map(int, input().split())
stability_lst = list(map(int, input().split()))
moving_q = deque([i for i in range(2*N)])
visited = [0]*(2*N)
answer = 0
cnt = 0
people_lst = []
#while
while 1:
    answer += 1
    #rotate
    moving_q.rotate(1)

    up = moving_q[0]
    down = moving_q[N-1]

    #N-1에 있는 사람 내리기
    visited[down] = 0
    # print()
    # print(moving_q)
    # print(visited)
    # print(people_lst)
    # print("stable : ", stability_lst)
    # print()

    new_people = []
    #사람이동 2*N 부터 순차적으로 볼 것.
    for i in people_lst:
        #사람 있으면 이동할 칸 보기
        if visited[i]:
            nxt = (i+1)%(2*N)
            #안정성 0이거나 앞 칸에 사람 있으면 이동 불가
            if stability_lst[nxt] ==0 or visited[nxt]:
                new_people.append(i)
                continue
            #앞칸 내리는 위치면 안정성만 -1
            #아니면 visited 처리도 하기

            if nxt != down:
                visited[nxt] = 1
                new_people.append(nxt)

            stability_lst[nxt] -= 1

            #안정성 앞자리 0 되면 cnt+1
            if stability_lst[nxt] == 0:
                cnt+=1

            #기존 visited해제
            visited[i] = 0
    people_lst = new_people[:]
    # 1에 사람 올리기
    if not visited[up] and stability_lst[up] > 0:
        visited[up] = 1
        people_lst.append(up)
        stability_lst[up] -= 1
        if stability_lst[up] == 0:
            cnt += 1
    #종료조건 체크
    if cnt>=K:
        break
print(answer)

from collections import deque
"""
1508 문제읽기 시작
1516 문제 이해 완 / 주석 구상 시작
1538 구현하고 디버깅,, 
~1545 내리는 위치 항상 도달 즉시 내리는 것 처리 안한 것 발견 . ! 시간초과..
1545~ 무한루프 가능성,, 테케 생각해보자. 종료 조건문 수정
1554 정답

풀이시간 : 46분
실행시간 : 380ms
메모리 : 199112 KB
실패 원인
    1. 문제 조건 내 마음대로 k이상을 ==k로 변경,,
    2. 문제에서 "내리는 곳에 도달할 때마다"라는 부분 간과 
    결론 . 문제를 꼼꼼히 읽는 데에 시간 더 투자하자..

====================================================================
visited : 0 ~ 2N-1칸에 로봇 있/없 확인
lst : 0~2N-1칸 내구도 관리
q : 벨트 위의 로봇들 넣어두기
up : 올리는 위치에 와 있는 칸의 idx /-1씩 줄어듬, mod 2N
down : 내리는 위치에 와 있는 칸의 idx/ -1씩 줄어듬, mod 2N

answer : 현재 단계 / 1부터 시작

while문 내에서 주어진 단계 차례대로 수행
    - 벨트 회전 ( up, down 조절)
        로봇 이동 (내구도, visited 체크)
    - 현재 올리는 위치의 내구도 visited 체크 후 로봇 올리기(내구도 -=1 visited체크)
    - 내구도 0 개수 확인 및 break
    - answer 더하기
"""

n, k = map(int, input().split())
lst = list(map(int, input().split()))
mod = 2*n
power = lst.count(0)
visited = [0] * (2*n)
up = 0
down = n-1
q = deque([])
answer = 1
while 1:
    up = (up-1)%mod
    down = (down-1)%mod
    size = len(q)
    for i in range(size):
        t = q.popleft()
        nt = (t+1)%mod
        if t==down: #내리는 곳에 도달한 애면 내려버리기
            visited[t] = 0
            continue
        if not visited[nt] and lst[nt]>0: #다음칸 옮길 수 있음
            visited[t]=0
            lst[nt]-= 1
            if lst[nt]==0:
                power += 1
            if nt!= down: #다음 칸이 내리는 곳이 아니면 계속 벨트 위에 있음
                visited[nt] = 1
                q.append(nt)
        else: #못 옮기면 가만히 있기
            q.append(t)

    if not visited[up] and lst[up]>0:
        q.append(up)
        visited[up] = 1
        lst[up]-=1
        if lst[up]==0:
            power +=1
    if power >= k:
       break
    answer+=1

print(answer)
