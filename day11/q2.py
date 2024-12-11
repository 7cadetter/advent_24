def blink(rocks):
    """
    Creates new list of rocks based on blinking conditions of old list
    """
    new_rocks = {}

    for rock in list(rocks.keys()):
        # If the number of digits is even, separate into two halves and put both into new dictionary
        if len(rock) % 2 == 0:
            half1 = rock[:int(len(rock)/2)]
            half2 = str(int(rock[int(len(rock)/2):])) # This gets rid of any leading 0s from half 2

            if half1 in new_rocks:
                new_rocks[half1] += rocks[rock]
            else:
                new_rocks[half1] = rocks[rock]

            if half2 in new_rocks:
                new_rocks[half2] += rocks[rock]
            else:
                new_rocks[half2] = rocks[rock]

        # If the number of digits is odd, multiply by 2024 (or change to 1 if 0)
        else:
            if rock == '0':
                if '1' in new_rocks:
                    new_rocks['1'] += rocks['0']
                else:
                    new_rocks['1'] = rocks['0']
                
            else:
                new_num = str(int(rock) * 2024)
                if new_num in new_rocks:
                    new_rocks[new_num] += rocks[rock]
                else:
                    new_rocks[new_num] = rocks[rock]
    
    return new_rocks

with open('input.txt', 'r') as text:
    line = text.read()

rocks_list = line.split()
rocks = {}

# Rock dictionary contains numbers as keys as amount of occurences as values
for rock in rocks_list:
    if rock not in rocks:
        rocks[rock] = 1
    else:
        rocks[rock] += 1

# Blink 75 times and update rocktionary
for i in range(75):
    new_rocks = blink(rocks)
    rocks = new_rocks

# Add occurences of each rock to find amount of rocks
print(sum(rocks.values()))
