with open('list1.txt', 'r') as list1, open('list2.txt', 'r') as list2:
    occurs = {}
    result = 0

    for line in list2:
        if line in occurs:
            occurs[line] += 1
        else:
            occurs[line] = 1
    
    for line in list1:
        if line in occurs:
            # Add similarity score
            result += int(line) * occurs[line]
    
    print(result)