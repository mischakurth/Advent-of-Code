from collections import defaultdict

class Solution:
    @staticmethod
    def is_correct_order(pages, prereqs, update):
        pages_copy = pages.copy()
        for page in update:
            pages_copy.discard(page)
            for prereq in prereqs[page]:
                if prereq in pages_copy:
                    return False
        return True

    def correct_order(self, update, pages, prereqs):
        if self.is_correct_order(pages, prereqs, update):
            return int(update[len(update) // 2])
        else:
            return 0

    def incorrect_order(self, update, pages, prereqs):
        if self.is_correct_order(pages, prereqs, update):
            return 0
        else:
            updated_update = []
            next_pages = []
            for p in pages:
                if len(prereqs[p]) == 0:
                    next_pages.append(p)
            while next_pages:
                next_pages.sort()
                updated_update.append(next_pages[0])
                pages.remove(updated_update[-1])
                next_pages.pop(0)
                for page in prereqs.keys():
                    prereqs[page].discard(updated_update[-1])
                for p in pages:
                    if len(prereqs[p]) == 0:
                        next_pages.append(p)

            return int(updated_update[len(updated_update) // 2])

    def day_05(self, file_name, part):
        with open(file_name) as f:
            rules, updates = f.read().split('\n\n')
        rules = rules.split('\n')
        updates = filter(None, updates.split('\n'))
        result = 0
        for update in updates:
            update_list = update.split(',')
            pages = set(update_list)
            prereqs = defaultdict(set)
            for rule in rules:
                rule = rule.split('|')
                if rule[0] in pages and rule[1] in pages:
                    prereqs[rule[1]].add(rule[0])
            if part == 1:
                result += self.correct_order(update_list, pages, prereqs)
            if part == 2:
                result += self.incorrect_order(update_list, pages, prereqs)
        return result

s = Solution()
print('Lösung zu Teil 1: ', s.day_05('input.txt', 1))
print('Lösung zu Teil 2: ', s.day_05('input.txt', 2))