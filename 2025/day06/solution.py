from collections import defaultdict

file_name = 'input.txt'

with open(file_name) as f:
    homework = f.read().splitlines()

def homework_check_part_two(hw):
    result = 0
    ops = hw[-1]
    nums = []
    for col in range(len(hw[0]) - 1, -1, -1):
        digits = []
        for line in hw[:-1]:
            char = line[col]
            if char == ' ' or char == '\n':
                continue
            else:
                digits.append(char)
        new_num = ''.join(digits)
        if new_num:
            nums.append(int(new_num))
        if ops[col] in '+*':
            if ops[col] == '+':
                result += sum(nums)
            else:
                res = 1
                for num in nums:
                    res *= num
                result += res
            nums = []
    return result


def homework_check(hw):
    for i, line in enumerate(hw):
        hw[i] = [c for c in line.split(' ') if c != ' ' and c != '']

    ops = hw[-1]
    nums = hw[:-1]

    result = 0
    for i, op in enumerate(ops):
        if op == '+':
            for j in range(len(nums)):
                result += int(nums[j][i])
        else:
            res = 1
            for j in range(len(nums)):
                res *= int(nums[j][i])
            result += res
    return result


print('Lösung zu Teil 1:', homework_check(homework.copy()))
print('Lösung zu Teil 2:', homework_check_part_two(homework.copy()))