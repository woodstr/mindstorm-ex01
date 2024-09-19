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

workaround_extra_forward_indexes = []

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
                
                new_state = (new_robot_pos, new_cans, direction )

            if new_state not in visited:
                # print("New state")
                # print (new_state)
                visited.add(new_state)
                workaround_extra_forward_indexes.append(len(path))
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
# sokoban_map = [
#     "XXXXXXXXX",
#     "X@      X",
#     "X.X$X X X",
#     "X       X",
#     "X X$X X X",
#     "X .     X",
#     "X X X X X",
#     "X*      X",
#     "XXXXXXXXX"
# ]

sokoban_map = [
    "XXXXXXX",
    "X.@ X X",
    "X$* $ X",
    "X   $ X",
    "X ..  X",
    "X  *  X",
    "XXXXXXX"
]

initial_real_map = [
    "XXXXXX", 
    "X    X", 
    "X    X",    
    "X    X",
    "X    X",
    "XXXXXX"
]

test1_real_map = [
    "XXXXXX", 
    "X.@  X", 
    "X    X",    
    "X$   X",
    "X    X",
    "XXXXXX"
]

test2_real_map = [
    "XXXXXXXXX",
    "X@     .X",
    "X X X X X",
    "X  $    X", 
    "X X X X X",
    "X. $    X",
    "X X X X X",
    "X  $   .X",
    "XXXXXXXXX"
]

test3_real_map = [
    "XXXXXXXXX",
    "X@      X",
    "X X X X X",
    "X. $    X",
    "X X X X X",
    "X  $   .X",
    "X X X X X",
    "X*      X",
    "XXXXXXXXX"
]

test4_real_map = [
    "XXXXXXXXX",
    "X@     .X",
    "X X X X X",
    "X  * * $X",
    "X X X X X",
    "X  $   .X",
    "X X X X X",
    "X       X",
    "XXXXXXXXX"
]

test5_real_map = [
    "XXXXXXXXX",
    "X@     .X",
    "X X X X X",
    "X      $X",
    "X X X X X",
    "X  $   .X",
    "X X X X X",
    "X       X",
    "XXXXXXXXX"
]

test6_real_map = [
    "XXXXXXXXX",
    "X@   $ .X",
    "X X X X X",
    "X$      X",
    "X X X X X",
    "X  $   .X",
    "X X X X X",
    "X. $   .X",
    "XXXXXXXXX"
]

# Solve the puzzle and print the set of instructions
solution = solve_sokoban(test2_real_map)
print()
print(solution)
print()



# Format the solution!

# Remove first forward as robot starts at the intersection
if solution[0] == 'forward':
    solution = solution[1:]

solution = solution + [None]  # Add padding to prevent out of index error

# First replace the consecutive left or right moves with a single 180 degree turn
for idx, move in enumerate(solution):
    # If the move is None, skip it as we have already processed it
    if move == None:
        continue

    elif move in ['left', 'right'] and solution[idx + 1] == move:
        solution[idx] = '180'
        solution[idx + 1] = None
solution = [move for move in solution if move is not None] # remove Nones from the list
print(solution)
print()

solution = solution + [None]*5  # Add padding to prevent out of index error
# Then, format left and right turns.
# Our robots left turns are the same as [left, forward, forward]
# Our robots right turns are the same as [right, forward, forward]
for idx, move in enumerate(solution):
    # If the move is None, skip it as we have already processed it
    if move == None:
        continue

    elif move == 'left' and [solution[idx+1], solution[idx+2]] == ['forward', 'forward']:
        solution[idx+1] = None
        solution[idx+2] = None
    elif move == 'right' and [solution[idx+1], solution[idx+2]] == ['forward', 'forward']:
        solution[idx+1] = None
        solution[idx+2] = None
solution = [move for move in solution if move is not None] # remove Nones from the list
print(solution)
print()

solution = solution + [None]*5  # Add padding to prevent out of index error
# Then get rid of extra forward after a 180
for idx, move in enumerate(solution):
    # If the move is None, skip it as we have already processed it
    if move == None:
        continue

    elif move == '180' and solution[idx + 1] == 'forward':
        solution[idx + 1] = None
solution = [move for move in solution if move is not None] # remove Nones from the list
print(solution)
print()

# Then get rid of extra forwards on consecutive forwards
# # Count number of moves, if 6 or 5 reduce to 3, if 3 or 4 reduce to 2, if 1 or 2 reduce to 1
formatted_solution = []
solution = solution + [None]*5  # Add padding to prevent out of index error
for idx, move in enumerate(solution):
    # If the move is None, skip it as we have already processed it
    if move == None:
        continue

    elif move == 'forward':
        # if 6 forwards, then reduce to 2
        if [solution[idx+1], solution[idx+2], solution[idx+3], solution[idx+4], solution[idx+5]] == ['forward', 'forward', 'forward', 'forward', 'forward']:
            # add moves to formatted solution and delete remaining forwards from next checks
            formatted_solution = formatted_solution + ['forward']*2
            solution[idx+1] = None
            solution[idx+2] = None
            solution[idx+3] = None
            solution[idx+4] = None
            solution[idx+5] = None
        # if 5 forwards, reduce to 2
        elif [solution[idx+1], solution[idx+2], solution[idx+3], solution[idx+4]] == ['forward', 'forward', 'forward', 'forward']:
            formatted_solution = formatted_solution + ['forward']*2
            solution[idx+1] = None
            solution[idx+2] = None
            solution[idx+3] = None
            solution[idx+4] = None
        # if 4 forwards, reduce to 2
        elif [solution[idx+1], solution[idx+2], solution[idx+3]] == ['forward', 'forward', 'forward']:
            formatted_solution = formatted_solution + ['forward']*2
            solution[idx+1] = None
            solution[idx+2] = None
            solution[idx+3] = None
        # if 3 forwards, reduce to 1 (unless we just made a turn! then reduce to 2)
        elif [solution[idx+1], solution[idx+2]] == ['forward', 'forward']:
            if formatted_solution and formatted_solution[-1] in ['left', 'right']:
                formatted_solution = formatted_solution + ['forward']*2
                solution[idx+1] = None
                solution[idx+2] = None
            else:
                formatted_solution.append('forward')
                solution[idx+1] = None
                solution[idx+2] = None

        # if 2 forwards, reduce to 1
        elif solution[idx+1] == 'forward':
            formatted_solution.append('forward')
            solution[idx+1] = None
        # if 1 forward, reduce to 1
        elif move == 'forward':
            formatted_solution.append('forward')
    # if move was no a forward then just add it
    else:
        formatted_solution.append(move)

# Remove first left and print placement message if first move is left
if formatted_solution[0] == 'left':
    formatted_solution = formatted_solution[1:]
    print("Place robot facing left!!!")

print(formatted_solution)