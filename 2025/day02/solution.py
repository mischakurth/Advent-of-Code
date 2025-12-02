class Solution:

    @staticmethod
    def invalid_id_addition_part_one(file_name):
        with open(file_name) as f:
            ranges = f.read().split(',')
        ids = 0
        for r in ranges:
            start, end = r.split('-')
            if len(start) == len(end) and len(start) % 2 == 1:
                continue
            for check_id in range(int(start), int(end) + 1):
                check_id = str(check_id)
                n = len(check_id)
                if n % 2 == 1:
                    continue
                if check_id[:n//2] == check_id[n//2:]:
                    ids += int(check_id)
        return ids


    def invalid_id_addition_part_two(self, file_name):
        #input_string = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
        #ranges = input_string.split(',')
        with open(file_name) as f:
            ranges = f.read().split(',')
        ids = 0
        for r in ranges:
            start, end = r.split('-')
            for check_id in range(int(start), int(end) + 1):
                if self.is_invalid(check_id):
                    ids += check_id
        return ids

    @staticmethod
    def is_invalid(check_id):
        check_id = str(check_id)
        for i in range(1, len(check_id)):
            id_substring = set()
            reps, modulo = divmod(len(check_id), i)
            if modulo != 0:
                continue
            len_rep = len(check_id) // reps
            for rep in range(reps):
                substr = check_id[rep * len_rep : (rep + 1) * len_rep]
                id_substring.add(substr)
                if len(id_substring) == 2:
                    break
            if len(id_substring) == 1:
                return True
        return False

s = Solution()
print('Lösung zu Teil 1: ', s.invalid_id_addition_part_one('input.txt'))
print('Lösung zu Teil 2: ', s.invalid_id_addition_part_two('input.txt'))