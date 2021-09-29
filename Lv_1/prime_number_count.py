from itertools import combinations


def solution(nums):
    # combinations 를 활용하면 모든 경우의 수를 구할 수 있다.
    cmb_list = combinations(nums, 3)

    answer = 0
    for case in cmb_list:
        num = sum(case)

        # 소수 판별은 1과 자기 자신이외의 숫자로 나눠지지 않는 숫자
        # num 의 절반보다 큰 값으로 나누면 어차피 안나눠진다.
        is_prime = False
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True

        if is_prime:
            answer += 1

    return answer

# 수정 답안
# python 에는 for else 구문이 있다.
# for else 구문에서는 for 문이 break 로 끝나면 else 부분이 실행된다.
# 이렇게 하면 is_prime 이 필요없다.


def solution(nums):
    cmb_list = combinations(nums, 3)

    answer = 0
    for case in cmb_list:
        num = sum(case)

        # num 의 절반보다 큰 값으로 나누면 어차피 안나눠진다.
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                break
        else:
            answer += 1

    return answer