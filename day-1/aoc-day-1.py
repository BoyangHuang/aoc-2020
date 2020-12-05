numbers = []
with open("input_numbers.txt", mode="r", newline="\n") as f:
    lines = f.readlines()
    for line in lines:
        numbers.append(int(line.strip()))

min_num = min(numbers)

potentials = {}
for number in numbers:
    potentials[2020-number] = number

for k, v in potentials.items():
    for number in numbers:
        if k-number in numbers:
            print(number, k-number, potentials[k], number * (k-number) * potentials[k])
            break
