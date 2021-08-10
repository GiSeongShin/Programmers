# https://programmers.co.kr/learn/courses/30/lessons/42862
# Greedy > 체육복

def solution(n, lost, reserve):
    # reserve_person 으로 lost_person 없애기
    # answer = n - (lost - lost_people)

    # 원본에서 lost in reserve / reserve in lost 값을 제거한다.
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for reserve_person in _reserve:
        front_person_num = reserve_person - 1
        back_person_num = reserve_person + 1

        if front_person_num in _lost:
            _lost.remove(front_person_num)
        elif back_person_num in _lost:
            _lost.remove(back_person_num)

    number_of_lost_people = len(_lost)
    answer = n - number_of_lost_people

    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
solution(n, lost, reserve)