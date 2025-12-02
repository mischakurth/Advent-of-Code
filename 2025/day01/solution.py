class Solution:

    @staticmethod
    def get_zero_positions_part_one(file_name):
        with open(file_name) as f:
            rotations = f.read().splitlines()  # Liste der Zeilen
        pos = 50
        zero_positions = 0
        for rot in rotations:
            if rot[0] == 'L':
                pos = (pos - int(rot[1:])) % 100
            else:
                pos = (pos + int(rot[1:])) % 100
            if pos == 0:
                zero_positions += 1
        return zero_positions

    @staticmethod
    def get_zero_positions_part_two(file_name):
        with open(file_name) as f:
            rotations = f.read().splitlines()  # Liste der Zeilen
        pos = 50
        zero_positions = 0
        #test_case = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
        #for rot in test_case:
        for rot in rotations:
            if rot[0] == 'L':
                if pos == 0:
                    zero_positions -= 1
                pos -= int(rot[1:])
            else:
                pos += int(rot[1:])

            div, modulo = divmod(pos, 100)
            zero_positions += abs(div)
            if modulo == 0 and rot[0] == 'L':
                zero_positions += 1

            pos = modulo
        return zero_positions


s = Solution()
print('Lösung Teil 1: ', s.get_zero_positions_part_one("input.txt"))
print('Lösung Teil 2: ', s.get_zero_positions_part_two("input.txt"))