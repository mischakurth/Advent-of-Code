class Solution:
    @staticmethod
    def get_total_distance(file_name):
        with open(file_name) as f:
            whole_list = f.read().split()

        left_list = []
        right_list = []
        for i, entry in enumerate(whole_list):
            if i % 2:
                right_list.append(entry)
            else:
                left_list.append(entry)





        total = 0


        return total



s = Solution()
print('Lösung: ', s.get_total_distance('input.txt'))