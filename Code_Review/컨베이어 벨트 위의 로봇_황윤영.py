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
