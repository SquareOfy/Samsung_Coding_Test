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