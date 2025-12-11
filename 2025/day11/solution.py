file_name = 'input.txt'
with open(file_name) as f:
    input_data = f.read().splitlines()
    input_data_map = {}
    for line in input_data:
        source, targets = line.split(':')
        targets = [t for t in targets.split(' ') if t != '']
        input_data_map[source] = targets



class Solution():
    def __init__(self, data_map):
        self.data_map = data_map

    def count_paths(self, source, target, avoid):
        count = 0
        stack = [[source]]
        while stack:
            curr_path = stack.pop()
            for t in self.data_map[curr_path[-1]]:
                if t == target:
                    count += 1
                else:
                    if t not in avoid:
                        stack.append(curr_path + [t])
        return count

    def count_paths_part_two(self):
        count = 0
        count += self.count_paths('svr', 'fft', {'out', 'dac'}) * \
                 self.count_paths('fft', 'dac', {'out', 'svr'}) * \
                 self.count_paths('dac', 'out', {'fft', 'svr'})
        print(count)
        count += self.count_paths('svr', 'dac', {'out', 'fft'}) * \
                 self.count_paths('dac', 'fft', {'out', 'svr'}) * \
                 self.count_paths('fft', 'out', {'dac', 'svr'})

        return count


s = Solution(input_data_map)
print('Lösung zu Teil 1:', s.count_paths('you', 'out', []))
print('Lösung zu Teil 2:', s.count_paths_part_two())