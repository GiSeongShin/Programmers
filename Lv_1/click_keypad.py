# my answer
def solution(numbers, hand):
    # 1,4,7 은 무조건 L
    # 3,6,9 는 무조건 R
    # 왼손 오른손 현재 위치를 기억할 변수가 필요
    # 현재 위치를 기준으로 거리를 체크하는 로직이 필요
    # 거리가 같은지 비교하고 같으면 hand 기준으로 처리
    answer = ''
    left_distance = 0
    left_line = 3
    right_distance = 0
    right_line = 3
    # keyword : 숫자만을 입력한다.
    # 입력된 숫자는 3으로 나눠진다?
    # if number == 0 / number//3 == 0 / number//3 == 1 / number//3 == 2

    def line_checker(number):
        if number == 0:
            return 3
        else:
            return (number-1)//3

    while len(numbers) > 0:
        if numbers[0] in [1, 4, 7]:
            answer += 'L'
            left_line = line_checker(numbers[0])
            left_distance = 0
        elif numbers[0] in [3, 6, 9]:
            answer += 'R'
            right_line = line_checker(numbers[0])
            right_distance = 0
        else:
            number_line = line_checker(numbers[0])
            if abs(number_line - left_line) + left_distance < abs(number_line - right_line) + right_distance:
                answer += 'L'
                left_line = line_checker(numbers[0])
                left_distance = -1
            elif abs(number_line - left_line) + left_distance > abs(number_line - right_line) + right_distance:
                answer += 'R'
                right_line = line_checker(numbers[0])
                right_distance = -1
            else:
                if hand == "left":
                    answer += 'L'
                    left_line = line_checker(numbers[0])
                    left_distance = -1
                else:
                    answer += 'R'
                    right_line = line_checker(numbers[0])
                    right_distance = -1

        numbers.pop(0)

    return answer


# best answer
# 키패드를 좌표로 2차원 행렬을 만들고 가로거리 세로거리를 구하는 방식인듯.
# 출제자가 원하는 해결방식일듯..

def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer