from collections import deque

file_name = 'input.txt'
with open(file_name) as f:
    data_input = f.read().splitlines()

class Solution():
    def __init__(self, data):
        self.data = data

    def count_button_presses(self):
        total_presses = 0
        for line in self.data:
            parts = line.split(' ')
            indicators = parts[0][1:-1]
            buttons = [b[1:-1] for b in parts[1:-1]]
            indicators = [1 if char == '#' else 0 for char in indicators]
            buttons = [set([int(b) for b in button.split(',')]) for button in buttons]
            curr = [0 for _ in range(len(indicators))]
            min_presses = self.bfs_search(indicators, buttons, curr)
            total_presses += min_presses
        return total_presses

    def bfs_search(self, end_state, buttons, start_state):
        start_state_tuple = tuple(start_state)
        target_state_tuple = tuple(end_state)
        q = deque([(start_state_tuple, 0, -1)])
        while q:
            state, count, last_index = q.popleft()
            if state == target_state_tuple:
                return count
            for i in range(last_index + 1, len(buttons)):
                button = buttons[i]
                new_state = self.switch_button(state, button)
                q.append((new_state, count + 1, i))
        return float('inf')

    def count_joltage_presses(self):
        total_presses = 0
        for line in self.data:
            parts = line.split(' ')
            joltage = tuple(int(p) for p in parts[-1][1:-1].split(','))
            buttons = [b[1:-1] for b in parts[1:-1]]
            buttons = [set([int(b) for b in button.split(',')]) for button in buttons]
            min_presses = self.bfs_search_joltage(joltage, buttons)
            total_presses += min_presses
        return total_presses

    def bfs_search_joltage(self, end_state, buttons):
        start_state = tuple([0 for _ in range(len(end_state))])
        visited = {start_state}
        q = deque([(start_state, 0)])
        while q:
            state, count = q.popleft()
            if state == end_state:
                return count
            for b in buttons:
                new_state = self.switch_button_joltage(state, b)
                if new_state not in visited and self.allowed_state(new_state, end_state):
                    visited.add(new_state)
                    q.append((new_state, count + 1))

        return float('inf')

    @staticmethod
    def switch_button_joltage(curr_state, button):
        new_state = list(curr_state)
        for b in button:
            new_state[b] = new_state[b] + 1
        return tuple(new_state)

    @staticmethod
    def allowed_state(state, target):
        for s, t in zip(state, target):
            if s > t:
                return False
        return True

    @staticmethod
    def switch_button(curr_state, button):
        new_state = list(curr_state)
        for b in button:
            new_state[b] = 1 - new_state[b]
        return tuple(new_state)


test_input = '[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'
test_input = test_input.splitlines()
s = Solution(data_input)
print('Lösung zu Teil 1:', s.count_button_presses())
print('Lösung zu Teil 2:', s.count_joltage_presses())