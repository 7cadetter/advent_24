def onBoard(pos):
    """
    Check if a position is in the bounds of the map
    """
    if pos[0] < 0 or pos[0] >= len(map):
        return False
    elif pos[1] < 0 or pos[1] >= len(map[0]):
        return False
    else:
        return True

with open('input.txt', 'r') as text:
    map = text.readlines()
    antennae = {}
    antinodes = set({})

    for i in range(len(map)):
        # Get rid of \n
        map[i] = map[i].strip()

        # Unless the character is '.', enter it as a key and its position as a value
        for j in range(len(map[0])):
            if map[i][j] != '.':
                if map[i][j] not in antennae:
                    antennae[map[i][j]] = {(i, j)}
                else:
                    antennae[map[i][j]].add((i, j))

    # For each antenna, check the distance to each other antenna of the same type, and place an antinode
    # the same distance away from the other antenna
    for a in antennae:
        for pos in antennae[a]:
            for other_pos in antennae[a]:
                if other_pos == pos:
                    continue
                else:
                    i = pos[0] - other_pos[0]
                    j = pos[1] - other_pos[1]

                    anti_pos = (other_pos[0] - i, other_pos[1] - j)

                    if onBoard(anti_pos) and anti_pos not in antinodes:
                        antinodes.add(anti_pos)
    
    print(len(antinodes))