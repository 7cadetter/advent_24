def search(pos, region, edges, map,):
    """
    Recursive function to search through a certain region in the map and add up the edges of all of its plots
    """
    letter = map[pos[0]][pos[1]]
    region.add(pos)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Check each direction from each node
    for drct in directions:
        # Assign the new position
        new_i = pos[0] + drct[0]
        new_j = pos[1] + drct[1]

        # If the new position is out of bounds, it's an edge
        if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]):
            edges += 1
        # If the new position is the same letter as the region, search in that new position
        elif map[new_i][new_j] == letter:
            if (new_i, new_j) not in region:
                region, edges = search((new_i, new_j), region, edges, map)
        # If the new position is a different letter, it's an edge
        else:
            edges += 1
    
    return region, edges

with open('input.txt', 'r') as text:
    map = text.readlines()
    map = [line.strip() for line in map]

# Regions is a dictionary with letters as its keys. The value for each key is a list of 
# regions of that letter (in the form of sets). Since each plot is represented by a tuple coordinate, regions
# is a dictionary of lists of sets of tuples
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
        
        # If it's a new region, search for all of its plot and the number of its edges
        if unique:
            region, reg_edges = search((i, j), set(), 0, map) 

            # Value is the number of edges times the amount of plots (area) in a region
            regions[map[i][j]].append(region)
            value = len(region) * reg_edges
            total += value


print(total)