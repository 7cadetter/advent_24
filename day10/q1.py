def search(head, count, peaks, map):
    """
    Recursive function to search in all directions from a coordinate for a number 1 bigger than itself
    """

    # If you found a 9, add it to the list of peaks
    if count == 9:
        peaks.add(head)
    else:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for drct in directions:
            new_i = head[0] + drct[0]
            new_j = head[1] + drct[1]

            # For each direction, move one space and unless it's out of bounds, call the same function on
            # that space. It will run til it reaches a 9
            if new_i < 0 or new_i >= len(map) or new_j < 0 or new_j >= len(map[0]):
                continue
            elif int(map[new_i][new_j]) == count + 1:
                search((new_i, new_j), count + 1, peaks, map)
    
    return peaks
            


with open('input.txt', 'r') as text:
    map = text.readlines()
    map = [line.strip() for line in map]

trailheads = []

# Add each trailhead position to a list
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == '0':
            trailheads.append((i, j))

result = 0
# Search for 9s from each trailhead in the list and add the amount of trails to the result
for head in trailheads:
    result += len(search(head, 0, set(), map))

print(result)