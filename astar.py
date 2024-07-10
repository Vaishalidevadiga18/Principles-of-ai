import heapq

class Node:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def astar(start, end, grid):
    open = []
    heapq.heappush(open, Node(start[0], start[1], 0, abs(start[0] - end[0]) + abs(start[1] - end[1])))
    closed = set()
    while open:
        node = heapq.heappop(open)
        if (node.x, node.y) == end:
            return node.g
        if (node.x, node.y) in closed:
            continue
        closed.add((node.x, node.y))
        for x, y in [(node.x + 1, node.y), (node.x - 1, node.y), (node.x, node.y + 1), (node.x, node.y - 1)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                new_g = node.g + 1
                new_h = abs(x - end[0]) + abs(y - end[1])
                new_node = Node(x, y, new_g, new_h)
                heapq.heappush(open, new_node)
    return None

if __name__ == "__main__":
    grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
    start = (0, 0)
    end = (3, 0)
    print(astar(start, end, grid))
