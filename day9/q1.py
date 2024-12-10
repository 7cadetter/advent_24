def isContig(memory):
    """
    Check if memory is conitguous with no spaces between memory
    """
    space = False
    for i in memory:
        if not space and i == '.':
            space = True
        
        # If the space started and you find another number, it's not contiguous
        elif space and i != '.':
            return False
    return True

with open('input.txt', 'r') as text:
    result = 0
    line = text.read()
    
    memory = []

    id = 0

    # Append the ID to the memory the amount of times that the numbers indicate, and then the spaces
    # the same way
    for i in range(0, len(line), 2):
        for j in range(int(line[i])):
            memory.append(id)
        
        if i+1 < len(line):
            for j in range(int(line[i+1])):
                memory.append('.')
        
        id += 1

    # Go backward through memory and switch the number with the first space in the memory
    for i in range(len(memory)-1, 0, -1):
        if memory[i] != '.':
            memory[memory.index('.')] = memory[i]
            memory[i] = '.'
            if isContig(memory):
                break

    # Add all numbers multiplied by their index to result until you get to the spaces
    for i in range(len(memory)):
        if memory[i] == '.':
            break
        
        result += int(memory[i]) * i

    print(result)


    
    
