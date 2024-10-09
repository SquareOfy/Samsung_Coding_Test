"""
1624 문제읽기 시작
    - 보자마자 헉 했다. 단계가 너무 많고, 어항을 회전해서 쌓아올리는 부분의 구현방법이 떠오르지 않음
    - 함수화가 중요한 문제라 생각함
        (반복되는 로직 많음,, 하지만 결론적으로 너무 복잡해서 함수를 처음부터 분리해놓는 설계를 하진 못했음)
    - 회전해서 올리는걸 어떻게 구현할까,, 리스트로는 불가능하다고 생각해서 배열을 세로로 늘여서 리스트 안에 리스트를 넣는 방식을 고안

1645 회전함수 구현, 입력받기
    - 회전함수에서 튜플말고 리스트로 변환하는 문법이 조금 서툴다 ;; 외워버리자
    - 헷갈려서 여러번 출력해보며 내가 원하는 모양이 나오는지 확인하며 구현했음

1652 어항쌓기 구현 시작 (극악) (44분....)
    - 어항을 회전해서 배열에 넣는 방식은 어렵지 않았으나,
    - 회전할 배열을 뽑아올 인덱스와 회전한 배열을 넣기 시작할 인덱스를 잡고 다음 인덱스를 구하는 과정이 몹시 매우 헷갈렸음
    - 처음에 여기저기 막 넣어보다가 더 혼란스럽게 되는 결과 초래....
    - 어항 쌓는게 잘 되다가 break 포인트를 못잡음
    - 손으로 어항을 그려보며(특히 마지막 지점 : 회전하는 배열의 인덱스와 다음 칸의 인덱스가 다를 때를 그림)
      인덱스를 어떻게 잡아야할 지 찾았음

1735 어항쌓기 구현완료 및 물고기 수 조절 구현시작
    - 뒤에도 물고기 쌓기가 있으므로 함수화하기로 함
    - 비교적 쉬웠음 . d가 5나눈 값인 거에서 살짝 버벅임
    ===============여기 구현하고 시간 종료


1831 다시 이어서 코드구현시작
    - 다시 일렬로 놓기 구현 ㅇㅋ
    - 공중부양 구현 너무 어려웠음 (바닥 면적이 n//4가 되도록 해야한다는 점 간과하고 디버깅 많이 하기도 함)
    - 공중부양의 매개변수를 시작점과 길이로 받아서 수정함 (처음엔 한번만 동작하는 거에 맞춰서 짰었음)

1900 find gap 함수 구현시작(while문 종료조건 갱신할 함수)
    - 최종 출력조건보다 위 절차를 구현하는데에 집중해서 미리 while 문 안만들어놨었음
    - while문 안에 넣을 부분 탭해서 while문 추가...
    - 구현 완료 했으나 이상하게 무한루프를 돌고 3번째 테케인가는 딱 숫자하나가 안맞음

1910 무한디버깅...
    - 대체 어디서 문제가 생겼는지 알 수 없어 전반적으로 단계를 거칠 때마다 print출력
    - 손으로 그려보고 눈으로 따라가며 체크
    - 문제 조건에 어긋나는 부분이 없었는데 답이 달랐음
    - 문제 다시 읽음..
    - 코드 다시 읽음
    - min인 어항에 1 더 해주는 로직이 while문 밖에 있는 것 발견하여 해결

반성...
- 파이써닉한 사고를 하자 .. ! 코테에 유리하도록.. 너무 자바스러웠따 ..(원판도 이것도 ,, )
    [[2*2], [1*4]]가 들어갈 수 있었다 ..굳이 세로로 변환할 필요가 없었더라 
- 문제 조건을 잘 읽고 처음에 틀을 짜놓자 ... 나중에 수정하다가 실수가 발생했따

잘한점,,
- 함수화 잘함
- 어려운 방식의 구현 방법이었지만 끝까지 구현해냈다 ..^^ 굿잡



-----------------------------------구상메모---------------------------------------
아예 구현 아이디어가 떠오르지 않는다 ;

일단 배열 오른쪽으로 90도 회전해서 반환하는 함수 만들어서
계속 써야할 것 같다

#어항쌓기 생각해보자
눕혀서는 어렵다
세로로 늘여서 수를 위로 쌓는걸 그 리스트에 append한다고 생각하자
l = 1 (쌓아갈 애의 길이)
for i in range(0, n)
    arr[i:i+l]를 시계방향으로 회전하기 (어차피 눕혀있던것도 시계방향으로 회전해서 똑같)
    그리고 남은 자리 n - i+l+1+1 이 지금 내 len(arr[i:i+l})보다 긴 지 확인
    길지 않다면 break


[5]
[2]
[3]
[14]
[9]
[2]
11
8
"""
def control():
    s = set() #좌표, 방향 (쌍방으로 넣기)
    #(행 열 d) 로 넣기
    tmp_arr = []
    for i in range(n):
        if not arr[i]:
            continue
        for j in range(len(arr[i])):
            for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
                du = i+di
                dv = j+dj
                if du<0 or du>=n:
                    continue
                if len(arr[du]) <= dv or dv<0:
                    continue
                if (i, j, di, dj) in s:
                    continue
                s.add((i, j, di, dj))
                s.add((du, dv, -di, -dj))
                d = abs(arr[i][j] - arr[du][dv])//5
                if d==0:
                    continue
                if arr[i][j]<arr[du][dv]: #i, j가 작으면
                    tmp_arr.append((i, j, d))
                    tmp_arr.append((du, dv, -d))

                elif arr[i][j]>arr[du][dv]:
                    tmp_arr.append((i, j, -d))
                    tmp_arr.append((du, dv, d))

    for i, j, v in tmp_arr:
        arr[i][j] += v
def fly(st, k):

    left = arr[st:st+k//2]
    left = rotate(rotate(left))

    for i in range(k// 2):
        arr[st+k // 2 + i].extend(left[i])
        arr[st+i].clear()


def rotate(a):
    #배열 2차원으로 주어짐
    return [list(i) for i in list(zip(*a[::-1]))]


def pprint():
    for i in range(n):
        print(arr[i])

def set_line():
    idx = 0
    tmp = [[] for _ in range(n)]
    for i in range(n):
        l = len(arr[i])
        if l == 0:
            continue
        if l == 1:
            break
        for j in range(l):
            tmp[idx].append(arr[i][j])
            idx += 1
        arr[i].clear()
    for i in range(idx):
        arr[i].extend(tmp[i])

def find_gap_min():
    mx = 0
    mn = 10000

    for i in range(n):
        mx = max(mx, max(arr[i]))
        mn = min(mn, min(arr[i]))
    return mx-mn, mn


n, k = map(int, input().split())
arr = list(map(int, input().split()))
mx = max(arr)
#가장 적은 애들한테 +1
mn = min(arr)
gap = mx-mn
answer = 0


# 배열 세우기
arr = [[int(i)] for i in arr]
while gap >k:
    answer += 1
    for i in range(n):
        if not arr[i]:
            continue
        for j in range(len(arr[i])):
            if arr[i][j]==mn:
                arr[i][j]+=1
    #어항 쌓기
    next_len = 1
    bottom_len = 1
    i = 0
    while i<n:
        #회전할 배열
        tmp = rotate(arr[i:i+bottom_len])
        next_len = len(arr[i])

        if i+bottom_len+next_len>n:
            break

        #회전한 배열 올릴 수 있으면
        for j in range(next_len):
            arr[i+bottom_len+j].extend(tmp[j])
        for j in range(bottom_len):
            arr[i+j].clear()

        i += bottom_len
        bottom_len = next_len
    #어항쌓기 완료


    #물고기 수 조절
    control()
    #물고기수조절 확인 완료

    #다시 일렬로 놓기
    set_line()

    #공중부양
    fly(0, n)
    fly(n//2, n//2)

    #물고기 수 조절
    control()
    #바닥에 일렬로 놓기
    set_line()
    gap, mn = find_gap_min()

print(answer)
