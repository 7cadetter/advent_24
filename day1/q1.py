with open('list1.txt', 'r') as list1, open('list2.txt', 'r') as list2:
    l1 = list(list1)
    l2 = list(list2)
    l1.sort()
    l2.sort()
    result = 0
    
    for i in range(len(l1)):
        # Add difference
        result += abs(int(l1[i]) - int(l2[i]))
    
    print(result)
