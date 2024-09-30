"""
풀이 시간 : 1시간 4분
실행 시간 :308ms
메모리 : 118888kb

2047 문제 읽기 시작
    - 문제를 다시 꼼꼼히 읽으며, 그 날 내가 문제를 풀지 못했던 요인은
        문제를 맘대로 해석해서 문제난이도를 셀프로 올렸기 때문임을 느낌
    - 문제를 읽으며 10*10 배열 만들어야지 생각
    - 인덱스 주의해야겠다고 생각 => 주석에 남겨둠

2056 구현할 순서대로 주석으로 구현 자리 마련 + 구현할 방식 메모
2059 구현시작
    - 한칸 짜리 일 때, index 찾는 함수를 만들어서 2칸 짜리일 때도 활용
    - 파란색과 초록색 영역이 행/열이 반전된다 이렇게 구현해야할 부분이 많아 코드가 길어질 것 같았다
        그리고 그럴수록 디버깅은 더 복잡해질 것.. 그래서 함수 내에 is_row flag를 두고 이걸로 함수 내에서
        한번에 구현했다..
        이걸로 코드 수정을 한번만 해도 되는 효과를 보았지만, 어떤게 파란색이고 어떤게 초록색이더라 하며 헷갈리기도 했음
    - 세 종류의 블록에서 공통 로직인건 if문 밖으로 빼서 한번의 코드로 처리하려고 노력했다

2123 디버깅
    블록 이동까지는 이쁘게 잘되는데 연한부분에 블록 있을 때 삭제 + 밀기 부분이 이상하다
        코드 살펴보기 + 프린트 디버깅 활용해서 블록이 잘 쌓이는지 다시 확인하고
        잘 쌓이는 것 확인 후에는 삭제할 행 탐색하는 부분 확인
        그것까지 확인 후에는 미는 push함수 확인했다
        순차적으로 메모장에 결과값 복사해서 그림과 비교하며 달라진 부분, 틀리기 시작한 부분을 분석
        위 모든걸 확인해도 특별히 잘못된 부분이 없는데 이상하다 .. 했음
        계속 살펴보고 idx 나오는 거 프린트하다보니 삭제를 9번 index를 해야하는데 0으로 입력했단 걸 알게됨
            특정 영역에 프린트 찍었는데 전혀 그 부분이 동작하지 않는걸 보고 깨달음
2151 정답
피드백
     - 잘한점
        함수화를 잘한 것 같다 
            같은 함수를 여러번 사용 했고, 함수화 덕분에 코드 길이가 훨씬 짧아짐
        조금 비효율적인 로직(행 2개 삭제 시)도 있지만,
         그 로직의 효율을 높이기 위해 구현 복잡도가 올라가서실수할 가능성이 높아진다고 판단,
         시간/메모리가 충분하므로 최대한 실수를 덜 할 수 있는 방식으로 채택해 구현했다
            
     - 못한점
        이 문제를 처음 풀었을 때 문제를 제대로 안 읽고 내 멋대로 해석해서 문제 난이도를 화아ㅏ악 올렸었다.
            그 당시에 한번에 풀지 못한 요인..
            문제는 글자 있는 그대로 받아들일 것 멋대로 해석하지말 것


==================문풀 메모 =======================
10*10

green arr[4:][:4]
blue arr[:4][4:]

1.
한 줄이 다 차면 그 줄 사라지고 위에서 사라진 개수만큼 당겨옴 (점수 + 줄 수만큼)
초록 : 같은 행의 모든 열[:4]
파랑 : 같은 열의 모든 행[:4]

2. 한줄 다 찬 행/열 모두 점수 획득한 후에 처리
블록 다 내리고 연한 부분에 블록이 있는지 확인하기
있으면 있는 만큼 아래 행 / 열 삭제 => 아래 / 오른쪽으로 이동




"""
#한칸짜리일 때 쌓일 idx 찾는 함수
def find_idx(is_row, r, c):
    #r,c 빨간색에 놓인 위치
    #is_row True이면 초록
    if is_row:
        for i in range(6, 10):
            if arr[i][c]==0:
                continue
            return i-1
        return 9
    # False이면 파랑
    else:
        for i in range(6, 10):
            if arr[r][i]==0:
                continue
            return i-1
        return 9
def check_line(is_row, k):
    if is_row:
        for i in range(4):
           if arr[k][i] == 0:
               return False
    else:
        for i in range(4):
            if arr[i][k] == 0:
                return False
    return True

def push(is_row, idx):
    if is_row:
        arr[idx][:4] = [0]*4
        for i in range(idx, 4, -1):
            arr[i][:4] = arr[i-1][:4]
        arr[4][:4] = [0]*4
    else:
        for i in range(4):
            arr[i][idx] = 0
        for j in range(idx, 4, -1):
            for i in range(4):
                arr[i][j] = arr[i][j-1]
        for i in range(4):
            arr[i][4] = 0
#input
N = int(input())
score = 0
arr = [[0]*10 for _ in range(10)]
for i in range(N):
    # 블록 내리기 구현..
    # 파랑은 제일 오른쪽 열부터 해당 행의 값을 보며 빈칸이 나올 때까지 index찾기
    # 세로 두개짜리는 두 행을 모두 보고 그 중 min을 골라 그 열에 표시
    # 가로 두개짜리는 그냥 찾고 그 index랑 index-1에 체크
    # 초록은 제일 아래 행부터 해당 열의 값을 보며 빈칸이 처음으로 나오는 index찾기
    # 가로 두개 짜리는 두 열을 보고 그 중 min을 골라 그 행에
    # 세로 두개 짜리는 그냥 찾고 그거랑 그거보다 한칸 위(idx-1)에 체크

    t, x, y = map(int, input().split())
    r_idx = find_idx(1, x, y)
    c_idx = find_idx(0, x, y)

    #한칸
    if t == 1:
        arr[r_idx][y] = 1 #초록색에 내리기
        arr[x][c_idx] = 1 #파란색에 내리기
    # 1*2
    elif t==2:
        # r_idx1 = find_idx(0, x, y)
        r_idx2 = find_idx(1, x, y+1)
        r_idx = min(r_idx, r_idx2)
        #초록색에 내리기 (가로로 2개)
        arr[r_idx][y] = 1
        arr[r_idx][y+1] = 1

        #파란색에 내리기
        arr[x][c_idx] = 1
        arr[x][c_idx-1] = 1
        if check_line(0,c_idx-1):
            #
            push(0, c_idx-1)
            score+=1


    #2*1
    else:
        c_idx2 = find_idx(0, x+1, y)
        # print("x : ", x)
        # print("2*1일 때 c_idx : ", c_idx)
        # print("2*1일 때 c_idx2 : ", c_idx2)

        c_idx = min(c_idx2, c_idx)

        arr[r_idx][y] = 1
        arr[r_idx-1][y] = 1
        arr[x][c_idx] = 1
        arr[x+1][c_idx] = 1

        if check_line(1, r_idx-1):
            #해당 줄 아래로 밀기
            push(1, r_idx-1)
            score+=1
    #위 세개 공통 로직
    # 내리고 나서 내린 곳의 초록(행) 파랑(열) 4개 다 찼나 체크
    if check_line(1, r_idx):
        # 내리기
        push(1, r_idx)

        # 점수더하기
        score+=1
    if check_line(0, c_idx):
        # 오른쪽으로 밀기
        push(0, c_idx)
        # for j in range(c_idx, 0, -1):
        #     for i in range(4):
        #         arr[i][j] = arr[i][j-1]
        # 점수더하기
        score+=1

    # print("=========================")
    # for i in range(10):
    #     print(arr[i])
    #
    # print("========================")
    #다 내리고 점수 얻고 나서 연한칸 확인
    #초록색
    cnt_r = 0
    for i in range(4, 6):
        if 1 in arr[i][0:4]:
            cnt_r+= 1

    for k in range(cnt_r):
        push(1, 9)

    cnt_c = 0
    for i in range(4, 6):
        for j in range(4):
            if arr[j][i] == 1:
                cnt_c += 1
                break
    # print("cnt_c : " ,cnt_c)
    for k in range(cnt_c):
        push(0, 9)


# for i in range(10):
#     print(arr[i])
#
# print()
answer = 0
for i in range(4, 10):
    for j in range(4):
        if arr[i][j] == 1:
            answer += 1
        if arr[j][i] == 1:
            answer +=1

print(score)
print(answer)