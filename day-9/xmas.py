from collections import deque

numbers = deque()

with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.readlines()):
        numbers.append(int(line))


current_numbers = deque()
answer = 375054920

contiguous_sum = 0

while True:
    if contiguous_sum == answer:
        print(min(current_numbers) + max(current_numbers))
        break

    elif contiguous_sum < answer:
        new_number = numbers.popleft()
        contiguous_sum += new_number
        current_numbers.append(new_number)

    else:
        contiguous_sum -= current_numbers.popleft()
