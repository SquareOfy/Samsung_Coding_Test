"""
1차 풀이시간 : 50분
2차 풀이 시간 : 20분
    실행 시간 : 185ms
    메모리 : 25mb

실수 모음
- 출력 실수함!!
- 값 1부터 시작인 거 실수함
"""
"""
============================2차 코드 리뷰===========================
1920 문제읽기 시작.
    동시 회전인 걸로 크게 깨졌어서 각성하고 그 부분 봄.
    문제 주석 정리 

1930 구현시작

1934 디버깅 시작 
    값이 0 나옴 . 원인 파악을 위해 의자 출력. 
    회전이 안된다? 회전 정보 담은 리스트 출력
    문제와 다른 회전 정보 ..for문에 i값 출력 -> i값이 이상하다 ! 
    인덱스 1 시작 의심해서 해결
 
"""

"""
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 주의할 사항, 테스트케이스 외에 고려할 사항, 생각해보기 + 설계에 반영 : 동시에 회전시키는 것! 출력값!
5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리 : 안함. 구현단계가 많지 않고 까다롭지 않아서 손설계로 충분했다고 생각
7. 구현 ok
8.테스트케이스 단계별 디버깅 확인 ok rotate_lst 찍어서 확인해봄. deque도
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 해당없음

Debugging CheckPoint
- N, M / 행 열 index 오타 실수 점검
- max, min 구할 때 초기값 체크
- 배열 사용 목적 확인 후 배열 변수 실수 확인
- continue, break, return 부분이 로직적으로 맞는지. break해서는 안되는데 했다거나 break로는 빠져나오기가 안된다거나
- 조건분기문 복사한 경우 모두 바꿨는지 체크
- 디버깅해서 바꾼 코드 부분 혹은 로직이 있다면 그 부분 중심으로 전반적으로 재점검
- 문제 조건 + 코드 로직 같이 따라가며 이상한 로직 없는지 점검
- 로직이 맞는데 답이 이상하다면 아주 사소한 순서 문제는 없을지 점검

Reset Timing
- 1시간 ~ 1시간 반 : 코드 다 짰는데 테케 정답이 엉망진창?
    문제 이해 미흡, 설계 미흡일 확률 높으므로 문제 다시 읽고 리셋할 모듈 찾을지 전체 리셋할지 판단하기
- 1시간 반 쯤에 코드 대부분이 잘 돌아가는데 특정 포인트에서 안되는 것 같다?
    - 특수한 테케가 있는지 1차로 점검해보고 디버깅
    - 오타 찾아야할 것 같다 => 그냥 리셋해버리자


"""

"""
4개의 팔각 의자 두 지역에서 온 사람들 N과 S 
팔각 의자는 왼쪽에서부터 오른쪽까지 각각 1번부터 4번까지의 번호

각각의 의자를 총 k번 회전
한 번 회전할 때 45도씩 즉 한 칸을 움직임
회전은 시계 방향과 반시계 방향 모두 가능

회전 요청 규칙
n번째 의자가 회전하기 전 인접한 의자(n-1번째와 n+1번쨰)에 있던 의자에서 제일 가깝게 마주치는
두 명의 사람의 출신 지역이 다르다면 n번째 의자가 회전할 때 인접한 의자 또한 반대 방향으로 회전하게 됩니다.

회전 요청에 따라 의자를 회전시킨 후  그로 인해 일어나는 모든 회전이 끝날 때까지 기다립니다.
 한 번 회전한 의자는 다시 회전하지 않습니다.

 남쪽지방 사람 착석여부를 각 테이블에 대하여 s1, s2, s3, s4라고 할 때 1*s1 + 2*s2 + 4*s3 + 8*s4를 출력

"""

from collections import deque

chair_lst = [deque(list(map(int, list(input())))) for _ in range(4)]
K = int(input())
for k in range(K):
    n, d = map(int, input().split())
    n -= 1
    rotate_lst = [0] * 4
    rotate_lst[n] = d
    for i in range(n + 1, 4):
        if chair_lst[i - 1][2] == chair_lst[i][6]:
            break
        rotate_lst[i] = rotate_lst[i - 1] * (-1)
    for i in range(n - 1, -1, -1):
        if chair_lst[i + 1][6] == chair_lst[i][2]:
            break
        rotate_lst[i] = rotate_lst[i + 1] * (-1)
    for i in range(4):
        if rotate_lst[i] == 0:
            continue
        chair_lst[i].rotate(rotate_lst[i])
answer = 0
for i in range(4):
    if chair_lst[i][0] == 1:
        answer += 2 ** i
print(answer)

"""
1640 문제이해완
구현 및 디버깅에 정신 없어서 시간기록 못함

1730 제출

풀이시간 : 50분

=============문제점들 ================
문제를 잘못 이해함.
의도한 바대로 구현은 문제가 없었으나, 회전하기 전에 모두 회전할 의자(톱니바퀴)를 정하고
한번에 회전했다는 부분을 놓침 (문제 읽으며 메모 했는데도 .......)
문제를 어떻게 하면 안 놓치고 한번에 꼼꼼히 이해할 지 대책이 필요하다...

이후 디버깅 하는 과정에서 앞 문제로 인해 당황했는지,
여기서도 디버깅 엉망진창
회전 기록하는 배열 다음 라운드에서 리셋안함,,,
내가 짠 로직을 잘 이해하고 어느 지점에서 변수나 배열을 리셋할지, 잘 점검하며 코드짜자!!


============구상 및 주의점 ================
연쇄적으로 회전이 발생한다는 점과
한번 회전한 의자는 회전 안한다는 점에 주의할 것

함수 매개변수
idx : 회전시킬 의자의 번호
d : 회전방향
from : 회전이 어떤 방향에서 왔는지(어느방향으로 퍼지는 중인지)
    -이면 왼쪽 확인할 것 +1이면 오른쪽 확인할것 0이면 시작시점

왼쪽을 변화하는지 볼 때는 나의 pointer+2와 상대의pointer +5비교
오른쪽은 나의 p + 5와 상대의 p+2
"""

def rotate_chair(idx, d, fm):
    #회전시키기
    rotate_lst[idx] = d
    #왼쪽회전함수 호출
    if fm == -1 or fm ==0:
        if idx-1 >=0:
            p = (pointer[idx]+6)%8
            yp = (pointer[idx-1]+2)%8

            if arr[idx][p] != arr[idx-1][yp]:
                # print("왼")
                rotate_chair(idx-1, -d, -1)
    if fm==1 or fm==0:
        if idx+1<4:

            p = (pointer[idx] + 2) % 8
            yp = (pointer[idx+1] + 6) % 8
            # print(p, yp)
            # print(arr[idx][p], arr[idx+1][yp])
            if arr[idx][p] != arr[idx+1][yp]:
                # print("오")
                rotate_chair(idx+1, -d, 1)

pointer = [0]*4
arr = [list(map(int, list(input()))) for i in range(4)]
k = int(input())
for i in range(k):
    rotate_lst = [0] * 4
    idx, d = map(int, input().split())
    rotate_chair(idx-1, d, 0)

    for j in range(4):
        pointer[j] = (pointer[j] - rotate_lst[j]) % 8


# print(pointer)
answer =0
for i in range(4):
    p = pointer[i]
    answer += (2**i)*arr[i][p]

print(answer)