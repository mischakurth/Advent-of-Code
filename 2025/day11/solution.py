from functools import lru_cache

file_name = 'input.txt'
with open(file_name) as f:
    input_data = f.read().splitlines()
    input_data_map = {}
    for line in input_data:
        input_source, input_targets = line.split(':')
        input_targets = [t for t in input_targets.split(' ') if t != '']
        input_data_map[input_source] = set(input_targets)

class Solution:
    def __init__(self, data_map):
        self.data_map = data_map

    def count_paths(self, source, target, avoid):
        count = 0
        stack = [[{source}, source]]
        while stack:
            visited_nodes, last_node = stack.pop()
            for t in self.data_map[last_node]:
                if t == target:
                    count += 1
                else:
                    if t not in avoid:
                        stack.append([visited_nodes | {t}, t])
        return count

    def count_paths_part_two_dfs(self):
        count = 0
        count += self.count_paths('svr', 'fft', {'out', 'dac'}) * \
                 self.count_paths('fft', 'dac', {'out', 'svr'}) * \
                 self.count_paths('dac', 'out', {'fft', 'svr'})
        count += self.count_paths('svr', 'dac', {'out', 'fft'}) * \
                 self.count_paths('dac', 'fft', {'out', 'svr'}) * \
                 self.count_paths('fft', 'out', {'dac', 'svr'})
        return count

    def memoized_count_paths(self, start, target):
        @lru_cache(None)
        def dfs(curr_device, seen_fft, seen_dac):
            if curr_device == target:
                return int(seen_fft and seen_dac)
            count = 0
            for next_device in self.data_map[curr_device]:
                count += dfs(
                    next_device,
                    seen_fft or (next_device == "fft"),
                    seen_dac or (next_device == "dac")
                )
            return count

        return dfs(start, False, False)


s = Solution(input_data_map)
print('Lösung zu Teil 1:', s.count_paths('you', 'out', []))
print('Lösung zu Teil 2:', s.memoized_count_paths('svr', 'out'))
# print('Lösung zu Teil 2:', s.count_paths_part_two_dfs())