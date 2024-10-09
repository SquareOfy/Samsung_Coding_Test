"""
1차
풀이 시간 : 1시간 25분
시도 횟수 : 6회
실행 시간 :292ms
메모리 :113092kb

2차
풀이 시간 : 3시간
시도 횟수 : 3회
실행 시간 :292ms
메모리 :113092kb
실행 시간 : 176 ms
메모리 : 113084 kb

- 실수 모음
    - 문제 잘못 읽기
    - 인덱스 범위 오류

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 ok
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
: 전에 풀었던 경험을 바탕으로 가운데 애들 먼저 칠해야겠다고 생각!
: 인덱스가 코드트리엔 없어서... 내가 네 꼭짓점 구해서 범위 구해야겠다고 생각함
5. 종이에 손설계 OK
6. 주석으로 구현할 영역 정리 : ok !
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : ok 했지만 굉장히 눈 똑바로 안뜨고 본듯
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!


"""

"""
========================= 2차 코드 리뷰 ========================

1606 문제 읽기 시작 + 주석 정리 

1613 설계
    - 일단 가운데 칸 먼저 채워야한다는 건 금방 생각함
    - 가운데 칸 채울 때는 문제에서 아래칸부터 방향 알려줘서
        그 방향 그대로 따라 구현해야지 생가갛ㅁ
    - 2,3,4, 5번 구역 어떻게 잡을지 백준이랑 달리 인덱스 안줘서 당황
    - 네 꼭짓점 좌표 잡아서 백준처럼 범위 만들어야겠다 생각
    
    - 인덱스가 헷갈려서 꽤 오래 설계함
1632 주석 정리 + 구현시작 
    - 마름모(?) 모양 사각형 잘 잡히는지 중간 테스트 함
1705 구현 완료 후 제출했으나 틀림
    - 1차로 마름모가 생기는 경우를 다 완탐하지 못할 가능성을 두고 프린트 디버깅
      너무 잘 한다 ...
    - 마름모는 잘 만드는데 나머지 네 구역 칠하는 과정에서 다른 구역을 침범하는 문제 발견
-----------------------------다른 일 생김-------------------------
1757 다시 디버깅 시작
    위에서 발견한 문제가 내가 세운 범위가 이상해서임을 깨달음
    분명 저런식으로 인덱스 잡는 것 맞는데 어떻게 해야할지 모르겠음 
    => 먼저 칠하고 그 위에 1을 덮을까 생각해서 수정했지만 애초에 인덱스가 안맞아서
    영역침범하므로 소용 없었음
    
    마름모에서 우측하단은 마름모 길이에서 우측하단, 좌측하단인 점을 생각하여 
    마름모의 가장자리에서 내리고 오른쪽으로 퍼뜨리는 방식 생각해서 구현함
1903까지 

2140 ~ 1006

    답 안나옴. 이유. 마름모 가장자리에서 퍼뜨린게 배열 전체를 덮어주지 않을 수 있음
    => 위에서 잡은 인덱스 범위를 추가 활용해서 마름모 가장자리로 채우지 못한 부분은
    저 인덱스 범위로 추가로 채우는 방식 활용
    
    마지막으로 채운 사이드가 마름모 꼭짓점 라인을 모두 먹는 문제 발생 
    마지막일 때만 마지막 점은 채우지 않는 조건 적용하여 해결
    
    population을 위 과정에서 더하면 자꾸 겹쳐지는 경우가 생겨서 
    맨 마지막에 다 채운 애로 새로 채움
    
    => 시간 효율은 없지만 우찌저찌 정답처리는 됨 (중간에 밥먹었음 ㅠ_ㅠ)

총평 

- 인덱스 찾기 너무너무 못한다.. 아직도 헷갈리고 모르겠다
이거 꼬오오오오오옥 다시 풀어보자 .
"""



"""
1이상 100이하의 숫자로만 이루어져 있는 n * n 크기의 격자 정보
격자의 숫자들은 지역별 인구수
다섯 개의 부족이 땅을 나눠가지기로 했습니다.
땅을 나누기 위해 기울어진 직사각형을 이용


기울어진 직사각형이란, 
격자내에 있는 한 지점으로부터 체스의 비숍처럼 대각선으로 움직이며 반시계 순회를 했을 때 지나왔던 지점들의 집합
반드시 아래에서 시작해서 1, 2, 3, 4번 방향순으로 순회
각 방향으로 최소 1번은 움직여야 합니다
이동하는 도중 격자 밖으로 넘어가서는 안됩니다.

1번 부족
기울어진 직사각형의 경계와 그 안에 있는 지역

2번 부족
기울어진 직사각형의 좌측 상단 경계의 윗부분에 해당하는 지역
위쪽 꼭짓점의 위에 있는 칸들은 모두 포함하지만 왼쪽 꼭짓점의 왼쪽에 있는 칸들은 포함하지 않습니다.

3번 부족
기울어진 직사각형의 우측 상단 경계의 윗부분에 해당하는 지역
오른쪽 꼭짓점의 오른쪽에 있는 칸들은 모두 포함하지만 윗쪽 꼭짓점의 위쪽에 있는 칸들은 포함하지 않습니다.

4번 부족
기울어진 직사각형의 좌측 하단 경계의 아랫부분에 해당하는 지역
왼쪽 꼭짓점의 왼쪽애 있는 칸들은 모두 포함하지만 아랫쪽 꼭짓점의 아래쪽에 있는 칸들은 포함하지 않습니다.

5번 부족
기울어진 직사각형의 우측 하단 경계의 아랫부분에 해당하는 지역
아랫쪽 꼭짓점의 아랫쪽에 있는 칸들은 모두 포함하지만 오른쪽 꼭짓점의 오른쪽에 있는 칸들은 포함하지 않습니다.


각 부족장이 관리하는 인구 수의 최댓값과 최솟값의 차이가 가장 작을 때의 값
"""

# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")
s = 0
for i in range(N):
    s += sum(arr[i])
# a, b for문으로 정하기 a : 1~N-2, b는 1~ N-1-a
# i, j 는 i는 위로 필요한 공간으로 범위 잡기 (a+b) ~ N
# j는 그냥 다 하고 continue로 거르기
for a in range(1, N):
    for b in range(1, N):
        for i in range(a + b, N):
            for j in range(N):
                if i - a - b < 0: continue
                if j + b >= N: continue
                if j - a < 0: continue
                check = [[0] * N for _ in range(N)]
                population = [0] * 5
                # 대각 체크
                r, c = i, j
                l = b
                line_lst = []  # 아래 위 위 아래
                dir_lst = ((1, 1), (-1, 1), (-1, -1), (1, -1))
                for di, dj in (-1, 1), (-1, -1), (1, -1), (1, 1):
                    lst = [(r, c)]
                    for k in range(l):
                        r += di
                        c += dj
                        check[r][c] = 1
                        lst.append((r, c))
                    l = b if l == a else a
                    line_lst.append(lst)


                for rr in range(i - a - b + 1, i):
                    flag = False
                    for cc in range(j - a, j + b):
                        if check[rr][cc] == 1 and not flag:
                            flag = True
                        elif check[rr][cc] == 0 and flag:
                            check[rr][cc] = 1
                        elif check[rr][cc] == 1 and flag:
                            break
                for k in range(4):
                    lines = line_lst[k]
                    di, dj = dir_lst[k]
                    for t in range(len(lines)):
                        rr, cc = lines[t]
                        dv = cc + dj
                        while 0 <= dv < N:
                            check[rr][dv] = k + 2
                            dv += dj
                        if k==3 and t==(len(lines)-1):
                            break
                        du = rr + di
                        while 0 <= du < N:
                            check[du][cc] = k + 2
                            du += di
                # 2,3,4,5 부족 체크
                for rr in range(N):
                    for cc in range(N):
                        if check[rr][cc]!=0:
                            continue

                        if rr in range(i-a) and cc in range(j+b-a+1):
                            check[rr][cc] = 4
                        elif rr in range(i-b+1) and cc in range(j+b-a+1, N):
                            check[rr][cc] = 3
                        elif rr in range(i-a, N) and cc in range(j):
                            check[rr][cc]= 5
                        else:
                            check[rr][cc] = 2
                for rr in range(N):
                    for cc in range(N):
                        k = check[rr][cc]
                        population[k - 1] += arr[rr][cc]
                answer = min(max(population) - min(population), answer)
print(answer)



"""
총 문제 풀이시간 :1시간 25분
실행시간 :292ms
메모리 :113092kb

0922 : 문제읽기 시작 ~ 구상
    - 문제 이해가 꽤 시간이 걸렸다
    - 5번 선거구 모양을 어떻게 구현하면 좋을지 함께 고민하는데, 바로 떠오르지 않아
      문제를 여러번 읽으며 5번 선거구 모양의 패턴을 찾으려고 노력함

0940 : 대략적인 구상 주석으로 정리 / 시간복잡도 계산 / 구현시작
    - 5구역 라인 구하는게 복잡해서 1~4구역 먼저 정하고 남은 자리에 5넣으려고 함(설계 실수)

0949 : 재설계 및 코드 수정(무한 디버깅의 화근이 여기서 발생)
    - 의도대로 구현 후 테케 적용해보니 말도 안되는 값 나와서 바로 구역에 어떤 선거구가 배정되었는지 프린트해서 확인
    - 5구역부터 지정하고 d1, d2를 중심으로 1~4를 지정해야함 알아챔
    - 문제 다시 읽으며 규칙 찾아 설계하여 구현함
    - 구현 후 테스트 해보니 또 답이 다름.
    - 위에서 사용한 구역마다 선거구 표기한 배열 출력해서 선거구 잘 들어갔는지 확인
        - 인덱스 실수 발견
        - 오타....
        - 문제 잘못 읽은 이슈 발견 => 인구수가 아닌 구역수 차이의 최솟값을 출력함
    - 수정 후 제출했으나 오답... 이후 숱한 오답
        - for문에 지정할 범위가 많은 문제라 범위에서 문제가 있었을 것 같아,
        - 그 부분을 중점으로 디버깅했음

        - 그러다 오타도 발견
        - 그래도 오답이 계속 나오길래 출력한 x, y, d1, d2 케이스를 찬찬히 살펴봄
        - x==0일 때가 안잡힌다는 걸 발견해서 범위 실수 수정 (1028~ )
            - 이 때 print로는 x==0일 때 안나오는 원인을 파악하기 어려워 디버거를 활용해봄(매우 유용했음)


        - 그래도 오답...
        - d1, d2가 어디서 안잡히는 걸까 싶어 n으로 바꾸고 문제에 적힌 그대로 조건 넣어 continue 처리

        - 그래도 오답.................
        - 출력되는 케이스들을 꼼꼼히 살펴봐도 선거구를 매우 잘!! 배치하고
        - 인구수도 알맞게 계산함.

        - 놓친 조건이 있지 않을까 하는 생각에 문제 찬찬히 다시 읽음

        - 그 때 들어오는 A[r][c]의 범위 100....
        - 그리고 초기에 인구수가 아닌 구역수로 설계했던 것이 떠오름....
        - answer의 초기값이 너무 작았던 문제 발견,,
            - 수정 후 정답처리




반성문 ...
- 실수 많이 줄였다고 자만하고 긴장 풀고 풀었나 너무 숱한 실수를 했다
- 최솟값 최댓값 물어보는 문제에서는 초기값 항상 주의해서 잡자. 의식하기
- 중간에 설계 뒤엎었을 땐 관련된 코드 부분 꼭 전체를 찬찬히 다 살펴서 빠짐없이 수정하자
- 문제.................왜 읽었는데 코드는 저렇게 짜나
- 소음에 익숙해지자.... 진짜 너무 힘들었음

그나마 칭찬할 점
- 디버깅 하는 도중, 디버깅할 대상 살피고 print는 다소 어려운 디버깅이라 판단해 디버거를 사용한 점.
    => 실제 시험에도 사용할 일이 충분히 있을 수 있으니 남은 한달동안 더 자주 사용해보며 익숙해지자
- 그 외 없음 .

"""

def is_possible():
    for i in range(5):
        if population[i] == 0:
            return False
    return True


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
population = [0] * 5

# x, y에 따라 d1, d2의 가능한 범위가 달라지므로
# x, y마다 d1, d2의 모든 경우를 고려해보자
# (20**2)**3

# d1, d2 고르고 나면 걔네로 1, 2, 3, 4 구역 정하고 5-(1,2,3,4)하기
answer = n * n * 100
popu = [[-1]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):

                if x+ d1 + d2 >= n :
                    continue

                if y-d1<0:
                    continue
                if y+d2>=n:
                    continue

                population = [0] * 5
                popu = [[-1] * n for _ in range(n)]


                # 이 조합으로 0, 1,  2, 3 계산
                # 잘못 설계함 ㅠㅠ
                st = y
                ed = y
                # print()
                # print("x, y, d1, d2")
                # print(x, y, d1, d2)
                # 5 먼저 채우고 나머지를 아래 기준으로 채워야함
                for r in range(x, x+d1+d2+1): #
                    #가로 시작 st 1씩 빼가다가 r이 x+d1 이후이면 더하기 시작
                    #가로 끝 ed 1씩 더해가다가 x+d2 이후이면 빼기 시작
                    for c in range(st, ed+1):
                        popu[r][c] = 4
                        population[4]+= arr[r][c]

                    if r<x+d1:
                        st -= 1
                    else:
                        st += 1

                    if r<x+d2:
                        ed += 1
                    else:
                        ed -= 1


                for r in range(n):
                    for c in range(n):
                        if popu[r][c] == 4:
                            continue
                        if r < x + d1 and c <= y:
                            population[0] += arr[r][c]
                            popu[r][c] = 0
                        elif r <= x + d2 and y < c < n:
                            population[1] += arr[r][c]
                            popu[r][c] = 1
                        elif x + d1 <= r < n and c < y - d1 + d2:
                            population[2] += arr[r][c]
                            popu[r][c] = 2
                        elif x + d2 < r < n and y - d1 + d2 <= c < n:
                            population[3] += arr[r][c]
                            popu[r][c] = 3
                if is_possible():
                    answer = min(max(population) - min(population), answer)


                # for i in range(n):
                #     print(popu[i])
                # print(population)
                # print(max(population) - min(population))
                # print()
print(answer)