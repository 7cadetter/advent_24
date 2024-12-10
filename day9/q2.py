with open('input.txt', 'r') as text:
    result = 0
    line = text.read()
    line = [int(i) for i in line]
    
    memory = []
    mem_length = {}
    spaces = {}

    id = 0
    # Append the ID to the memory the amount of times that the numbers indicate, and then the spaces
    # the same way. For each id, add it to the mem_length dictionary with its number of appearance
    # and its index. For each space, add it to the spaces dictionary with its index
    for i in range(0, len(line), 2):
        mem_length[id] = (line[i], len(memory))
        for j in range(line[i]):
            memory.append(id)
        
        if i+1 < len(line) and line[i+1] > 0:
            if line[i+1] in spaces:
                spaces[line[i+1]].append(len(memory))
            else:
                spaces[line[i+1]] = [len(memory)]
            for j in range(line[i+1]):
                memory.append('.')

        id += 1

    # Go through each memory block backwards, and dind the left-most position where there is a space 
    # that can fit that block.
    for i in range(len(mem_length)-1, 0, -1):
        smallest = mem_length[i][1]
        for space in sorted(list(spaces.keys())):
            # If the space is bigger and further left than the memory block 
            if space >= mem_length[i][0] and spaces[space][0] < mem_length[i][1]:
                if spaces[space][0] < smallest:
                    smallest = spaces[space][0]
                    sp_count = space

        # If there was a valid space to move the block to
        if smallest != mem_length[i][1]:
            for count in range(mem_length[i][0]):
                # Change the space to the memory block and the memory block to space
                memory[smallest + count] = i
                memory[mem_length[i][1] + count] = '.'
            
            mem_size = mem_length[i][0]

            # If there's leftover space after inserting the memory block, add the new position of the 
            # leftover space to the spaces dictionary and re-sort it
            if mem_size < sp_count:
                if sp_count - mem_size in spaces:
                    spaces[sp_count - mem_size].append(spaces[sp_count][0] + mem_size)
                else:
                    spaces[sp_count - mem_size] = [spaces[sp_count][0] + mem_size]
                spaces[sp_count - mem_size].sort()
            
            # Remove the space that was used from spaces and delete the key if there's no more spaces
            # of that size
            spaces[sp_count].pop(0)
            if len(spaces[sp_count]) == 0:
                del spaces[sp_count]

    # Add all numbers multiplied by their indices
    for i in range(len(memory)):
        if memory[i] == '.':
            continue
        
        result += int(memory[i]) * i

    print(result)