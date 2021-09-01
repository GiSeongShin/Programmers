answer = 0


def dfs(idx, sum, numbers, target):
    global answer
    if len(numbers) == idx:
        if sum == target:
            answer += 1
            return
        else:
            return

    dfs(idx=idx + 1, sum=sum + numbers[idx], numbers=numbers, target=target)
    dfs(idx=idx + 1, sum=sum - numbers[idx], numbers=numbers, target=target)


def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer


# 숫자앞에 + or - 가 들어감
# 모든 경우의 수를 완료한 뒤 target 과 sum 을 비교한다.
numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)
