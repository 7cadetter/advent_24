class Guard(object):
    """
    The patrolling guard. Can move one step forward and check if they are out of bounds
    """
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return f'Guard is at {self.position} moving {self.direction}'
    
    def nightShift(self, obstacles):
        """
        The entirety of the guard's path with a certain list of obstacles
        """
        path = {}
        while not self.outOfBounds():
            # If the guard has been to a certain position, facing the same direction, it's a loop
            if (self.position[0], self.position[1]) in path:
                if self.direction in path[(self.position[0], self.position[1])]:
                    return 'loop'
                # Put the direction into the dictionary
                else:
                    path[(self.position[0], self.position[1])].append(self.direction)
            # Add the position and direction to the dictionary
            else:
                path[(self.position[0], self.position[1])] = [self.direction]

            self.move(obstacles)
        
        return path
    
    def move(self, obstacles):
        # If the guard is facing up
        if self.direction == 'up':
            # Turn right if there's an obstacle in front of guard, move if not
            if (self.position[0]-1, self.position[1]) in obstacles:
                self.direction = 'right'
            else:
                self.position[0] -= 1

        # If the guard is facing down
        elif self.direction == 'down':
            # Turn left if there's an obstacle in front of guard, move if not
            if (self.position[0]+1, self.position[1]) in obstacles:
                self.direction = 'left'
            else:
                self.position[0] += 1

        # If the guard is facing left
        elif self.direction == 'left':
            # Turn up if there's an obstacle in front of guard, move if not
            if (self.position[0], self.position[1]-1) in obstacles:
                self.direction = 'up'
            else:
                self.position[1] -= 1

        # If the guard is facing right
        elif self.direction == 'right':
            # Turn down if there's an obstacle in front of guard, move if not
            if (self.position[0], self.position[1]+1) in obstacles:
                self.direction = 'down'
            else:
                self.position[1] += 1

    def outOfBounds(self):
        # If guard is out of vertical bounds
        if self.position[0] < 0 or self.position[0] >= len(map):
            return True
        # If guard is out of horizontal bounds
        elif self.position[1] < 0 or self.position[1] >= len(map[0]):
            return True
        else:
            return False

with open('input.txt', 'r') as input:
    result = 0

    map = input.readlines()
    obstacles = []

    # Search through whole map. Add coordinates to obstacles list if obstacle found, and create guard when
    # their coordinates are found
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                obstacles.append((i, j))
            elif map[i][j] == '^':
                pos = (i, j)
                guard = Guard([pos[0], pos[1]], 'up')
    
    # Path without any added obstacles
    path = guard.nightShift(obstacles)

    # Placeholder for extra obstacle to add
    obstacles.append(0)

    for coord in path:
        added = False
        # Don't try and add obstacle in the starting position
        if coord == pos:
            continue

        # If guard will be moving upwards when facing the added obstacle
        if path[coord][0] == 'up':
            for i in range(len(obstacles) - 1):
                # If there's an obstacle in the guard's row to the right, add an obstacle in front of the guard
                if obstacles[i][0] == coord[0] + 1 and obstacles[i][1] > coord[1]:
                    obstacles[-1] = coord
                    added = True
                    break
        
        # If guard will be moving right when facing the added obstacle
        elif path[coord][0] == 'right':
            for i in range(len(obstacles) - 1):
                # If there's an obstacle in the guard's column below them, add an obstacle in front of the guard
                if obstacles[i][0] > coord[0] and obstacles[i][1] == coord[1] - 1:
                    obstacles[-1] = coord
                    added = True
                    break

        # If guard will be moving down when facing the added obstacle
        elif path[coord][0] == 'down':
            for i in range(len(obstacles) - 1):
                # If there's an obstacle in the guard's row to the left, add an obstacle in front of the guard
                if obstacles[i][0] == coord[0] - 1 and obstacles[i][1] < coord[1]:
                    obstacles[-1] = coord
                    added = True
                    break
        
        # If guard will be moving left when facing the added obstacle
        elif path[coord][0] == 'left':
            for i in range(len(obstacles) - 1):
                # If there's an obstacle in the guard's column above them, add an obstacle in front of the guard
                if obstacles[i][0] < coord[0] and obstacles[i][1] == coord[1] + 1:
                    obstacles[-1] = coord
                    added = True
                    break
        
        # If an obstacle was added, send the guard on a nightshift and see if they get stuck in a loop
        if added:
            guard = Guard([pos[0], pos[1]], 'up')
            if guard.nightShift(obstacles) == 'loop':
                result += 1
        
    print(result)