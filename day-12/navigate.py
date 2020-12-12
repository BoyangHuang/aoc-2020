import typing as T

from dataclasses import dataclass


navigation_instructions = []
turn_table = { # array is clockwise (L), reverse array counter clockwise (R)
    "east": ["north", "west", "south"],
    "west": ["south", "east", "north"],
    "north": ["west", "south", "east"],
    "south": ["east", "north", "west"],
}


@dataclass
class Ship:
    east: int = 0
    west: int = 0
    north: int = 0
    south: int = 0
    current_direction: str = "east"

    def turn(self, direction, units):
        turn_array = turn_table[self.current_direction]
        if direction == "L":
            if units == 90:
                self.current_direction = turn_array[0]
            elif units == 180:
                self.current_direction = turn_array[1]
            elif units == 270:
                self.current_direction = turn_array[2]
        elif direction == "R":
            if units == 90:
                self.current_direction = turn_array[2]
            elif units == 180:
                self.current_direction = turn_array[1]
            elif units == 270:
                self.current_direction = turn_array[0]

    def move(self, instr: T.Tuple[str, int]):
        action, units = instr
        if action == "E":
            self.east += units
        elif action == "W":
            self.west += units
        elif action == "N":
            self.north += units
        elif action == "S":
            self.south += units
        elif action in ("L", "R"):
            self.turn(action, units)
        elif action == "F":
            self.__setattr__(self.current_direction, self.__getattribute__(self.current_direction) + units)

    @property
    def east_west(self):
        return self.east - self.west

    @property
    def north_south(self):
        return self.north - self.south

    def __repr__(self):
        return f"east: {self.east}, west: {self.west}, north: {self.north}, south: {self.south}, current_direction: {self.current_direction}, manhattan distance:{abs(self.east - self.west) + abs(self.north - self.south)}"


@dataclass
class Waypoint:
    ship: Ship
    east_west: int = 10
    north_south: int = 1

    def _turn_90(self, direction):
        if direction == "L":
            self.east_west, self.north_south = self.north_south * -1, self.east_west
        elif direction == "R":
            self.east_west, self.north_south = self.north_south,  self.east_west * -1

    def turn(self, direction, units):
        number_of_turns = units // 90
        for _ in range(number_of_turns):
            self._turn_90(direction)

    def move(self, instr: T.Tuple[str, int]):
        action, units = instr
        if action == "E":
            self.east_west += units
        elif action == "W":
            self.east_west -= units
        elif action == "N":
            self.north_south += units
        elif action == "S":
            self.north_south -= units
        elif action in ("L", "R"):
            self.turn(action, units)
        elif action == "F":
            move_instructions = []
            if self.east_west > 0:
                move_instructions.append(("E", self.east_west * units))
            elif self.east_west < 0:
                move_instructions.append(("W", abs(self.east_west) * units))

            if self.north_south > 0:
                move_instructions.append(("N", self.north_south * units))
            elif self.north_south < 0:
                move_instructions.append(("S", abs(self.north_south) * units))

            for move_instruction in move_instructions:
                self.ship.move(move_instruction)


with open("input.txt", mode="r") as f:
    for i, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        navigation_instructions.append((line[0], int(line[1:])))

ship_1 = Ship()
for instruction in navigation_instructions:
    ship_1.move(instruction)

print("RESULT FOR PART 1: ", ship_1)

ship = Ship()
waypoint = Waypoint(ship=ship)
for instruction in navigation_instructions:
    waypoint.move(instruction)

print("RESULT FOR PART 2: ", waypoint.ship)

