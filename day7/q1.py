import copy

with open('input.txt', 'r') as text:
    result = 0
    for line in text:
        # Split into total and numbers
        total, numbers = line.split(':')
        numbers = numbers.split()
        total = int(total)
        numbers = [int(i) for i in numbers]

        # Add numbers to a list separated by a plus sign
        equation = []
        for num in numbers:
            equation.append(num)
            equation.append('+')

        # Remove the last plus sign
        equation.pop()

        # Dictionary containing the index of each operator and its corresponding binary value
        op_idx = {}

        binary = 1
        for i in range(1, len(equation), 2):
            op_idx[i] = binary
            binary *= 2
        
        # Reverse the dictionary to make binary work
        op_idx = dict(reversed(list(op_idx.items())))

        # Maximum amount of permutations for replacement (represent each number's binarynary state with 
        # * for 1 and + for 0)
        perm_max = (2**len(op_idx)) - 1
        # Current amount of permutations gone through
        perm_count = 0

        while perm_count <= perm_max:
            perm_clone = perm_count
            new_equation = copy.deepcopy(equation)

            # For each operator in the equation, if the permutation count is bigger than the operator's binary
            # value, replace the plus sign with an asterisk and decrease the permutation count by the binary value
            for pair in op_idx.items():
                if perm_clone >= pair[1]:
                    perm_clone -= pair[1]
                    new_equation[pair[0]] = '*'


            eq_total = new_equation[0]
            
            # For each new operation and number, add / multiply it to the current total
            for i in range(1, len(new_equation), 2):
                op = new_equation[i]
                numb = new_equation[i + 1]
                if op == "+":
                    eq_total += numb
                elif op == "*":
                    eq_total *= numb

            # If the total of the equation matches the given total, add it to the result and move to next line
            if eq_total == total:
                result += total
                break

            perm_count += 1

    print(result)