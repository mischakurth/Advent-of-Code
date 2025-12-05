

with open('input.txt') as f:
    ranges, ingredients = f.read().split('\n\n')

def day_05(part, ranges, ingredients):
    ranges = ranges.split('\n')
    ingredients = [i for i in ingredients.split('\n') if len(i) > 0]
    if part == 1:
        result = count_fresh_ingredients(ranges, ingredients)
    else:
        result = count_fresh_ingredients_part_two(ranges)
    return result


def count_fresh_ingredients(ranges, ingredients):
    result = 0
    for i in ingredients:
        for range in ranges:
            start, end = range.split('-')
            if int(start) <= int(i) <= int(end):
                result += 1
                break
    return result

def count_fresh_ingredients_part_two(ranges):
    for i, range in enumerate(ranges):
        start, end = range.split('-')
        ranges[i] = (int(start), int(end))
    ranges.sort()
    result = 0
    cur_end = ranges[0][1]
    cur_start = ranges[0][0]
    for start, end in ranges:
        if start <= cur_end:
            cur_end = max(cur_end, end)
        else:
            result += cur_end - cur_start + 1
            cur_start = start
            cur_end = end
    return result + (cur_end - cur_start + 1)



print('Lösung zu Teil 1:', day_05(1, ranges, ingredients))
print('Lösung zu Teil 2:', day_05(2, ranges, ingredients))