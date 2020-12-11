seatmap = []
directions = [(0,1), (1,0), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]


with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.readlines()):
        seatmap.append(line.replace("\n", ""))

def get_desired_seat_state(seatmap, seat_coordinate):
    row, col = seat_coordinate
    seat_value = seatmap[row][col]

    if seat_value == ".":
        return "."

    neighbors = []
    for d in directions:
        new_row, new_col = row, col
        while True:
            d_row, d_col = d
            new_row, new_col = d_row + new_row, d_col + new_col
            if any([new_row < 0, new_col < 0, new_row >= len(seatmap), new_col >= len(seatmap[0])]):
                break
            if seatmap[new_row][new_col] == "L":
                break
            if seatmap[new_row][new_col] == "#":
                neighbors.append("#")
                break

    occupied_neighors = [n for n in neighbors if n == "#"]
    if seat_value == "#" and len(occupied_neighors) >= 5:
        return "L"
    elif seat_value == "L" and len(occupied_neighors) == 0:
        return "#"
    else:
        return seat_value



hashes = []
while True:
    new_seatmap = []
    for i, row in enumerate(seatmap):
        new_seatmap.append("")
        for j, seat in enumerate(row):
            new_seatmap[i] += get_desired_seat_state(seatmap, (i,j))
    new_seatmap_hash = hash(tuple(new_seatmap))
    if new_seatmap_hash in hashes:
        break
    hashes.append(new_seatmap_hash)
    seatmap = new_seatmap

occupied_seats = 0
for row in new_seatmap:
    occupied_seats += row.count("#")

print(occupied_seats)
