def solution(participant, completion):
    par_dict = {}
    com_dict = {}
    for par in participant:
        if par in par_dict.keys():
            par_dict[par] += 1
        else:
            par_dict[par] = 1

    for com in completion:
        if com in com_dict.keys():
            com_dict[com] += 1
        else:
            com_dict[com] = 1

    par_keys = par_dict.keys()
    com_keys = com_dict.keys()

    for key in par_keys:
        if key in com_keys:
            if par_dict[key] == com_dict[key]:
                pass
            else:
                return key
        else:
            return key


par = ["leo", "kiki", "eden"]
com = ["eden", "kiki"]
solution(par, com)

par = ["mislav", "stanko", "mislav", "ana"]
com = ["stanko", "ana", "mislav"]
solution(par, com)


# dict 로 변경하자
# name: count of name
# 이후 key 별 값을 비교하여 다른 값을 찾자
