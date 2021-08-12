def solution(name):
    # 1. name 을 ascii 로 변경한 뒤 위 또는 아래로 몇번 움직여야 되는지 확인한다.
    # min( ord(char) - ord('A'), ord('Z') - ord(char) + 1  ) # 위로 갈때는 Z 로 가는 1번의 횟수를 더해준다.
    #
    # 2. 좌우 이동 최소횟수
    # A 를 만나면 정방향으로 가는게 이득인지 역방향으로 돌아가는게 이득인지 확인해야함
    # A 가 연속해서 나올 수 있으니 A 가 나오면 다음 index 도 A 인지 확인해야함
    # 정방향 = len(name) - 1
    # 역방향 = idx + idx + (len(name) - next_idx)
    answer = 0
    move_count = len(name) - 1
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        move_count = min(move_count, idx + idx + (len(name) - next_idx))

    return answer + move_count


name = "JAN"
print(solution(name))
