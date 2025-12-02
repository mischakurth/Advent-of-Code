class Solution:

    @staticmethod
    def get_multiple_if_correct(p):
        p = p[:8]
        nums = p.split(',')
        if len(nums) > 1:
            num1 = nums[0]
            num2 = nums[1].split(')')[0]
            if num1.isdecimal() and num2.isdecimal():
                return int(num1) * int(num2)
        return 0

    def add_multiplications_part_one(self, file_name):
        with open(file_name) as f:
            parts = f.read().split('mul(')
        result = 0
        for p in parts:
            result += self.get_multiple_if_correct(p)
        return result

    def add_multiplications_part_two(self, file_name):
        with open(file_name) as f:
            parts = f.read().split('don\'t()')
        result = 0
        for i, p in enumerate(parts[1:]):
            possible_index = p.find('do()')
            parts[i + 1] = p[possible_index:]
        for p in parts:
            segment = p.split('mul(')
            for s in segment:
                result += self.get_multiple_if_correct(s)
        return result

s = Solution()
print('Lösung zu Teil 1: ', s.add_multiplications_part_one('input.txt'))
print('Lösung zu Teil 2: ', s.add_multiplications_part_two('input.txt'))