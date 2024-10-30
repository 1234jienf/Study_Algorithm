from collections import deque

SIZE = 5
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


class Board:
    def __init__(self):
        self.cells = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    def getCells(self):
        self.cells = [list(map(int, input().split())) for _ in range(SIZE)]

    def inRange(self, y, x):
        return 0 <= y < SIZE and 0 <= x < SIZE

    def rotate(self, sy, sx, cnt):
        result = Board()
        result.cells = [row[:] for row in self.cells]
        for _ in range(cnt):
            tmp = result.cells[sy + 0][sx + 2]
            result.cells[sy + 0][sx + 2] = result.cells[sy + 0][sx + 0]
            result.cells[sy + 0][sx + 0] = result.cells[sy + 2][sx + 0]
            result.cells[sy + 2][sx + 0] = result.cells[sy + 2][sx + 2]
            result.cells[sy + 2][sx + 2] = tmp

            tmp = result.cells[sy + 1][sx + 2]
            result.cells[sy + 1][sx + 2] = result.cells[sy + 0][sx + 1]
            result.cells[sy + 0][sx + 1] = result.cells[sy + 1][sx + 0]
            result.cells[sy + 1][sx + 0] = result.cells[sy + 2][sx + 1]
            result.cells[sy + 2][sx + 1] = tmp
        return result

    # 직접 값을 0으로 바꿔주는 것까지 수행한다
    # 그러므로 항상 복사된 Board에서만 돌리는 것을 명심하자
    def cal_score(self):
        score = 0
        visit = [[False for _ in range(SIZE)] for _ in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                if not visit[i][j]:
                    q = deque([(i, j)])
                    trace = deque([(i, j)])
                    visit[i][j] = True
                    while q:
                        y, x = q.popleft()
                        for k in range(4):
                            ny, nx = y + dy[k], x + dx[k]
                            if self.inRange(ny, nx) and self.cells[ny][nx] == self.cells[y][x] and not visit[ny][nx]:
                                q.append((ny, nx))
                                trace.append((ny,nx))
                                visit[ny][nx] = True
                    if len(trace) >= 3:
                        score += len(trace)
                        while trace:
                            ty, tx = trace.popleft()
                            self.cells[ty][tx] = 0
        return score

    def fill(self, q):
        for j in range(SIZE):
            for i in reversed(range(SIZE)):
                if self.cells[i][j] == 0:
                    self.cells[i][j] = q.popleft()

    def __repr__(self):
        return repr(self.cells)

def main():
    K, M = map(int, input().split())
    board = Board()
    board.getCells()
    q = deque()
    for t in list(map(int, input().split())):
        q.append(t)

    for _ in range(K):
        maxScore = 0
        maxScoreBoard = None
        for cnt in range(1, 4):
            for sx in range(3):
                for sy in range(3):
                    rotated = board.rotate(sy, sx, cnt)
                    score = rotated.cal_score()
                    if maxScore < score:
                        maxScore = score
                        maxScoreBoard = rotated
        if maxScoreBoard is None:
            break
        board = maxScoreBoard
        while True:
            board.fill(q)
            newScore = board.cal_score()
            if newScore == 0:
                break
            maxScore += newScore

        print(maxScore, end=" ")

if __name__ == "__main__":
    main()