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