def get_new_range(lower, upper, front_or_back):
    if len(front_or_back) == 0:
        return lower
    midpoint = lower + (upper - lower) // 2

    mode = front_or_back[0]
    if mode in  ["B", "R"]: # UPPER
        return get_new_range(midpoint + 1, upper, front_or_back[1:])

    if mode in["F", "L"]: # LOWER
        return get_new_range(lower, midpoint-1, front_or_back[1:])

fb = []
lr = []
with open("seats.txt", mode="r", newline="\n") as f:
    for line in f.readlines():
        fb.append(line[:7])
        lr.append(line[7:].replace("\n", ""))

secret_ids = []
for i, front_back in enumerate(fb):
    lower = 0
    upper = 127
    row_num = get_new_range(lower, upper, front_back)

    left = 0
    right = 7
    col_num = get_new_range(left, right, lr[i])

    secret_id = row_num * 8 + col_num
    secret_ids.append(secret_id)


for i in range(min(secret_ids)+1, max(secret_ids)):
    if i not in secret_ids:
        print("My id: ", i)
        break