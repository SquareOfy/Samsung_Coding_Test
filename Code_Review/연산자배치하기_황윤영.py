"""
2차
풀이 시간 : 10분
시도 횟수 : 3회
실행 시간 : 165ms
메모리 : 26 mb

실수 모음 
- 초기값 설정 실수

Routine
1. 문제 그냥 정독 ok
2. 문제 주석 복사 필요없었음 ,, 문제가 간단.. 근데 그래도 하자 ;
4. 테스트케이스 외에 고려해야할 사항 생각해보기 + 설계에 반영
    : 연산자 우선순위 무시되므로 그냥 순서대로 하자고 생각
5. 종이에 손설계 : ok
6. 주석으로 구현할 영역 정리 : ok
7. 구현 : ok
8.테스트케이스 단계별 디버깅 확인 : no
9. 1시간 지났는데 디버깅 헤매는 중이면 리셋!!

"""
"""
================= 2차 코드 리뷰 ====================

1535 문제 읽기 시작
1536 설계 시작
1538 구현 영역 주석 정리 및 구현 시작

1542 제출 후 오답 디버깅
    mx, mn 초기값 설정 문제라는걸 깨닫고 충분히 큰 값으로 함
    근데 또 틀 
    실수 출력 됨 int 로 바꿔서 해결

"""


#calculate 함수
def calculate(a, b, o):
    if o==0:
        return a+b
    if o==1:
        return a-b
    if o==2:
        return a*b

#dfs
def dfs(level, num):
    global mn_ans, mx_ans
    if level == N:
        mn_ans = min(mn_ans, num)
        mx_ans = max(mx_ans, num)

        return

    for i in range(3):
        if cnt_lst[i]==0: continue
        cnt_lst[i]-= 1
        nxt_num = calculate(num, numbers[level], i)
        dfs(level+1, nxt_num)
        cnt_lst[i]+= 1



#입력
N = int(input())
numbers = list(map(int, input().split()))
mn_ans = 1e9
mx_ans = int(-1e9)

cnt_lst = list(map(int, input().split()))
#함수 실행
dfs(1, numbers[0])
print(int(mn_ans), int(mx_ans))