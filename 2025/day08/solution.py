import math

file_name = 'input.txt'

with open(file_name) as f:
    input_data = f.read().splitlines()

def build_circuits(distances, n):
    circuits = []
    d = 0
    for _ in range(n):
        dist, l1, l2 = distances[d]
        c1_index = None
        c2_index = None
        for index, circuit in enumerate(circuits):
            if l1 in circuit:
                c1_index = index
            if l2 in circuit:
                c2_index = index
            if c1_index and c2_index:
                break

        if c1_index != c2_index:
            if c1_index is None:
                circuits[c2_index].add(l1)
            elif c2_index is None:
                circuits[c1_index].add(l2)
            else:
                circuits[c1_index] = circuits[c1_index].union(circuits[c2_index])
                del circuits[c2_index]
        elif c1_index == c2_index and c1_index is None:
            circuits.append({l1, l2})
        d += 1

    return circuits

def build_circuits_part_two(distances, n):
    circuits = []
    d = 0
    connections = 1
    last_light = None
    prelast_light = None
    while connections < n:
        dist, l1, l2 = distances[d]
        c1_index = None
        c2_index = None
        for index, circuit in enumerate(circuits):
            if l1 in circuit:
                c1_index = index
            if l2 in circuit:
                c2_index = index
            if c1_index and c2_index:
                break

        if c1_index != c2_index:
            if c1_index is None:
                circuits[c2_index].add(l1)
            elif c2_index is None:
                circuits[c1_index].add(l2)
            else:
                circuits[c1_index] = circuits[c1_index].union(circuits[c2_index])
                del circuits[c2_index]
            connections += 1
            last_light = l1
            prelast_light = l2
        elif c1_index == c2_index and c1_index is None:
            circuits.append({l1, l2})
            connections += 1
        d += 1

    return last_light, prelast_light

def abs_dist(light1, light2):
    l1 = light1.split(',')
    l2 = light2.split(',')
    return math.sqrt((int(l1[0]) - int(l2[0])) ** 2 + (int(l1[1]) - int(l2[1])) ** 2 + (int(l1[2]) - int(l2[2])) ** 2)

def multiply_circuits(lights, part):
    result = 1
    dist = []
    for i in range(len(lights) - 1):
        for j in range(i + 1, len(lights)):
            dist.append((abs_dist(lights[i], lights[j]), i, j))
    dist.sort()
    if part == 1:
        circuits = build_circuits(dist, 1000)
        circuits.sort(reverse=True, key=lambda x: len(x))
        return result * len(circuits[0]) * len(circuits[1]) * len(circuits[2])
    else:
        last_light, prelast_light = build_circuits_part_two(dist, len(lights))
        l1 = lights[last_light].split(',')[0]
        l2 = lights[prelast_light].split(',')[0]
        return int(l1) * int(l2)


print('Lösung zu Teil 1:', multiply_circuits(input_data, 1))
print('Lösung zu Teil 2:', multiply_circuits(input_data, 2))