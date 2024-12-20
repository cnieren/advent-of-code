from enum import Enum
import os

class Direction(Enum):
    NONE = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    @classmethod
    def from_string(cls, char):
        if char == '^':
            return cls.NORTH
        if char == '>':
            return cls.EAST
        if char == '<':
            return cls.WEST
        if char == 'v':
            return cls.SOUTH
        return cls.NONE

class ActorType(Enum):
    EMPTY = 1
    OBJECT = 2 
    GUARD = 3
    VISTED = 4

    @classmethod
    def from_string(cls, char):
        if char == '.':
            return cls.EMPTY
        if char == '#':
            return cls.OBJECT
        if char in ['^', '>', '<', 'v']:
            return cls.GUARD

class Node:
    def __init__(self, x: int, y: int, actor_type: ActorType, direction: Direction):
        self.x = x
        self.y = y
        self.actor_type = actor_type
        self.direction = direction

    def visit(self):
        self.actor_type = ActorType.VISTED

    def get_actor_type(self):
        return self.actor_type

    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

    def turn(self):
        if self.direction == Direction.NORTH:
            self.direction = Direction.EAST
            return
        if self.direction == Direction.EAST:
            self.direction = Direction.SOUTH
            return
        if self.direction == Direction.SOUTH:
            self.direction = Direction.WEST
            return
        if self.direction == Direction.WEST:
            self.direction = Direction.NORTH
            return

    def __str__(self):
        if self.actor_type == ActorType.EMPTY:
            return '.'
        if self.actor_type == ActorType.OBJECT:
            return '#'
        if self.actor_type == ActorType.VISTED:
            return 'X'
        if self.actor_type == ActorType.GUARD:
            if self.direction == Direction.NORTH:
                return '^'
            if self.direction == Direction.EAST:
                return '>'
            if self.direction == Direction.SOUTH:
                return 'v'
            if self.direction == Direction.WEST:
                return '<'

class Lab:
    def __init__(self, floor):
        self.map = floor
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j].actor_type == ActorType.GUARD:
                    self.guard_x = i
                    self.guard_y = j
                    break
    
    def get_next_node(self, x: int, y: int, direction: Direction):
        if direction == Direction.NORTH:
            if x - 1 < 0:
                return None
            return self.map[x-1][y]
        
        if direction == Direction.EAST:
            if y + 1 >= len(self.map[0]):
                return None
            return self.map[x][y+1]

        if direction == Direction.SOUTH:
            if x + 1 >= len(self.map[0]):
                return None
            return self.map[x+1][y]

        if direction == Direction.WEST:
            if y - 1 < 0:
                return None
            return self.map[x][y-1]

    def move_guard(self):
        next_node = self.get_next_node(self.guard_x, self.guard_y, self.map[self.guard_x][self.guard_y].direction)

        if not next_node:
            # We found the exit
            return None
        else:
            self.map[self.guard_x][self.guard_y].visit()

            next_type = next_node.get_actor_type()

            if next_type == ActorType.OBJECT:
                self.map[self.guard_x][self.guard_y].turn()
                next_node = self.get_next_node(self.guard_x, self.guard_y, self.map[self.guard_x][self.guard_y].direction)

                if not next_node:
                    # We found the exit
                    return None

            next_node.actor_type = ActorType.GUARD
            next_node.direction = self.map[self.guard_x][self.guard_y].direction
            self.guard_x = next_node.x
            self.guard_y = next_node.y

        return True

    def count_moves(self):
        count = 0
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.map[i][j].actor_type == ActorType.VISTED:
                    count += 1
        return count + 1;

    def __str__(self):
        result = ""
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                result += str(self.map[i][j])
            result += "\n"
        return result;


filename = 'input.txt'
data = []

if not os.path.isfile(filename):
    print(f'File: {filename} -- Not Found')
    exit()

with open(filename) as filep:
    i = 0
    for line in filep:
        obs = []
        # Read file here
        j = 0

        for char in list(line.strip()):
            actor_type = ActorType.from_string(char)
            obs.append(Node(i, j, actor_type, Direction.from_string(char)))
            j += 1

        data.append(obs)
        i += 1

lab = Lab(data)
while lab.move_guard():
    continue
print(lab)
print()
print(lab.count_moves())
