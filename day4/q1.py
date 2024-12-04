def forward(line, i):
    """
    Check if a substring spells 'MAS' going forward from a certain index
    """
    if line[i+1] == 'M' and line[i+2] == 'A' and line[i+3] == 'S':
        return True
    else:
        return False
    
def backward(line, i):
    """
    Check if a substring spells 'MAS' going backwards from a certain index
    """
    if line[i-1] == 'M' and line[i-2] == 'A' and line[i-3] == 'S':
        return True
    else:
        return False
    
def up_down(line1, line2, line3, i):
    """
    Check if a substring spells 'MAS' going up or down from a certain index
    """
    if line1[i] == 'M' and line2[i] == 'A' and line3[i] == 'S':
        return True
    else:
        return False
    
def diag_right(line1, line2, line3, i):
    """
    Check if a substring spells 'MAS' going diagonally right from a certain index
    """
    if line1[i+1] == 'M' and line2[i+2] == 'A' and line3[i+3] == 'S':
        return True
    else:
        return False
    
def diag_left(line1, line2, line3, i):
    """
    Check if a substring spells 'MAS' going diagonally left from a certain index
    """
    if line1[i-1] == 'M' and line2[i-2] == 'A' and line3[i-3] == 'S':
        return True
    else:
        return False



with open('input.txt', 'r') as input:
    text = input.readlines()
    count = 0

    for i in range(len(text)):
        # Strip \n from line
        text[i] = text[i].strip()

        for j in range(len(text[i])):
            # Find an X
            if text[i][j] == 'X':

                # If there's room on the right to spell XMAS forwards
                if j < len(text[i]) - 3:
                    if forward(text[i], j):
                        count += 1
                    # If there's room to spell XMAS diagonally (up and right)
                    if i > 2:
                        if diag_right(text[i-1], text[i-2], text[i-3], j):
                            count += 1
                    # If there's room to spell XMAS diagonally (down and right)
                    if i < len(text) - 3:
                        if diag_right(text[i+1], text[i+2], text[i+3], j):
                            count += 1

                # If there's room on the left to spell XMAS backwards
                if j > 2:
                    if backward(text[i], j):
                        count += 1
                    # If there's room to spell XMAS diagonally (up and left)
                    if i > 2:
                        if diag_left(text[i-1], text[i-2], text[i-3], j):
                            count += 1
                    # If there's room to spell XMAS diagonally (down and left)
                    if i < len(text) - 3:
                        if diag_left(text[i+1], text[i+2], text[i+3], j):
                            count += 1
                    
                # If there's room above to spell XMAS upwards
                if i > 2:
                    if up_down(text[i-1], text[i-2], text[i-3], j):
                        count += 1

                # If there's room below to spell XMAS downwards
                if i < len(text) - 3:
                    if up_down(text[i+1], text[i+2], text[i+3], j):
                        count += 1

print(count)




