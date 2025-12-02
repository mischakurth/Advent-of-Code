class Solution:

    @staticmethod
    def safe_report_part_one(r):
        if r != sorted(r) and r != sorted(r, reverse=True):
            return False
        for level_1, level_2 in zip(r, r[1:]):
            diff = abs(level_1 - level_2)
            if not (1 <= diff <= 3):
                return False
        return True

    def safe_report_part_two(self, r):
        # muss eine Zahl entfernen
        for i in range(len(r)):
            if self.safe_report_part_one(r[:i] + r[i + 1:]):
                return True
        else:
            return False

    def count_safe_reports_part_one(self, file_name):
        with open(file_name) as f:
            reports = f.read().splitlines()
        safe_reports = 0
        for line in reports:
            r = line.split()
            r = [int(i) for i in r]
            if self.safe_report_part_one(r):
                safe_reports += 1
        return safe_reports

    def count_safe_reports_part_two(self, file_name):
        with open(file_name) as f:
            reports = f.read().splitlines()
        safe_reports = 0
        for line in reports:
            r = line.split()
            r = [int(i) for i in r]
            if self.safe_report_part_two(r):
                safe_reports += 1
        return safe_reports

s = Solution()
print('Lösung zu Teil 1: ', s.count_safe_reports_part_one('input.txt'))
print('Lösung zu Teil 2: ', s.count_safe_reports_part_two('input.txt'))