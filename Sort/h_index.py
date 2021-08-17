def solution(citations):
    # 최대값은 모든 논문의 인용 횟수가 전체 논문의 개수보다 많거나 같은 케이스
    # 최대값이 되는 케이스부터 순차적으로 확인
    # 정렬 후 i 번째 값이 (길이 - i) 보다 크면 그 이후는 전부 (길이 - i) 보다 크다
    # (길이 - i) 의 최대값이 h-index 이므로 정렬 후 (길이 - i) 와 citations[i] 를 비교한다.

    sorted_citations = sorted(citations)
    length = len(citations)
    for idx in range(length):
        if sorted_citations[idx] >= length - idx:
            return length - idx

    return 0


# 삽질기록 (시간초과)
# pivot 을 잡고 해당 수보다 큰 값이 절반을 넘어가는지 체크했음
# 두 수의 합이 소숫점인 경우가 발생하여 ceil 함수를 사용했음
# from math import ceil
#
#
# def solution(citations):
#     h_index = 0
#     t1 = 0
#     t2 = len(citations)
#     while True:
#         pivot = ceil((t1+t2) / 2)
#
#         pivot_count = 0
#         for x in citations:
#             if x >= pivot:
#                 pivot_count += 1
#
#         if pivot != len(citations) and (pivot == t1 or pivot == t2):
#             break
#
#         if pivot_count >= pivot:
#             h_index = pivot
#             t1 = pivot
#             if pivot == len(citations):
#                 break
#
#         if pivot_count < pivot:
#             t2 = pivot
#
#     answer = h_index
#     return answer
