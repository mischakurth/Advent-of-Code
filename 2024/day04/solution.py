class Solution:

    def count_xmas(self, word_search):
        total_count = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for r in range(len(word_search)):
            for c in range(len(word_search[0])):
                if word_search[r][c] == 'X':
                    for d in directions:
                        total_count += self.linear_search((r, c), 'X', word_search, d)
        return total_count

    def linear_search(self, point, char, word_search, direction):
        r, c = point
        if r < 0 or c < 0 or r == len(word_search) or c == len(word_search[0]) or word_search[r][c] != char:
            return 0
        if char == 'S':
            return 1
        next_char = 'M' if char == 'X' else 'A' if char == 'M' else 'S'
        next_point = (r + direction[0], c + direction[1])
        return self.linear_search(next_point, next_char, word_search, direction)

    @staticmethod
    def count_xmas_part_two(word_search):
        total_count = 0
        for r in range(1, len(word_search) - 1):
            for c in range(1, len(word_search[0]) - 1):
                if word_search[r][c] == 'A':
                    neigh = set()
                    neigh.add(word_search[r - 1][c - 1])
                    neigh.add(word_search[r + 1][c + 1])
                    if neigh == {'M', 'S'}:
                        neigh.clear()
                        neigh.add(word_search[r + 1][c - 1])
                        neigh.add(word_search[r - 1][c + 1])
                        if neigh == {'M', 'S'}:
                            total_count += 1
        return total_count

    def day_04(self, file_name, part):
        with open(file_name) as f:
            word_search = f.read().split()
        if part == 1:
            return self.count_xmas(word_search)
        else:
            return self.count_xmas_part_two(word_search)

s = Solution()
print('Lösung zu Teil 1: ', s.day_04('input.txt', 1))
print('Lösung zu Teil 2: ', s.day_04('input.txt', 2))