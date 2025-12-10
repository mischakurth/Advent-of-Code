from collections import defaultdict

file_name = 'input.txt'
with open(file_name) as f:
    data = f.read().splitlines()

class Solution:
    def __init__(self, input_data):
        self.data = [line.split(',') for line in input_data]
        self.data = [(int(point[0]), int(point[1])) for point in self.data]
        self.xs = set()
        self.ys = set()
        for x,y in self.data:
            self.xs.add(x)
            self.ys.add(y)
        self.edge_map_x, self.edge_map_y = self.get_edge_points()

    def get_edge_points(self):
        edge_map_x = defaultdict(lambda: [float('inf'), float('-inf')])
        edge_map_y = defaultdict(lambda: [float('inf'), float('-inf')])
        for p1, p2 in zip(self.data, self.data[1:]):
            if p1[1] == p2[1]:
                for x in self.xs:
                    if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]):
                        edge_map_x[x][0] = min(edge_map_x[x][0], p1[1])
                        edge_map_x[x][1] = max(edge_map_x[x][1], p1[1])
            else:
                for y in self.ys:
                    if min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]):
                        edge_map_y[y][0] = min(edge_map_y[y][0], p1[0])
                        edge_map_y[y][1] = max(edge_map_y[y][1], p1[0])
        return edge_map_x, edge_map_y

    def valid_rect(self, p1, p2):
        min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
        min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])
        for x in self.xs:
            if min_x <= x <= max_x:
                if min_y < self.edge_map_x[x][0] or max_y > self.edge_map_x[x][1]:
                    return False
        for y in self.ys:
            if min_y <= y <= max_y:
                if min_x < self.edge_map_y[y][0] or max_x > self.edge_map_y[y][1]:
                    return False
        return True

    def max_rect_size(self, part):
        max_area = 0
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                if part == 1 or self.valid_rect(self.data[i], self.data[j]):
                    max_area = max(max_area, self.get_area(self.data[i], self.data[j]))
        return max_area

    @staticmethod
    def get_area(point_a, point_b):
        return abs(point_a[0] - point_b[0] + 1) * abs(point_a[1] - point_b[1] + 1)

s = Solution(data)
print('Lösung zu Teil 1:', s.max_rect_size(1))
print('Lösung zu Teil 2:', s.max_rect_size(2))