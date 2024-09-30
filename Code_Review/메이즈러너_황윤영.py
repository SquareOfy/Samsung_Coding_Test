"""
풀이시간 : 3시간

초기 제출 ㅠ
실행시간 : 4982ms
메모리 : 45 mb

1차 리팩토링 : 기존 완탐 방식을 이용하되, 탈출구를 중심으로 돌았음
실행시간 4565ms
메모리 : 44mb

2차 리팩토링 : 정사각형 완탐방식 아닌 조건분기공식 활용
실행시간 4741ms
메모리 45mb

3차 리팩토링 : bfs 버림 눈물난다 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
실행시간 : 186ms
메모리 25mb


코드리뷰


미치게 힘들어서 미루고 싶지만 이 죽을것같은 고통을 기록해야해 ...

1300 문제 읽기 시작
1308 정독 완료하고 정사각형 부분 만만치 않겠다 생각하며 주석 정리
1311 손설계 시작
    - bfs로 접근해야겠다고 생각했었다
        이유는 참가자가 움직이는 조건의 최단거리 조건,, 상하좌우로 움직임 등등 때문
        결론적으로 굉장히 잘못된 접근이었다

    - 정사각형 구상도 단단히 잘못됐었음
        정사각형으로부터 가장 가까이 있는 사람을 찾으려고 했는데
        그게 최소 정사각형을 보장하진 않아서 추가 조치가 필요했고
        무엇보다 bfs로 하기엔 비효율적인 작업. ;;;
0131 설계 후 구현시작
0150 디버깅 시작
    - 에러 나는 것 오타 일단 수정
    - 답 안맞길래 단계별로 print 디버깅 세팅
    - bfs로 이동할 위치 잘못 찾아가는 문제 발견
        문제 정독이 부족한건지,, 그냥 설계를 잘못한건지
        일단 arr[du][dv]>0 일 땐 방문 안하는걸 처리하려고 했다.. 최단거리로 가야하는데.
        그랬다보니 최단거리가 매번 달라져서 min_dist 라는 장치를 두게 됐고, visited 도 rank로 기록하며
        여러번 rank같으면 여러번 방문하게 하는 추가 조치 취함

        아래는 문제 정보 미흡이 확실..
        그 부분 수정한 후엔 0 아닌 곳 지났을 때 flag를 queue 에 들고 다니면서 길막힌 곳으로 올 때는
        안 움직이게 처리를 했는데, 사실 가는 길이 막혀있어도 내가 갈 딱 그 칸만 0이 아니면 된다는 사실을
        나중에야 깨달음

    - 회전 문제
        회전한 배열 내의 좌표를 정사각형 내에서 어떻게 변화하는지를 봐야하는데,
        n*n 배열 자체를 회전시켰을 때의 배열을 반환해서 문제 발생
        함수에 dist변수 추가해서 그 배열 내의 좌표를 반환하도록 했고,
        이걸 sr, sc값과 조합하여 전체 배열에서의 적절한 좌표를 찾도록 했다.
        ===================여기까지가 1415============================


    - 탈출한 사람 처리
        -1 처리 안해서 문제 생긴거 잡음
    - 이동할 칸 계산 문제 ...
        도착하긴 하는데, 이동할건지 말건지 조건 처리가 문제였다
        상하 우선 / 좌우 우선이란 조건
        가야할 곳을 안가는 문제 발생한 것 발견하고 디버거로 찾아보고 난리브루스치다가
        내 앞의 한칸만 0이 아니면 된다는 것 깨닫고 수정
    - 회전 문제 : 자꾸 인덱스 에러 나고 잘못 찾아짐
        조건 분기문으로 sr, sc 찾으려했는데 뭔가 머리가 꽉 막히고 안돌아갔다.
        자꾸 인덱스 에러 나서 막판에 그냥 시간 될 것 같으니까 완탐해버리자 생각함
        => 비효율적....이지만.............확실하긴 했다
    - 회전 완탐으로 고치고 나니 아직 bfs 안고쳐진 것 알게 됨 ..
        visited 체크 rank 비교로 바꾸고 초기값 수정함


피드백
    - 잘한 점
        없는 것 같은데 .........
        그래도..................
        진짜 말도 안되는 풀이었는데 .............
        꾸역꾸역 시간 max로 턱걸이로 .............풀어냈다 ..?

        정사각형 풀이 과감히 던져버림

        리팩토링 열심히 했다 ..
    - 못한 점
        문제 설계 자체를 잘못함 : 왤까 . 왜 항상 이럴까
            자꾸 bfs가 아닌 문제를 bfs로 접근한 전적이 많다
            최단거리라는 말만 보면 좀 사고가 닫히는 것 같기도 하다;
            기출 중에서도 이렇게 접근해서 시간 엄청 나왔던 문제 있었다 ..
            bfs로 구현하려는데 유독 조건이 너무 까다롭다? 의심하자. bfs맞는지 . 전적이 정말 많다

        시간복잡도 계산 똑바로 안하고 들어갔다
            대략적인 감으로 완탐해도 되겠다는 느낌은 들긴 했지만
            정말 큰 시간이 찍히길래 좀 놀라기도 했다 .......
            심지어 원인이 정사각형이 아니었다 %^>^5^$ㄸ bfs .. 아닌데 bfs 돌렸으니 ;

        꼭 이런 인덱스 가지고 계산하는 경우 실수도 많고 잘 구현 못하는듯 ;
            비슷한 문제 있으면 풀어봐야겠다 ㅠ ㅠ

        이후 1시간 정말 의미없는 디버깅 했던 것 같다.
        다시 영상을 되돌아보니 이문제에서 풀이를 버리고 새로운 설계를 해봐야했을 타이밍은
        1시간 반이 흘렀을 때였을 것 같다. 이유.
        1시간은 내가 이 정도로 버릴 생각을 절대 못할 것 같고, 그럴듯한 결과가 나오기도 했다..
        1시간 반쯤 bfs로 엄청 고생했기 때문 ㅠ


=> 리팩토링을 결심 . 저 시간을 보고 리팩토링을 안하면 난 사람이 아니야
=> 리팩토링하면서 정사각형 부분 고쳤는데, (완탐 -> 조건분기 공식) 그래도 4000대가 나와서
    bfs가 문제군 했고. 문제 다시 보고 bfs가 아니라면 ,, 하고 보니 이제야 보이는 솔루션 ;




"""
def control_idx(i):
    return int(i)-1


def oob(i, j):
    return i<0 or j<0 or i>=N or j>=N

#최단길이의 정사각형을 만들 수 있는 사람 후보군으로 sr, sc를 찾는 함수
def find_sr_sc():

    result_r, result_c = N, N

    #사람 후보 중에서
    for pr, pc in p_lst:

        #행의 차이가 한변의 길이와 같다면 그냥 작은 행이 시작칸의 행
        if abs(er-pr)==dist:
            sr = min(er, pr)
        else:
            #다르다면 둘다 포함해야 하므로 둘 중 아래쪽에 있는 행에서 dist를 뺀 값을 행값으로
            #단 0보다 작아지면 0으로 하기
            if max(er, pr)-dist+1>=0:
                sr = max(er, pr)-dist+1
            else:
                sr = 0
        #행 로직과 동일
        if abs(ec-pc)==dist:
            sc = min(ec, pc)
        else:
            if max(ec, pc)-dist+1>=0:
                sc = max(ec, pc)-dist+1
            else:
                sc = 0
        #행 우선 열 우선 ..
        if sr<result_r:
            result_r=sr
            result_c=sc
        elif sr==result_r and sc<result_c:
            result_r = sr
            result_c = sc
    return result_r, result_c

#길이가 dist인 배열 내에서 회전했을 때 좌표
def rotate(r, c, dist):
    return c, dist-1-r


# 미로는 N×N 크기의 격자  좌상단은 (1,1)
# 벽
    # 참가자가 이동할 수 없는 칸입니다.
    # 1이상 9이하의 내구도를 갖고 있습니다.
    # 회전할 때, 내구도가 1씩 깎입니다.
    # 내구도가 0이 되면, 빈 칸으로 변경됩니다.
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
people = [list(map(control_idx, input().split())) for _ in range(M)]
er, ec = map(control_idx, input().split())
cnt = M
answer = 0

# K초 동안 위의 과정을 계속 반복됩니다.
for k in range(1, K+1):

    # 1. 움직임
    # 1초마다 모든 참가자는 한 칸씩 움직임
    # 모든 참가자는 동시에 움직입니다.
    # 상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동할 수 있습니다.
    # 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 합니다.
    # 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시합니다.
    # 참가가가 움직일 수 없는 상황이라면, 움직이지 않습니다.
    # 한 칸에 2명 이상의 참가자가 있을 수 있습니다.
    for i in range(M):
        r, c = people[i]
        if r==-1: continue
        nr, nc = r, c
        if er<r and arr[r-1][c]==0:
            nr = r-1
        elif er>r and arr[r+1][c] == 0:
            nr = r+1
        elif ec<c and arr[r][c-1]==0:
            nc = c-1
        elif ec>c and arr[r][c+1]==0:
            nc = c+1
        if nr==r and nc==c:
            continue
        answer+=1
        if nr == er and nc == ec:
            cnt-=1
            people[i] = [-1, -1]
        else:
            people[i] = [nr, nc]
    # 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝납니다.
    #움직이고 나서 사람 수 체크 후 break
    if cnt == 0:
        break

    # 2. 미로회전
        # 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형
        # 가장 작은 크기를 갖는 정사각형이 2개 이상이라면,
        # 좌상단 r 좌표가 작은 것이 우선되고, 그래도 같으면 c 좌표가 작은 것이 우선됩니다.
        # 선택된 정사각형은 시계방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깎입니다.

    dist = 2*N
    p_lst = []
    for m in range(M):
        r, c = people[m]
        if r==-1: continue
        tmp = max(abs(er-r), abs(ec-c))+1 #이 사람과 정사각형을 만들 때 한변의 길이 사람이 M명이니까 그 중 최소인 걸 찾아야하고
        if tmp<dist: #최소 갱신!!
            p_lst = [(r, c)]
            dist = tmp
        elif tmp==dist:
            p_lst.append((r, c))

    sr, sc = find_sr_sc()


    #정사각형 회전
    tmp = [[] for _ in range(dist)]
    for i in range(dist):
        tmp[i] = arr[sr+i][sc:sc+dist]
    for i in range(dist):
        for j in range(dist):
            if tmp[i][j]>0:
                tmp[i][j] -=1

    tmp = list(map(list, zip(*tmp[::-1])))
    for i in range(dist):
        arr[sr+i][sc:sc+dist] = tmp[i][:]


    er_tmp = er-sr
    ec_tmp = ec-sc
    er_tmp, ec_tmp = rotate(er_tmp, ec_tmp, dist)
    er, ec = er_tmp+sr, ec_tmp+sc
    #출구좌표 회전


    #저 안에 들어있는 사람 회전
    for i in range(M):
        r, c = people[i]
        if r==-1: continue
        if r in range(sr, sr+dist) and c in range(sc, sc+dist):
            tmp_r, tmp_c = rotate(r-sr, c-sc, dist)
            r, c = tmp_r+sr, tmp_c+sc
            people[i] = [r, c]

print(answer)
print(er+1, ec+1)


# 아래는 초기에 구현한 bfs ... 그 외 dist_bfs는 버려버림
##########################################################################3
# def bfs(r, c):
#     q = deque([(r, c, 1, -1, -1)])
#     visited = [[N*N]*N for _ in range(N)]
#     visited[r][c] = 1
#     min_dist = N*N+1
#     while q:
#         cr, cc, rank, one_r, one_c = q.popleft()
#         if cr==er and cc==ec:
#             if rank <= min_dist:
#                 min_dist = rank
#                 if arr[one_r][one_c]==0 :
#                     return one_r, one_c
#             continue
#         for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
#             du = cr+di
#             dv = cc+dj
#             if oob(du, dv) or visited[du][dv] < rank:
#                 continue
#
#             visited[du][dv] = rank
#
#             if rank==1:
#                 q.append((du, dv, rank+1, du, dv))
#             else:
#                 q.append((du, dv, rank+1, one_r, one_c))
#
#     return -1, -1