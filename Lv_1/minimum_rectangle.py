# w, h 을 큰 값과 작은 값으로 나눈다.
# 가장 큰 값은 회전을 어떻게 하던 필요한 값이다.
# w, h 중 작은 값중 가장 큰 값을 구한다.
# 두 값을 곱한다.
# my answer
def solution(sizes):
    low_list = []
    high_list = []
    for size in sizes:
        if size[0] >= size[1]:
            high_list.append(size[0])
            low_list.append(size[1])
        else:
            high_list.append(size[1])
            low_list.append(size[0])

    low_list.sort()
    high_list.sort()

    answer = low_list[-1] * high_list[-1]
    return answer


# best answer
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
