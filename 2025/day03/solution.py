class Solution:

    @staticmethod
    def max_joltage(bank):
        bank = str(bank)
        if len(bank) == 1:
            return int(bank)
        first_battery = 0
        for i in range(len(bank) - 1):
            if int(bank[i]) > int(bank[first_battery]):
                first_battery = i
            if int(bank[first_battery]) == 9:
                break
        second_battery = first_battery + 1
        for j in range(first_battery + 1, len(bank)):
            if int(bank[j]) > int(bank[second_battery]):
                second_battery = j
            if int(bank[second_battery]) == 9:
                break
        return int(bank[first_battery] + bank[second_battery])

    @staticmethod
    def max_joltage_overdrive(bank):
        bank = str(bank)
        last_battery_index = -1
        total_battery = []
        for i in range(11, -1, -1):
            i_battery = last_battery_index + 1
            for j in range(i_battery, len(bank) - i):
                if int(bank[j]) > int(bank[i_battery]):
                    i_battery = j
                if int(bank[i_battery]) == 9:
                    break
            last_battery_index = i_battery
            total_battery.append(bank[i_battery])
        return int(''.join(total_battery))


    def get_joltage(self, file_name, part):
        with open(file_name) as f:
            banks = f.read().splitlines()
        total_joltage = 0
        if part == 1:
            for bank in banks:
                total_joltage += self.max_joltage(bank)
        else:
            for bank in banks:
                total_joltage += self.max_joltage_overdrive(bank)
        return total_joltage


s = Solution()
print('Lösung zu Teil 1: ', s.get_joltage('input.txt', 1))
print('Lösung zu Teil 2: ', s.get_joltage('input.txt', 2))