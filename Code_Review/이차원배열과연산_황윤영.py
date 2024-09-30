"""
풀이시간 34분

1432 문제 읽기 시작
    일단 정독
    읽으면서 구현 관련한 생각들 주석으로 메모
    구현할 내용 메모


1437 구현 시작
    메인 로직을 구현 하기 전 로직을 담을(while) 바깥 틀부터 만들어놓음
    구현하다가 빈자리 0으로 채워줘야 한다는거 추가로 파악 ==> 문제 똑바로 안ㅇ읽냐
    100개 버리는 것도 ㄴㅏ중에 파악 ^^
    입력 인덱스 수정 ..
    실수 투성이었네

1446 디버깅 시작
    lst에 값 이상하게 들어가서 대소비교가 안된다
    에러가 나는 요소들 곳곳에서 순차적으로 print 해봄. 값이 어떻게 달라지는지 봄
    for 문을 회전한 이후이므로 row, col 의 len중 큰 값으로 가져와야함을 깨달음

    에러 나는 문젠 해결. 테케 안맞음
    0은 카운트 안하는거 놓친거 발견
1454 제출 후 오답
    100개 제외 버린다는 거 발견
    그래도 제출했을 때 런타임 에러
    문제 다시 꼼꼼히 읽음
    열의 크기가 달라질 때 처음 크기까지는 유지하도록 mx 초기값 변경

    문제에 입력값 범위 보고 주어진 R,C가 아직 범위 내의 값이 아닐 수도 있음을 깨달아서
    수정

1503 정답

피드백
    - 못한점
        문제를 너무 안읽은 문제 ............
        중요 요소 한 4개 정돈 놓쳤다



===========================구상 중 메모 =======================
행 연산은 좀 쉬울듯 ? 열 연산 어쩌지 배열 회전할까


일단 행 연산부터 생각하자.
그 행에 있는 값을 key로 개수를 value로 딕셔너리로 만들기
 그 후 items로 k, v를 튜플로 lst에 넣고 정렬해서 (정렬할 땐 value우선)
 해당 행에 끼워넣기 !

 배열 크기 맞추기 max len을 찾아서 그만큼 0으로 채워준다



연산하고 행 / 열 길이 보고 행연산 열연산 결정. .!
arr[r][c]의 값이 k 가 되면 종료 혹은 time이 101 되면 종료

"""
R, C, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
time = 0
while 1:
    row_len = len(arr)
    col_len = len(arr[0])
    if time >100 or ( R-1 < row_len and C-1<col_len and arr[R-1][C-1] == K):
        break

    #행 / 열 크기 확인
    #배열 transpose
    if row_len < col_len:
        arr = list(map(list, zip(*arr)))

    #연산하자
    for i in range(max(row_len, col_len)):
        tmp_dict = {}
        for j in range(min(row_len, col_len)):
            if arr[i][j] == 0:
                continue
            tmp_dict[arr[i][j]] = tmp_dict.get(arr[i][j],0)+1

        lst = []
        for k, v in tmp_dict.items():
            lst.append([k,v])
        lst.sort(key=lambda x:(x[1], x[0]))
        arr[i] = []
        for a in lst:
            arr[i].extend(a)
        arr[i] = arr[i][:100]
    # 0채워주자
    mx = min(row_len, col_len)
    for i in range(len(arr)):
        mx = max(mx, len(arr[i]))
    for i in range(len(arr)):
        while len(arr[i]) < mx:
            arr[i].append(0)



    #transpose했었다면 되돌리자
    if row_len<col_len:
        # for i in range(len(arr)):
        #     print(arr[i])
        # print()
        arr = list(map(list, zip(*arr)))

    time += 1
    # for i in range(len(arr)):
    #     print(arr[i])
    # print()


print(time if time<=100 else -1)