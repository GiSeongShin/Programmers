def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        cloth_name = cloth[0]
        cloth_type = cloth[1]

        if cloth_type in clothes_dict.keys():
            clothes_dict[cloth_type].append(cloth_name)
        else:
            clothes_dict[cloth_type] = [cloth_name]

    clothes_len = []
    for key in clothes_dict.keys():
        clothes_len.append(len(clothes_dict[key]) + 1)

    answer = 1
    for i in clothes_len:
        answer = answer * i

    # 아무것도 입지 않은 케이스는 제외한다.
    answer = answer - 1

    return answer


# [의상의 이름, 의상의 종류]
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# 의상의 종류별로 하나씩 걸치는 횟수를 count
solution(clothes)


# ㅇㅇ
# ㅁㅁ
# ㅅㅅ
# ㅂㅂ
# 3 * 3 * 3 * 3
# 81가지? - 1
