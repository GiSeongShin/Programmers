def solution(N, number):
    # N 을 1번 사용한 경우
    # N 을 2번 사용한 경우
    # .....
    # N 을 8번 사용한 경우
    # N 을 9번 이상 사용한 경우 (-1)

    # N 을 4번 사용한 경우
    # -> N 1개 (+, -, *, /) N 3개
    # -> N 2개 (+, -, *, /) N 2개
    # -> N 3개 (+, -, *, /) N 1개
    # -> N 4개 (NNNN)
    # ====================== End of Description

    # 8번 동작까지 답이 없으면 answer 는 -1 이다
    answer = -1
    # rs 에는 N 을 사용한 횟수 별 결과를 저장한다.
    # rs[0] = N 이 1번 // rs[1] = N 이 2번 ...
    rs = []
    # i = 1, 2, 3 ... 7, 8
    for i in range(1, 9):
        cases = set()
        cases.add(int(str(N) * i))
        # j = 8, 7, 6 ... 2, 1
        for j in range(0, i-1):
            # rs[0], rs[1], rs[2] ...
            for k in rs[j]:
                # rs[7], rs[6], rs[5] ...
                for l in rs[-j-1]:
                    cases.add(k + l)
                    cases.add(k - l)
                    cases.add(k * l)
                    if l != 0:
                        cases.add(k / l)
        # N 이 i 인 cases 중 정답 number 가 있을 시 사용횟수의 최솟값이다
        if number in cases:
            return i
        rs.append(cases)

    return answer


solution(5, 12)