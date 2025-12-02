from collections import defaultdict


class Solution:
    @staticmethod
    def get_total_distance_part_one(file_name):
        with open(file_name) as f:
            whole_list = f.read().split()
        left_list = []
        right_list = []
        for i, entry in enumerate(whole_list):
            if i % 2:
                right_list.append(entry)
            else:
                left_list.append(entry)
        left_list.sort()
        right_list.sort()
        total = 0
        for left, right in zip(left_list, right_list):
            total += abs(int(left) - int(right))
        return total

    @staticmethod
    def get_total_distance_part_two(file_name):
        with open(file_name) as f:
            whole_list = f.read().split()

        left_list = defaultdict(int)
        right_list = defaultdict(int)
        for i, entry in enumerate(whole_list):
            if i % 2:
                right_list[entry] += 1
            else:
                left_list[entry] += 1
        distance = 0
        for number, freq in left_list.items():
            distance += freq * int(number) * right_list[number]
        return distance



s = Solution()
print('Lösung Teil 1: ', s.get_total_distance_part_one('input.txt'))
print('Lösung Teil 2: ', s.get_total_distance_part_two('input.txt'))