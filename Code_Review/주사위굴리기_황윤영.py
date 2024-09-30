"""
1차
풀이 시간 : 2시간 3분
시도 횟수 : 2회
2차
풀이 시간 : 29분
실행 시간 : 130ms
시도 횟수 : 1회
메모리 : 25mb

- 실수 모음
    - index 실수
    - 오타 ( 방향 배열 변환하는거 )
    - 문제조건 놓침


"""
"""
========================== 2차 코드 리뷰 ===================================
1405 문제 읽기 시작 + 주석 정리 
1413 설계
    주사위 설계 서툰 편인 것 같아서 꼼꼼하게 생각하려고 노력함

1423 구현할 영역 정리 + 구현
1432 구현 완료 디버깅 
    - print 디버깅 -> 엥 도착 위치가 왜 음수지 !!! 방향 벡터 인덱스 변환 배열 오타 발견
    
정답 


"""
"""
Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영 : 생각 딱히 안나네 대신 주사위 안변하는거 주의
5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리
7. 구현
8.테스트케이스 단계별 디버깅 확인
9. 예외될 상황 테스트케이스 만들어서 확인
10. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!


Debugging CheckPoint
- N, M / 행 열 index 오타 실수 점검
- max, min 구할 때 초기값 체크
- 인덱스 디테일 확인( dfs 종료 level이나 범위 경계값)
- 배열 사용 목적 확인 후 배열 변수 실수 확인
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
0부터 9까지의 임의의 숫자가 그려진 n * m 격자판 위 한 면이 1 * 1 크기인 정육면체가 놓여져 잇음

격자판에서 정육면체를 굴리려합니다.
정육면체는 격자판 밖으로 이동할 수 없습니다
바깥으로 이동시키려고 하는 시도가 있을 때, 해당 시도를 무시하며 출력도 하지 않습니다.


처음 정육면체의 각 면에는 0이 쓰여져 있다
바닥에 있는 칸의 숫자에 따라 해당 칸과 정육면체의 숫자가 변하게 된다

칸에 쓰여져 있는 수가 0이면, 주사위의 바닥면에 쓰여져있는 수가 칸에 복사된다
이때 정육면체의 숫자는 변하지 않습니다

칸에 쓰여져 있는 수가 0이 아니면 칸에 쓰여져있는 수가 정육면체 바닥면으로 복사된다
해당 칸의 수는 0이 된다


각각 굴리기 시행 이후에 정육면체 상단 면에 있는 숫자를 출력


방향 
0  동쪽
1  서쪽
2 북쪽
3 남쪽 
"""

#oob
def oob(i, j):
    return i<0 or j<0 or i>=N or j>=M

def change_dice(d):
    global top, bottom
    tmp = top
    top = dice[(d+2)%4]
    dice[(d+2)%4] = bottom
    bottom = dice[d]
    dice[d] = tmp


#입력
N, M, r, c, K = map(int, input().split())
# 주사위 이동 방향 idx 변경 배열 필요
change_dir = (None, 1, 3, 0, 2) #동서북남을 북동서남으로 바꿔줌
arr = [list(map(int, input().split())) for _ in range(N)]
move_lst = list(map(int, input().split()))
top, bottom = 0, 0
dice = [0, 0, 0, 0] #초기 북동남서 주사위 값
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)
#명령에 따라 주사위 변경
for k in move_lst:
    d = change_dir[k]
    di, dj = DIR[d]
    nr, nc = r+ di, c+dj
    # print(r, c, "에서 ")
    # print(di, dj, "방향으로 ")
    # print(nr, nc, "여기로 이동")
    # print("============================")
    if oob(nr, nc): continue

    r, c = nr, nc
    change_dice(d)
    if arr[r][c] == 0:
        arr[r][c] = bottom
    else:
        bottom = arr[r][c]
        arr[r][c] = 0
    print(top)


#oob면 continue
# 바닥 숫자 있을 때만 복사 후 0 만들기


"""

========================== 1차 코드 리뷰 ===================================
1523 문제이해 완료 및 구상시작
1530 아이디어 안떠오름. 다음 문제부터 ;;
16?? 다시 문제 돌아옴. 주사위 굴리는 것 구현 방법 고민,,
1642 주사위 굴리기 구현 방식 생각남
1713 주사위 구현했으나 top bottom표기 숫자와 방향 숫자 겹쳐서 결과 잘못나옴 디버깅함(1번테케 안맞음,, 다시) dic 오타였음
        next에 i-1을 넣고 next를 함수 매개변수로 활용한 것이 원인,, index에 1을 뺄 것인지 말것인지 잘 설계할것!
1725 주사위 수 변하지 않는다는 문제조건 놓친 것 발견 ,,,
1726 백준도 제출하자 ..

=======================================
주사위 굴리기 어떻게 표현?
주사위 인덱스별로 top, bottom / 동서남북 기억
주사위 굴릴 때

이동방향  || bottom   top   동       서     남       북
동       || 서        동   bottom   top    남       북
서       || 동        서   top     bottom  남       북
남       || 북        남   동       서     bottom    up
북       || 남        북   동       서     top       bottom

이동방향에 따라 기존값이 위와 같이 변화
동서 북남 12 34
bottom 0 top 5로 표기하자
"""

def change_dice(l):
    #dice에서 현재 bottom인 곳을 dictionary에서 반대방향 뽑아서 바꾸기
    #top인 곳을 현재 방향으로 바꾸기
    #같은 방향인 곳을 bottom으로 바꾸기
    #반대 방향인 곳을 top으로 바꾸기
    opp = dic[l]

    ans_b = -1
    ans_t = -1
    for j in range(6):
        if dice_dir[j]==l:
            dice_dir[j] = 0
            ans_b = j
        elif dice_dir[j]==opp:
            dice_dir[j]=5
            ans_t = j
        elif dice_dir[j]==0:
            dice_dir[j]=opp
        elif dice_dir[j]==5:
            dice_dir[j]=l
    return ans_b, ans_t
dic = {1:2, 2:1, 3:4, 4:3} #동과 서 / 북과 남

dice = [0]*6
dice_dir = [i for i in range(6)]

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = list(map(int, input().split()))
dir = (0, 1), (0, -1), (-1, 0), (1, 0) #동서북남 순
t = 5
for i in lst:
    next = i-1

    #방향
    d = dir[next]
    nr = x+d[0]
    nc = y+d[1]
    #벗어나면 이동 x
    if nr<0 or nc<0 or nr>=n or nc>=m:
        continue
    x = nr
    y = nc
    #아니라면 해당 방향대로 주사위 바닥을 옮겨보자
    b, t= change_dice(i)
    #b는 바닥의 index
    if arr[x][y]==0:
        arr[x][y] = dice[b]
    else:
        dice[b] = arr[x][y]
        arr[x][y] = 0

    print(dice[t])
