from collections import defaultdict

answered = defaultdict(int)
sum = 0
num_people = 0

with open("input.txt", mode="r", newline="\n") as f:
    for line in f.readlines():
        if len(line) == 1:
            for k, v in answered.items():
                if v == num_people:
                    sum += 1
            num_people = 0
            answered = defaultdict(int)
            continue

        num_people += 1
        for char in line:
            if char != "\n":
                answered[char] += 1

print('sum', sum)
