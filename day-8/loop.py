
instructions = []
# visited_instructions = []

with open("input.txt", mode="r", newline="\n") as f:
    for i, line in enumerate(f.readlines()):
        instr, acc = line.split()
        instructions.append((instr, int(acc), i))


def change_destiny(starting_instruction, visited_instructions):
    try:
        print("changing destiny for ", starting_instruction)
        execute_instructions(starting_instruction,0, visited_instructions, destiny=False)
    except IndexError:
        print('flipping TO this instruction caused a index error', starting_instruction)
        exit()


def execute_instructions(starting_instruction, accumulation, visited_instructions, destiny):
    if starting_instruction in visited_instructions:
        return accumulation
    visited_instructions.append(starting_instruction)
    instr, acc, index = starting_instruction
    try:
        if instr == "nop":
            if destiny:
                print("I WAS: ", starting_instruction)
                change_destiny(("jmp", acc, index), [*visited_instructions,])
            new_instruction = instructions[index + 1]
            accumulation = execute_instructions(new_instruction, accumulation, visited_instructions, destiny)

        elif instr == "acc":
            new_instruction = instructions[index + 1]
            accumulation = execute_instructions(new_instruction, accumulation + acc, visited_instructions, destiny)

        elif instr == "jmp":
            if destiny:
                change_destiny(("nop", acc, index), [*visited_instructions,])
            new_instruction = instructions[index + acc]
            accumulation = execute_instructions(new_instruction, accumulation, visited_instructions, destiny)
    except IndexError:
        if instr == "acc":
            return accumulation + acc
        return accumulation
    return accumulation


accumulator = 0
curr_instruction = instructions[0]
acc = execute_instructions(curr_instruction, 0, [], False)
print(acc)


#
# while curr_instruction not in visited_instructions:
#     visited_instructions.append(curr_instruction)
#     instr, acc, index = curr_instruction
#     try:
#         if instr == "nop":
#             curr_instruction = instructions[index + 1]
#             continue
#
#         if instr == "acc":
#             accumulator += acc
#             curr_instruction = instructions[index + 1]
#             continue
#
#         if instr == "jmp":
#             curr_instruction = instructions[index + acc]
#             print(instr, acc, index)
#             continue
#     except IndexError:
#         print(accumulator, curr_instruction, acc)
#
# print(curr_instruction in visited_instructions)
# print("the step that was repeated:", curr_instruction)
# print(len(instructions))
# print(accumulator)
