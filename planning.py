from collections import deque

# Direction mappings and initial state
# Defines the possible directions and their movements.
DIRECTIONS = ['down', 'left', 'up', 'right']
MOVE_DELTA = {
    'down': (1, 0),
    'left': (0, -1),
    'up': (-1, 0),
    'right': (0, 1)
}

def parse_map(sokoban_map):
    """Parse the Sokoban map and return the robot, walls, cans, and goals."""
    robot_pos = None
    walls = set()
    cans = set()
    goals = set()

    for y, row in enumerate(sokoban_map):
        for x, char in enumerate(row):
            if char == 'X':  # Wall
                walls.add((y, x))
            elif char == '@':  # Robot starting position
                robot_pos = (y, x)
            elif char == '$':  # Can position
                cans.add((y, x))
            elif char == '.':  # Goal position
                goals.add((y, x))
            elif char == '*':  # Can on goal
                cans.add((y, x))
                goals.add((y, x))

    return robot_pos, walls, cans, goals

def is_valid_pos(pos, walls):
    """Check if a position is valid (inside the grid and not a wall)."""
    return pos not in walls

def bfs_solver(robot_pos, walls, cans, goals):
    """Solve the Sokoban puzzle using BFS and return the path of moves."""
    initial_state = (robot_pos, tuple(cans), 'down')
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        (robot, current_cans, direction), path = queue.popleft()

        if set(current_cans) == goals:  # Check if all cans are on goals
            return path


        #Moves left and right change facing direction and forward changes position + 1 towards facing direction
        for move in ['left', 'right', 'forward']:
            if move == 'left':
                new_direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]
                new_state = (robot, current_cans, new_direction)
            elif move == 'right':
                new_direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
                new_state = (robot, current_cans, new_direction)
            elif move == 'forward':
                dy, dx = MOVE_DELTA[direction]
                new_robot_pos = (robot[0] + dy, robot[1] + dx)

                if not is_valid_pos(new_robot_pos, walls):
                    continue

                # Check if the robot moves into a can
                if new_robot_pos in current_cans:
                    new_can_pos = (new_robot_pos[0] + dy, new_robot_pos[1] + dx) 

                    # If you try to push into wall or another can then skip 
                    if not is_valid_pos(new_can_pos, walls) or new_can_pos in current_cans: 
                        continue
                    # Create new state with the pushed can
                    new_cans = tuple(new_can_pos if can == new_robot_pos else can for can in current_cans)
                else:
                    #continue without change in can positions
                    new_cans = current_cans
                
                new_state = (new_robot_pos, new_cans, direction)

            if new_state not in visited:
                print("New state")
                print (new_state)
                visited.add(new_state)
                queue.append((new_state, path + [move]))

    return None  # No solution found

def solve_sokoban(sokoban_map):
    """Solve the Sokoban puzzle and return the list of directions."""
    robot_pos, walls, cans, goals = parse_map(sokoban_map)
    return bfs_solver(robot_pos, walls, cans, goals)

# Example map 
# sokoban_map = [
#     "XXXXXXX",
#     "X@  X",
#     "X X X",
#     "X $ X",
#     "X  .X",
#     "XXXXXXX"
# ]
sokoban_map = [
    "XXXXXXXXX",
    "X@      X",
    "X.X$X X X",
    "X       X",
    "X X$X X X",
    "X .     X",
    "X X X X X",
    "X*      X",
    "XXXXXXXXX"
]
# Solve the puzzle and print the set of instructions
solution = solve_sokoban(sokoban_map)
print(solution if solution else "No solution found.")

