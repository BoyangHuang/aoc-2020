import typing as T

import re
from dataclasses import dataclass


operation_dict = {
    "X": lambda bit: bit,
    "1": lambda _: "1",
    "0": lambda _: "0",
}

operation_dict_memory = {
    "X": lambda _: "X",
    "1": lambda _: "1",
    "0": lambda bit: bit,
}


def populate_memory(memory_string, value_to_write, memory_result):
    if "X" not in memory_string:
        memory_result[int(memory_string,2)] = value_to_write
    else:
        populate_memory(memory_string.replace("X", "1", 1), value_to_write, memory_result),
        populate_memory(memory_string.replace("X", "0", 1), value_to_write, memory_result),


@dataclass
class Instruction:
    mask: str
    operations: T.List[T.Tuple[str, str]]

    def _process_memory(self, memory_value):
        bitstring = f"{int(memory_value):036b}"
        processed_bitstring = ""
        for i, c in enumerate(self.mask):
            bit_operation = operation_dict_memory[c]
            processed_bitstring += bit_operation(bitstring[i])
        return processed_bitstring

    def _process_instruction(self, value):
        bitstring = f"{int(value):036b}"
        processed_bitstring = ""
        for i, c in enumerate(self.mask):
            bit_operation = operation_dict[c]
            processed_bitstring += bit_operation(bitstring[i])
        return int(processed_bitstring, base=2)

    def process_instructions(self):
        memories = {}
        for operation in self.operations:
            memory, value = operation
            memories[memory] = self._process_instruction(value)
        return memories

    def process_instructions_v2(self):
        memories = {}
        for operation in self.operations:
            memory, value = operation
            memory_string = self._process_memory(memory)
            populate_memory(memory_string, int(value), memories)
        return memories


instructions = []
with open("input.txt", mode="r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        if re.match(r"mask = [X10]{36}", line):
            current_mask = line.split()[2]
            instructions.append(Instruction(mask=current_mask, operations=[]))

        else:
            op = re.match(r"mem\[(\d*)\]", line)[1]
            decimal = line.split()[2]
            instructions[-1].operations.append((op, decimal))


memory_addresses = {}
for instr in instructions:
    memory_addresses.update(instr.process_instructions_v2())

print(memory_addresses)
print(sum(memory_addresses.values()))
