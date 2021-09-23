# my answer
def solution(lottos, win_nums):
    # 최고점 : 0 으로 표기된 숫자가 모두 일치할 경우
    # 최저점 : 0 으로 표기된 숫자가 모두 일치하지 않을 경우
    zero_count = 0
    for num in lottos:
        if num == 0:
            zero_count += 1
        elif num in win_nums:
            win_nums.remove(num)

    # lottos == 0: 1 // lottos == 1: 2
    max_val = len(win_nums) - zero_count + 1 if len(win_nums) - zero_count != 6 else 6
    min_val = len(win_nums) + 1 if len(win_nums) != 6 else 6
    answer = [max_val, min_val]
    return answer

# best answer
def solution(lottos, win_nums):
    # 최고점 : 0 으로 표기된 숫자가 모두 일치할 경우
    # 최저점 : 0 으로 표기된 숫자가 모두 일치하지 않을 경우
    rank = [6, 6, 5, 4, 3, 2, 1]
    zero_count = 0
    ans = 0
    for num in lottos:
        if num == 0:
            zero_count += 1
        elif num in win_nums:
            ans += 1

    answer = [rank[ans + zero_count], rank[ans]]
    return answer