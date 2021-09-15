def solution(number, k):
    # k 의 개수만큼 숫자를 제거해야함
    # 숫자를 차례대로 리스트에 저장하고 더 큰 값이 나오면 제거해준다
    number_stack = []

    for i in number:
        while True:
            if len(number_stack) > 0 and k > 0 and number_stack[-1] < i:
                number_stack.pop()
                k -= 1
            else:
                break

        number_stack.append(i)

    # k 가 0보다 큰 경우 number_stack 의 맨 뒤에서 하나씩 빼준다.
    while k > 0:
        number_stack.pop()
        k -= 1

    return ''.join(number_stack)