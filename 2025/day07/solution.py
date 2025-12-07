from collections import defaultdict

file_name = 'input.txt'

with open(file_name) as f:
    input_data = f.read().splitlines()

def count_splits(data):
    beam_cols = set()
    for i, char in enumerate(data[0]):
        if char == 'S':
            beam_cols.add(i)
    result = 0

    for line in data[1:]:
        new_beam_col = set()
        for beam_col in beam_cols:
            if line[beam_col] == '^':
                result += 1
                new_beam_col.add(beam_col - 1)
                new_beam_col.add(beam_col + 1)
            else:
                new_beam_col.add(beam_col)
        beam_cols = new_beam_col
    return result

def count_timelines(data):
    beam_cols = defaultdict(int)
    for i, char in enumerate(data[0]):
        if char == 'S':
            beam_cols[i] += 1
    result = 1

    for line in data[1:]:
        new_beam_col = defaultdict(int)
        for beam_col, freq in beam_cols.items():
            if line[beam_col] == '^':
                result += freq
                new_beam_col[beam_col - 1] += freq
                new_beam_col[beam_col + 1] += freq
            else:
                new_beam_col[beam_col] += freq
        beam_cols = new_beam_col
    return result


print('Lösung zu Teil 1:', count_splits(input_data))
print('Lösung zu Teil 2:', count_timelines(input_data))