jolts = {}

with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.readlines()):
        jolts[int(line)] = []

jolts = sorted(jolts)
my_device = max(jolts)

def remove_from_list(some_list, value):
    ret = [x for x in some_list if x != value]
    return ret


# def explore_jolt_tree(jolt_list, jolt_value, ones, threes):
#     print(jolt_list, jolt_value, my_device)
#
    # if len(jolt_list) == 0 and my_device <= jolt_value < my_device + 3:
    #     print(ones, threes)
    #     return True, ones, threes
    # elif len(jolt_list) == 0:
    #     return False, ones, threes
    # jolt_1, jolt_2, jolt_3 = jolt_value + 1, jolt_value + 2, jolt_value + 3
    # # jolt_less_1, jolt_less_2, jolt_less_3 = jolt_value - 1, jolt_value - 2, jolt_value - 3
    # if jolt_1 in jolt_list:
    #     success, one_res, three_res = explore_jolt_tree(remove_from_list(jolt_list, jolt_1), jolt_1, ones+1, threes)
    #     if success:
    #         return success, one_res, three_res
    # if jolt_2 in jolt_list:
    #     success, one_res, three_res  = explore_jolt_tree(remove_from_list(jolt_list, jolt_2), jolt_2, ones, threes)
    #     if success:
    #         return success, one_res, three_res
    # if jolt_3 in jolt_list:
    #     success, one_res, three_res  = explore_jolt_tree(remove_from_list(jolt_list, jolt_3), jolt_3, ones, threes+1)
    #     if success:
    #         return success, one_res, three_res

jolt_cache = {}

def explore_jolt_tree_part_2(jolt_list, jolt_value, valid_count):
    if my_device <= jolt_value < my_device + 3:
        return 1

    if jolt_value in jolt_cache:
        return jolt_cache[jolt_value]

    jolt_1, jolt_2, jolt_3 = jolt_value + 1, jolt_value + 2, jolt_value + 3

    if jolt_1 in jolt_list:
        valid_count += explore_jolt_tree_part_2(remove_from_list(jolt_list, jolt_1), jolt_1, valid_count)

    if jolt_2 in jolt_list:
        valid_count += explore_jolt_tree_part_2(remove_from_list(jolt_list, jolt_2), jolt_2, valid_count)

    if jolt_3 in jolt_list:
        valid_count +=  explore_jolt_tree_part_2(remove_from_list(jolt_list, jolt_3), jolt_3, valid_count)

    jolt_cache[jolt_value] = valid_count
    return valid_count


print(explore_jolt_tree_part_2(jolts, 0, 0))
