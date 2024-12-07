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

        # Dictionary containing the index of each operator and its corresponding ternary value
        op_idx = {}

        ternary = 1
        for i in range(1, len(equation), 2):
            op_idx[i] = ternary
            ternary *= 3
        
        # Reverse the dictionary to make ternary work
        op_idx = dict(reversed(list(op_idx.items())))

        # Maximum amount of permutations for replacement (represent each number's ternary state with || 
        # for 2, * for 1 and + for 0)
        perm_max = (3**len(op_idx)) - 1
        # Current amount of permutations gone through
        perm_count = 0

        while perm_count <= perm_max:
            perm_clone = perm_count
            new_equation = copy.deepcopy(equation)

            # For each operator in the equation, if the permutation count is bigger than twice the operator's
            # ternary value, replace the plus sign with two bars and if it's bigger than only once, replace with
            # an asterisk. Decrease the permutation count by the ternary value (or twice the ternary value)
            for pair in op_idx.items():
                if perm_clone >= pair[1] * 2:
                    perm_clone -= pair[1] * 2
                    new_equation[pair[0]] =  '||'
                elif perm_clone >= pair[1]:
                    perm_clone -= pair[1]
                    new_equation[pair[0]] = '*'

            # For each new operation and number, add, multiply or concatenate it to the current total
            eq_total = new_equation[0]
            for i in range(1, len(new_equation), 2):
                op = new_equation[i]
                numb = new_equation[i + 1]
                if op == "+":
                    eq_total += numb
                elif op == "*":
                    eq_total *= numb
                elif op == '||':
                    eq_total = int(str(eq_total) + str(numb))


            # If the total of the equation matches the given total, add it to the result and move to next line
            if eq_total == total:
                result += total
                break

            perm_count += 1

    print(result)