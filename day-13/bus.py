from math import lcm

# part 1
# with open("input.txt", mode="r") as f:
#     arrival_time = int(f.readline())
#     timestamps = [int(t) for t in f.readline().split(",") if t != "x"]
#
# print(arrival_time, timestamps)
#
# earliest_times = {}
# for t in timestamps:
#     earliest_time = ceil(arrival_time / t) * t
#     earliest_times[earliest_time] = t
#
# print(earliest_times)
# print("part 1:", (min(earliest_times) - arrival_time) * earliest_times[min(earliest_times)])


with open("input.txt", mode="r") as f:
    _ = int(f.readline())
    line = f.readline()
    timestamps = [(int(t), i) for i, t in enumerate(line.split(",")) if t != "x"]
    largest_index = max(timestamps)[1]
    timestamps = sorted([(t[0], (t[1]-largest_index)) for t in timestamps], reverse=True)



start_time = max(timestamps)[0]
# longest_timestamp = max(timestamps)
print(start_time)
print(timestamps)
root = start_time#ceil(200000000000000/start_time) * int(start_time)
while True:
    success = True
    successes = []
    for timestamp in timestamps:
        t, i = timestamp
        if not ((root + i) % t == 0):
            success = False
            failure = timestamp
            break
        else:
            successes.append(timestamp[0])
    if success:
        answer = (root - len(timestamps)+1)
        normalize_negatives = min([0, *[n[1] for n in timestamps if n[1] < 0]])
        print("success", root + normalize_negatives, " but you have to subtract the negative number from above")
        break
    else:
        # whenever we find a success, we lock it in. We can now increment the root by the LCM of all the successes.
        # for example, if i have 2, 3, 14 - the first number that "works" for 2, 3 is 2. Using this base, I'm safe to
        # increment by lcm(2,3) (i.e 6) from that base and I know that (root + 1)%3 0 - 8, 14, 20, 26, etc. When I hit
        # 26, I find out 14 works. Now I can take lcm(2, 3, 14) (which is 42).
        root += lcm(*successes)
