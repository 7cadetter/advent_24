with open('input.txt', 'r') as input:
    lines = list(input)

with open('list1.txt', 'w') as list1, open('list2.txt', 'w') as list2:
    for line in lines:
        print(line[8:-1], file=list2)
        print(line[:5], file=list1)

                
