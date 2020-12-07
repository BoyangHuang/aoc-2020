from collections import defaultdict

bag_dict = defaultdict(dict)

def clean_bag_string(bag_str):
    return bag_str.replace(".", "").replace(" bags", "").replace(" bag", "").strip()


def includes_gold_bag(contained_bag_dict):
    gold_bag_bool_list = [False]
    for inner_bag_name, inner_bag_count in contained_bag_dict.items():
        if inner_bag_name == "shiny gold":
            return True
        if inner_bag_name == "other":
            continue
        next_bag_dict = bag_dict.get(inner_bag_name)
        gold_bag_bool_list.append(includes_gold_bag(next_bag_dict))

    if any(gold_bag_bool_list):
        return True
    return False


def nested_bag_count(contained_bag_dict):
    total_bag_count = 0
    for inner_bag_name, inner_bag_count in contained_bag_dict.items():
        if inner_bag_name == "other":
            continue
        next_bag_dict = bag_dict.get(inner_bag_name)
        total_bag_count += nested_bag_count(next_bag_dict) * int(inner_bag_count) + int(inner_bag_count)
    return total_bag_count


with open("input.txt", mode="r", newline="\n") as f:
    for line in f.readlines():
        bag_string = line.split("contain")
        bag_key = clean_bag_string(bag_string[0])
        bag_values = bag_string[1].split(",")
        for bag_value in bag_values:
            deconstructed_bag_value= bag_value.split()
            count = deconstructed_bag_value[0]
            name = clean_bag_string(" ".join(deconstructed_bag_value[1:]))
            bag_dict[bag_key][name] = count

answer_1 = 0
for k, v in bag_dict.items():
    if includes_gold_bag(v):
        answer_1 += 1
print("ANSWER 1:", answer_1)

gold_bag_dict = bag_dict["shiny gold"]
print("ANSWER 2:", nested_bag_count(gold_bag_dict))
