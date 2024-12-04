def mas(line1, line2, line3, j):
    """
    Check if there's two 'MAS's in any direction making an X shape, starting from a certain index
    """
    # If it spells MAS going down and right
    if line1[j] == 'M' and line2[j+1] == 'A' and line3[j+2] == 'S':

        # If it spells MAS going down and left, or going up and right
        if line1[j+2] == 'M' and line3[j] == 'S':
            return True
        elif line1[j+2] == 'S' and line3[j] == 'M':
            return True
        
    # If it spells MAS going up and left
    elif line1[j] == 'S' and line2[j+1] == 'A' and line3[j+2] == 'M':

        # If it spells MAS going down and left, or going up and right
        if line1[j+2] == 'M' and line3[j] == 'S':
            return True
        elif line1[j+2] == 'S' and line3[j] == 'M':
            return True
        
    # There's no X - MAS
    else:
        return False

with open('input.txt', 'r') as input:
    text = input.readlines()
    count = 0

    for i in range(len(text) - 2):
        # Strip \n from line
        text[i] = text[i].strip()

        for j in range(len(text[i]) - 2):

            # Top left of the X - MAS
            if text[i][j] == 'M' or text[i][j] == 'S':
                if mas(text[i], text[i+1], text[i+2], j):
                    count += 1

print(count)