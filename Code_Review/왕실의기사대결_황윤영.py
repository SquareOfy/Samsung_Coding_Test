"""
1차
풀이 시간 : 3시간 31분
시도 횟수 : 무제한
실행 시간 : 141ms
메모리 : 25mb

2차
풀이 시간 : 1시간 3분
시도 횟수 : 3회
실행 시간 : 157ms
메모리 : 25mb

- 실수 모음
    - 변수명 실수 : 평소 N으로 쓰던 배열 크기가 L로 들어옴
    - 함수에 return 누락. 더 돌아서 에러 생김
    - 로직 구멍.. move할 때 자기 자신일 때만 지우기!!
    - 설계 미흡(1차)

"""
"""
============== 2차 코드 리뷰 ======================
고생고생 했던 문제. 정신 똑바로 차리고 풀자!! 고 생각하고 시작했음
1442 문제 읽기+주석정리 + 설계
1507 구현시작
    설계 꼼꼼하게 한 편이라 구현이 쉬웠음
    특히 기사 방패 끝점 인덱스를 1차에서 많이 헷갈려해서 틀렸는데 이걸 확실히 설계하고 감
1521 구현완 디버깅 시작 
    전부 다 밀지를 못하길래 is_possible 함수 확인 . return True누락 발견
    
    3을 안밀길래 왜 안밀지 보니, 다음 칸도 봐야하는데 return 하는 실수를 함. 
    if 로 체크하고 false면 return하도록 수정
    
    제출했는데 런타임 에러
    
===============잠깐 쉬고. . 
1545 돌아와서 다시 디버깅
    런타임 에러 원인을 찾으려고 기사 정보 출력해봤는데 정보가 입력과 다르다
    한번밖에 안가는데? 여러번 미는구나 싶어서 왜지 .. 하고 push_lst만드는 곳 살펴보다가
    중복으로 밀리는 것 확인. 제거 
    
    제출했는데 틀림
    관련 작은 테케 가져와서 전반적으로 출력해보다가 죽었는데 damage가 0이 아닌 것 확인
    damage받을 때 기사 죽으면 return 안한 것 발견해서 수정 후 정답
    
총평
    printa 함수 템플릿이 뭔가 확고해져서 프린트 디버깅이 확실히 쉬워진 걸 느낌
    당황해도 프린트디버깅 예쁘게 할 것. 그래야 찾기 쉬운 것 같다.
    설계를 꼼꼼히 하니, 로직상 틀린 부분이 적어서 그 외의 자잘한 실수들을 안하진 않았지만
    찾기는 쉬웠다. 


"""
"""

체스판의 왼쪽 상단은 (1,1)로 시작
d는 0, 1, 2, 3 중에 하나이며 각각 위쪽, 오른쪽, 아래쪽, 왼쪽 방향을 의미

각 기사의 초기위치는 (r,c)
(r,c)를 좌측 상단으로 하며 h(높이)×w(너비) 크기의 직사각형 형태
각 기사의 체력은 k

(1) 기사 이동
    상하좌우 중 하나로 한 칸 이동할 수 있습니다

    이때 만약 이동하려는 위치에 다른 기사가 있다면
    그 기사도 함께 연쇄적으로 한 칸 밀려나게 됩니다.
    => 재귀 함수 호출

    만약 기사가 이동하려는 방향의 끝에 벽이 있다면
    모든 기사는 이동할 수 없게 됩니다
    => return False

    체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 됩니다.

(2) 대결 대미지
    밀려난 기사들은 피해를 입게 됩니다.
    이때 각 기사들은 해당 기사가 이동한 곳에서
    w×h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 됩니다.

    각 기사마다 피해를 받은 만큼 체력이 깎이게 되며,
    현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다.
    명령을 받은 기사는 피해를 입지 않으며,
    기사들은 모두 밀린 이후에 대미지를 입게 됩니다.

Q 개의 명령이 진행된 이후, 생존한 기사들이 총 받은 대미지의 합
"""


# 기사 밀 수 있는지 체크하는 함수
def is_possible_push(num, d):
    r, c, h, w = gisa_lst[num]

    di, dj = DIR[d]
    if di:
        du = r + h if di > 0 else r - 1
        for dv in range(c, c + w):
            if oob(du, dv):
                return False
            if info_arr[du][dv] == 2:
                return False
            if gisa_arr[du][dv] != 0:
                if gisa_arr[du][dv] not in push_lst:
                    push_lst.append(gisa_arr[du][dv])
                if not is_possible_push(gisa_arr[du][dv], d):
                    return False
    elif dj:
        dv = c + w if dj > 0 else c - 1
        for du in range(r, r + h):
            if oob(du, dv): return False
            if info_arr[du][dv] == 2: return False
            if gisa_arr[du][dv] != 0:
                if gisa_arr[du][dv] not in push_lst:
                    push_lst.append(gisa_arr[du][dv])
                if not is_possible_push(gisa_arr[du][dv], d):
                    return False
    return True

# oob
def oob(i, j):
    return i < 0 or j < 0 or i >= L or j >= L


# 기사 옮기는 함수
def move_gisa(num, d):
    r, c, h, w = gisa_lst[num]
    di, dj = DIR[d]
    if di:
        remove_r = r if di > 0 else r + h - 1
        append_r = r + h if di > 0 else r - 1

        for dv in range(c, c + w):
            if gisa_arr[remove_r][dv] == num:
                gisa_arr[remove_r][dv] = 0
            gisa_arr[append_r][dv] = num
    elif dj:
        remove_c = c if dj > 0 else c + w - 1
        append_c = c + w if dj > 0 else c - 1
        # print(append_c)
        for du in range(r, r + h):
            if gisa_arr[du][remove_c] == num:
                gisa_arr[du][remove_c] = 0
            gisa_arr[du][append_c] = num
    gisa_lst[num] = (r + di, c + dj, h, w)

# damage 처리 함수
def get_damage(num):
    r, c, h, w = gisa_lst[num]
    for i in range(r, r + h):
        for j in range(c, c + w):
            if info_arr[i][j] == 1:
                damage_lst[num] += 1
                power_lst[num] -= 1
                if power_lst[num] == 0:
                    die_gisa(num)
                    return #누락...
def die_gisa(num):
    r, c, h, w = gisa_lst[num]
    for i in range(r, r + h):
        for j in range(c, c + w):
            gisa_arr[i][j] = 0

    gisa_lst[num] = -1
    damage_lst[num] = 0

def printa(string, arr):
    print(f"============={string}================")
    for t in range(len(arr)):
        print(arr[t])
    print("=======================================")
    print()

# 입력 및 배열 준비
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

L, N, Q = map(int, input().split())
info_arr = [list(map(int, input().split())) for _ in range(L)]
gisa_arr = [[0] * L for _ in range(L)]
gisa_lst = [-1]
damage_lst = [0] * (N + 1)
power_lst = [0] * (N + 1)

for n in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    gisa_lst.append((r, c, h, w))
    power_lst[n] = k

    for i in range(r, r + h):
        for j in range(c, c + w):
            gisa_arr[i][j] = n
# printa("초기 기사 상태", gisa_arr)
for q in range(Q):
    num, d = map(int, input().split())
    # print("==================", num, d, "===================")
    if gisa_lst[num] == -1: continue
    push_lst = []
    if not is_possible_push(num, d):
        continue

    # 기사들 이동
    for pn in push_lst:
        move_gisa(pn, d)
    move_gisa(num, d)  # 명령 받은 기사 이동
    # printa("기사 이동했음", gisa_arr)

    for pn in push_lst:
        get_damage(pn)

    # printa("데미지 먹인 후 ", gisa_arr)
    # print(power_lst)
    # print(damage_lst)
    # print(gisa_lst)


print(sum(damage_lst))
"""
======================1차 코드 리뷰=============================
풀이 시간 : 3시간 31분
실행 시간 : 141ms
메모리 : 25mb


*************모의연습 시간에 실패 후 야자시간에 재시도함*********


1. 모의연습 실패요인 분석 : 문제 잘못 이해하고 설계 잘못한 데다가 리셋시도 조차 안함
    1) 문제 잘못 이해 후 설계 실패
        기사의 방패는 직사각형 모양인데 딱 한칸만 밀 생각으로 설계했음
    2) 설계 실패 후 기존 코드 활용하는 방향으로 진행함
        새로 코드 엎고 새로 설계했어야했다. 기존에 설계 잘못한 데에서 다시 개선한 것 또한 설계 잘못됐음
        아예 기존 코드로 개선이 불가능하지 않다고 해서 기존 코드로 이어나간 것이 가장 큰 실패 요인
        벽이거나 oob일 때 밀기 불가
        기사를 또 만나면 그 기사의 모든 방패 영역을 또 밀 수 있는지 체크해야한다는 점 간과

    3) 위 두 요인으로 인해 코드가 굉장히 지저분해져서 디버깅이 어려워졌는데 리셋 안함...
        (밀 기사 없이 한칸만 이동할 때, 밀 기사 있을 때, 못 밀 때 다 다른 조건분기 써야해서 놓치기 쉬웠음)
        왜그랬지.
        뭔가 될 것 같다 틀린 것 같지 않다는 느낌이 제일 위험하다. 자꾸 내 코드에 대한 집착을 만들어ㅠ


2. 2차 시도 코드 리뷰

    1950 문제읽기 시작
        한번 엎어졌던 문제라 문제가 비교적 잘 읽혔음
        문제 주석 복사
    1954 설계 시작
        설계하면서 첫 시도 때 뭘 잘못 이해했는지 깨달음
        넓게 퍼지듯이 기사를 밀 때 또 기사를 만나면 그 기사의 전체 영역이 모두 밀리는지 확인해야함을 깨달ㅇ므
        => 기사를 밀다가 기사를 만나면 그 기사도 또 똑같은 과정으로 민다는 생각이 들어 재귀 방법이 떠오름

    2021 구현시작
        상하좌우에 따라 약간 하드 코딩스러운 부분이 있어 실수 안하려고 주의했음
        예지님이 알려주신 ALT + J 단축키 매우 잘 써먹는 중
    2119 제출 후 오답 디버깅 시작
        - 전체 코드 로직 문제와 함께 점검하며 틀린 곳 없는지 확인
         - 가장 로직이 복잡한 CHECK 함수 의심
         - print 디버깅으로 예제 확인 (적당한ㅇ ㅖ제가 없었다 토론방에 ㅠ)
         - 그러다 자꾸 멈춰야하는데 함수가 여러번 호출되는 이상한 현상 발견 ;
         - 로직 정상적으로 동작은 하는 것 같은데 함수 두번 호출되는게 이상;
         - while 문이 불필요한걸 확인. 어차피 한칸이잖아??
    1040 고쳐서 또틀림
        - 도무지 어딘지 모르겠는데 토론방 테케도 다 맞음
        - 어쩔 수 없이 기존 코드 뜯어보기 + 테케 출력해서 진짜 100짜리 테케 보기 함
        - 기사 옮길 때 구멍 발견
        - 그걸 초점으로 다시 코드 뜯어봄
        - 기사를 넣는 순서가 재귀로 함수 끝까지 타고 들어가서 마지막 기사를 만날 때인데
            처음에 for문으로 훑어서 넣는다 생각해서 push_lst를 거꾸로 돌렸고 그래서 발생하는 문제
        - lst 순서 바꿔서 조정
        - move할 때 본인인지 확인하는 로직 추가
    1121 정답

피드백
    - 문제 복사해놓고 꼼꼼히 보진 않고 그냥 형식적으로만 하는 것 같은 느낌이 든다.
        => 개선 .
            위에 복사해놓고 설계할 때 참고하되, 코드 사이사이에 지저분하게 두진 말자
            대신 코드 구현 완료 후 하나씩 가져다 비교하며 빠뜨린 것 없는지 확인하기
    - 코드에 대한 집착 버리기 지저분하면 리셋하기. 1시간 ~ 1시간 10분 쯤에 한번 판단.
        계속 디버깅 할거면 딱 20분 더 해보고 1시간 30분에 다시 판단하고 아니면 리셋 꼭 하자 .
        리셋하면서 설계를 다시 생각해보면 문제에 대한 이해가 올라가서 빈틈이 다시 보이더라 ㅠㅠ



"""

L, N, Q = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(L)]
gisa = [[0] * L for _ in range(L)]
gisa_info = [-1]
hp = [0] * (N + 1)
damage_lst = [0] * (N + 1)
DIR = (-1, 0), (0, 1), (1, 0), (0, -1)

for n in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    r -= 1
    c -= 1
    for i in range(h):
        for j in range(w):
            gisa[r + i][c + j] = n
    gisa_info.append([r, c, h, w])
    hp[n] = k


def is_possible_push(num, di, dj):
    r, c, h, w = gisa_info[num]
    if di:
        du = r + h if di > 0 else r - 1
        if du < 0 or du >= L:
            return False

        for j in range(c, c + w):
            if arr[du][j] == 2:
                return False
            if gisa[du][j] != 0:
                if not is_possible_push(gisa[du][j], di, dj):
                    return False
                if gisa[du][j] not in push_lst:
                    push_lst.append(gisa[du][j])
        return True
    else:
        dv = c + w if dj > 0 else c - 1
        if dv < 0 or dv >= L:
            return False
        for j in range(r, r + h):
            if arr[j][dv] == 2:
                return False
            if gisa[j][dv]:
                if not is_possible_push(gisa[j][dv], di, dj):
                    return False
                if gisa[j][dv] not in push_lst:
                    push_lst.append(gisa[j][dv])
        return True


def push(num, di, dj):
    r, c, h, w = gisa_info[num]
    gisa_info[num] = [r + di, c + dj, h, w]

    if di:
        delete_r = r if di > 0 else r + h - 1
        new_r = r + h if di > 0 else r - 1
        for j in range(c, c + w):
            if gisa[delete_r][j] == num:
                gisa[delete_r][j] = 0
            gisa[new_r][j] = num
    else:
        delete_c = c if dj > 0 else c + w - 1
        new_c = c + w if dj > 0 else c - 1

        for j in range(r, r + h):
            if gisa[j][delete_c]==num:
                gisa[j][delete_c] = 0
            gisa[j][new_c] = num


def kill(num):
    r, c, h, w = gisa_info[num]
    for i in range(r, r + h):
        for j in range(c, c + w):
            gisa[i][j] = 0
    damage_lst[num] = 0
    gisa_info[num] = -1


def get_damage(num):
    r, c, h, w = gisa_info[num]
    tmp = 0
    for i in range(r, r + h):
        for j in range(c, c + w):
            if arr[i][j] == 1:
                tmp += 1
    hp[num] -= tmp
    if hp[num] <= 0:
        kill(num)
    else:
        damage_lst[num] += tmp


for q in range(Q):

    q_i, d = map(int, input().split())

    if hp[q_i] <= 0: continue

    r, c, h, w = gisa_info[q_i]
    di, dj = DIR[d]
    push_lst = []

    is_possible = is_possible_push(q_i, di, dj)


    if not is_possible:
        continue

    for k in range(len(push_lst)):
        num = push_lst[k]
        push(num, di, dj)

    push(q_i, di, dj)

    for num in push_lst:
        get_damage(num)

print(sum(damage_lst))