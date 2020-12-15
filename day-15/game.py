with open("input.txt", mode="r") as f:
    numbers = [int(n) for n in f.readline().split(",")]

i = len(numbers)
previously_visited = {n: (i, True, None) for i, n in enumerate(numbers)}

previous_number = numbers[-1]
while i != 30000000:
    previously = previously_visited[previous_number]
    previous_index, is_first_time, potential_next_number = previously

    next_number = 0 if is_first_time else potential_next_number
    next_first_time = False if next_number in previously_visited else True
    target = previously_visited.get(next_number)
    if not target:
        target_potential_next_number = None
    else:
        target_index, _, _ = target
        target_potential_next_number = i - target_index
    previous_number = next_number
    previously_visited[next_number] = (i, next_first_time, target_potential_next_number)
    i += 1

print("Answer:", next_number)