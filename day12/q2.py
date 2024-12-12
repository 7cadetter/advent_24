directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def isInside(region, other):
    """
    Check if a region is completely inside another region. It doesn't work.
    """

    # If the region is bigger than the other one, it can't be inside it
    if len(region) > len(other):
        return False
    
    # If it's the same region, ignore
    elif region == other:
        return False
    
    # If every plot in the inner region is surrounded by only the same letters and the letters of the outer
    # region, it's surrounded. Looking back, this is obviously NOT true.
    for plot in region:
        for drct in directions:
            if (plot[0] + drct[0], plot[1] + drct[1]) not in region \
            and (plot[0] + drct[0], plot[1] + drct[1]) not in other:
                return False

    return True
        

def search(pos, region, map,):
    """
    Recursive function to search through a certain region in the map and add up the edges of all of its plots
    """
    letter = map[pos[0]][pos[1]]
    region.add(pos)

    # Check each direction from each node
    for drct in directions:
        new_i = pos[0] + drct[0]
        new_j = pos[1] + drct[1]

        # If the new position is out of bounds, ignore it
        if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]):
            continue
        # If the new position is the same letter as the region, search in that new position
        elif map[new_i][new_j] == letter:
            if (new_i, new_j) not in region:
                region = search((new_i, new_j), region, map)
    
    return region

def followWall(pos, map):
    """
    Follow the perimeter of the region and recognise a line when you turn
    """
    x = pos[1]
    y = pos[0]
    letter = map[y][x]
    lines = 0
    i = 0

    # Keep going until you're where you started, facing the same direction
    while pos != (y, x) or i != 0 or lines == 0:
        # If the plot in front of you is out of bounds, turn clockwise and add 1 to lines
        if y + directions[i][0] == len(map) or y + directions[i][0] == -1 \
        or x + directions[i][1] == len(map[0]) or x + directions[i][1] == -1:
            i = (i + 1) % 4
            lines += 1
        # If the plot in front of you is not the same letter, turn clockwise and add 1 to lines
        elif map[y + directions[i][0]][x + directions[i][1]] != letter:
            i = (i + 1) % 4
            lines += 1
        else:
            # Move forward
            y += directions[i][0]
            x += directions[i][1]

            # If you are not along the wall anymore, turn anti-clockwise and add 1 to lines
            if y + directions[i-1][0] != len(map) and y + directions[i-1][0] != -1 and x + directions[i-1][1] != len(map[0]) \
            and x + directions[i-1][1] != -1 and map[y + directions[i-1][0]][x + directions[i-1][1]] == letter:
                i = (i - 1) % 4
                lines += 1

    return lines


with open('input.txt', 'r') as text:
    map = text.readlines()
    map = [line.strip() for line in map]

regions = {}
total = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        unique = True

        # If it's not in the list, add an empty list just to append it to
        if map[i][j] not in regions:
            regions[map[i][j]] = []

        # If the plot is already in a region in the list, ignore it because it's been added already
        for area in regions[map[i][j]]:
            if (i, j) in area:
                unique = False
                break
        # If it's a new region, get the number of lines in it and all of its plots
        if unique:
            lines = followWall((i, j), map)
            region = search((i, j), set(), map)
            regions[map[i][j]].append(region)

            # Go through all the letters in the map
            for letter in regions:
                # Skip current letter
                if letter == map[i][j]:
                    continue
                # For each region of each letter, check if the current region is inside that region. If
                # it's inside, treat this region's lines as that region's (since they would count as interior
                # lines for that region)
                for area in regions[letter]:
                    if isInside(region, area):
                        total += lines * len(area)
            total += lines * len(region)

print(total)