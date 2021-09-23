# 처음에 정규식으로 접근을 하려고 했음.
# 로직을 짜다보니 replace 로 한 번에 끝나서 제출.
def solution(s):
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for key in number_dict.keys():
        s = s.replace(key, str(number_dict[key]))

    answer = int(s)
    return answer
