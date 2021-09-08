def solution(answers):
    # student a, b, c 는 아래의 패턴으로 찍는다.
    student_a = [1, 2, 3, 4, 5]
    student_b = [2, 1, 2, 3, 2, 4, 2, 5]
    student_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # answers 의 길이만큼 돌면서 정답여부를 체크하면 될듯.
    size = len(answers)

    # 학생들의 답안을 answers 보다 길게 만든다.
    answer_a = student_a * int(size / len(student_a) + 1)
    answer_b = student_b * int(size / len(student_b) + 1)
    answer_c = student_c * int(size / len(student_c) + 1)

    scores = [0, 0, 0]
    for idx in range(size):
        if answer_a[idx] == answers[idx]:
            scores[0] += 1
        if answer_b[idx] == answers[idx]:
            scores[1] += 1
        if answer_c[idx] == answers[idx]:
            scores[2] += 1

    max_score = max(scores)

    # 제일 큰 수를 return. 동일 값일 시 index 순으로. 학생 번호는 1부터 시작한다.
    answer = [i + 1 for i, score in enumerate(scores) if score == max_score]
    return answer


answers = [1, 2, 3, 4, 5]
solution(answers)

answers = [1, 3, 2, 4, 2]
solution(answers)