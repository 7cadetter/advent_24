class Guard(object):
    """
    The patrolling guard. Can move one step forward and check if they are out of bounds
    """
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def __str__(self):
        return f'Guard is at {self.position} moving {self.direction}'
    
    def move(self):
        # If the guard is facing up
        if self.direction == 'up':
            # Move up, and face right if there's an obstacle in front
            self.position[0] -= 1
            if (self.position[0]-1, self.position[1]) in obstacles:
                self.direction = 'right'

        # If the guard is facing down
        elif self.direction == 'down':
            # Move down, and face left if there's an obstacle in front
            self.position[0] += 1
            if (self.position[0]+1, self.position[1]) in obstacles:
                self.direction = 'left'

        # If the guard is facing left
        elif self.direction == 'left':
            # Move left, and face up if there's an obstacle in front
            self.position[1] -= 1
            if (self.position[0], self.position[1]-1) in obstacles:
                self.direction = 'up'

        # If the guard is facing right
        elif self.direction == 'right':
            # Move right, and face down if there's an obstacle in front
            self.position[1] += 1
            if (self.position[0], self.position[1]+1) in obstacles:
                self.direction = 'down'

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
    map = input.readlines()
    obstacles = []
    path = []

    # Search through whole map. Add coordinates to obstacles list if obstacle found, and create guard when
    # their coordinates are found
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '#':
                obstacles.append((i, j))
            elif map[i][j] == '^':
                guard = Guard([i, j], 'up')
        
    while not guard.outOfBounds():
            # Add the guard's position to the path list, and move the guard
            if (guard.position[0], guard.position[1]) not in path:
                path.append((guard.position[0], guard.position[1]))
            guard.move()
    
    print(len(path))
