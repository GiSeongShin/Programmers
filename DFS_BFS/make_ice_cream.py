# https://www.youtube.com/watch?v=7C9RgOcvkvo&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=3
# 동빈나 이코테 DFS & BFS 기초 문제 풀이

def make_ice_cream(n, m, sample):
    # 0이 있는지 체크
    # 0이 있으면 아이스크림을 만들 수 있음
    # 0이 나오면 다음 index 가 0인지 체크
    # 인접한 index 가 0일 시 인접노드를 확인
    # 인접한 index 가 1일 시 return False
    # 한 번 사용했던 자리는 얼음이 되니까 1으로 만들어줌
    count = 0

    def dfs(x, y):
        if x >= n or x < 0 or y >= m or y < 0:
            return False

        if sample[x][y] == 0:
            sample[x][y] = 1

            # 인접노드 4개 모두 체크
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else:
            return False

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1

    return count


n = 4
m = 5
sample = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

make_ice_cream(n, m, sample)
