"""
1차
풀이 시간 : 32분
시도 횟수 : 1회
실행 시간 : 96ms
메모리 : 110680kb


2차
풀이 시간 : 45분
시도 횟수 : 3회
실행 시간 : 143ms
메모리 : 25mb

실수 모음
- 복사한 코드에서 수정 미흡으로 오타 발생
- 로직 제대로 설계 안해서 인덱스 실수

"""
"""
========================== 2차 코드 리뷰 ====================

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 
    : 가다가 작아지는 방향 말고 반대도 봐야한다 ! OOB 점검 해야한다 !! 
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : 안함 간단했음
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : 문제 발생 후 함 
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!! 

1416 문제 읽기 시작 + 주석정리 
1422 설계 .
    한 줄 씩 보면서 앞칸 나보다 차이 1보다 클 때 넘기고
    1차이 날 땐 누가 더 크냐에 따라 작은 쪽을 경사로 놓기 가능한지 체크하려고 함
    for문이 중첩될거라 flag보단 함수화가 편하겠다고 생각함 
    
1428 구현 시작
1436 디버깅 시작 
    테케 안맞음. 조건 분기스러운 문제라 놓친 조건 찾아야지 생각
    코드 복붙하느라 인덱스 똑바로 수정 안함; 
    내가 왼쪽보다 작을 때는 나를 포함한 경사로.
     내가 클땐 나를 안포함하고 왼쪽으로 L개의 경사로인데 둘다 나를 포함하거나 안포함하게 해서 틀림
     
총평 : 1차 코드가 더 이쁘군 
    1차보다 못한 코드를 짠듯하다 
    특히 왼쪽 혹은 위로 경사로를 놓을 때, 다시 탐색하기 보다 지금까지 동일한 수의 개수를
    세어왔어서 바로 판단할 수 있게 짰던게 좋았다. 똑똑했군 ;
    실수 많이 했다 기록해놓고 실수 리스트 업데이트 해야지 ,,
    테케가 미흡했으니 내가 숫자 몇개 수정해서 상황별로 테스트 해봤으면 오답 안났을 것 같다 ,,  
     
"""

"""
크기가 n * n인 인도 / 보도블럭의 높이

경사로는 높이가 1이며 길이 L

경사로는 높이 차이가 1이 나는 보도블럭에 설치가능하며, 낮은 칸에 설치
경사로의 길이 L동안 바닥에 접촉해야하며,
경사로가 놓인 보도블럭의 높이는 모두 같아야 합니다.


다음과 같은 경우에는 경사로를 놓을 수 없습니다.
높이 차이가 1 보다 큰 경우
경사로의 길이만큼 낮은 칸의 보도블럭이 연속하지 않는 경우
경사로를 놓은 곳에 또 경사로를 놓은 경우
"""
def is_possible_row(i):
    # print(f"================={i } 행 check======================= ")
    for j in range(1, N):
        if abs(arr[i][j-1] - arr[i][j]) >1:
            # print("많이 차이남")
            # print()
            return False
        if arr[i][j-1] == arr[i][j]: continue
        if arr[i][j-1]>arr[i][j]:
            #앞으로 총 L칸 확인하기
            if j+L-1 >=N:
                # print(j)
                # print(j+L)
                # print("앞에 L 공간 부족")
                # print()
                return False
            for k in range(0, L):
                if arr[i][j+k] != arr[i][j] or visited[i][j+k]:
                    # print("울퉁불퉁 또는 경사로 중복")
                    # print()
                    return False
                visited[i][j+k] = 1
        elif arr[i][j-1]<arr[i][j]:
            #뒤로 총 L칸 확인하기 (나 미포함)
            if j-L < 0:
                # print(j-L)
                # print("뒤에 L 공간 부족")
                # print()
                return False
            for k in range(1, L+1):
                if arr[i][j-k] != arr[i][j-1] or visited[i][j-k]:
                    # print("뒤에 울퉁불퉁 또는 경사로 중복")
                    # print()
                    return False
                visited[i][j-k] = 1
    # print("통과")
    # print('=======================================')
    return True

def is_possible_col(j):
    for i in range(1, N):
        if abs(arr[i-1][j] - arr[i][j]) >1:
            return False
        if arr[i-1][j] == arr[i][j]: continue
        if arr[i-1][j]>arr[i][j]:
            #앞으로 총 L칸 확인하기
            if i+L-1 >=N:
                return False
            for k in range(0, L):
                if arr[i+k][j] != arr[i][j] or visited[i+k][j]:
                    return False
                visited[i+k][j] = 1
        elif arr[i-1][j]<arr[i][j]:
            #뒤로 총 L칸 확인하기
            if i-L < 0:
                # print(j - L)
                # print("뒤에 L 공간 부족")
                # print()
                return False

            for k in range(1, L+1):
                if arr[i-k][j] != arr[i-1][j] or visited[i-k][j]:
                    # print("뒤에 울퉁불퉁 또는 경사로 중복")
                    # print()
                    return False
                visited[i-k][j] = 1
    # print("통과")
    # print('=======================================')
    return True


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answer = 0
for i in range(N):
    #i행 가능한지 열 점검
    if is_possible_row(i):
        answer+=1

visited = [[0] * N for _ in range(N)]
for i in range(N):
    if is_possible_col(i):
        answer+=1

print(answer)



"""
1500 문제읽기시작
1506 문제 이해 완 구상시작
1532 구현 및 디버깅 완료 / 코드트리 정답

디버깅 중 내려갔다가 올라가는 중에 이미 경사로 놓은 곳 처리 미흡해서 디버깅 시간 걸림



===================구상==========================
1. 행과 열 각각 고려하므로 행끼리 개수 세기 / 열끼리 개수 세기 각각 하기
2. 경사로는 visited에 체크 .
    그래서 1차이 나는 곳 이동할 때 낮은 쪽 자리에 visited 1인지 체크하여 통행여부 체크

3. 경사로깔기 : 왼쪽에서 오른쪽으로 탐색(행기준으로 살펴보자)
    탐색할 때 이전 값을 봐야하니까 1부터 시작
    - 수가 커지든 작아지든 그 차이가 2 이상이면 무조건 불가능
    - 수가 작아지는 경우
        그 순간부터 cnt 하기 cnt==L되면 시작지점부터 visited체크
        cnt<L 이고 다른 값 나오면 바로 FALSE 이므로 그 행은 cnt 안하기

    - 수가 커지는 경우
        그 지점부터 L만큼 뒤로가며 cnt세고 가능한지 보기
        가능하면 visited 체크하고 넘어가기
"""
def check_row(i):
    cnt= 1 #연속된 수 기록
    for j in range(1, N):
        if visited[i][j]:
            continue
        if arr[i][j-1]==arr[i][j]:
            cnt+=1
            continue
        if abs(arr[i][j-1]-arr[i][j]) >=2:
            #이 행은 경사로 놔도 통행 불가
            # print("2이상 차이나서 실패")
            return False

        #수가 커지는 경우
        if arr[i][j-1]<arr[i][j]:
            if cnt>=L: #지금까지 연속된 수가 L보다 컸다면 가능
                for k in range(L):
                    if visited[i][j-1-k]:
                        return False
            else:
                # print("수가 커지는 경우 실패 :  ",  j)
                # print(cnt)
                return False
        #수가 작아는 경우
        else:
            for k in range(L):
                #j부터 L개의 칸을 보기 (자리 있나 없나 + 같은 숫자인가)
                if j+k >=N or arr[i][j+k]!=arr[i][j]:
                    # print("수가 작아지는 경우 실패 :  ", j)

                    return False
                visited[i][j+k] = 1
        cnt = 1
    return True

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
visited = [[0]*N for _ in range(N)]
#행 개수 탐색(i행이 경사로 놓아서 통행 가능한지 체크)
for i in range(N):
    # print("행, ", i)

    if check_row(i):
        answer+=1
# print("answer : " , answer)
arr = list(zip(*arr))
visited = [[0]*N for _ in range(N)]

for i in range(N):
    # print("열, ", i)
    if check_row(i):
        answer += 1
print(answer)