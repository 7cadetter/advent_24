with open('input.txt', 'r') as input:
    text = input.read()
    result = 0
    do = True

    for i in range(len(text)):
        # If there is a string of 'mul('
        if text[i] == 'm' and text[i+1] == 'u' and text[i+2] == 'l' and text[i+3] == '(':
            # If do() is on
            if do:
                # Get the maxmimum length of the full mul string (12 characters)
                unsplit_mul = text[i:i+12]
                # Get rid of extra text after closing bracket
                mul = unsplit_mul.split(")", 1)[0]

                # If the last character before the closing bracket is a number (correct)
                if mul[-1].isnumeric():
                    # Add the closing bracket back
                    mul += ')'
                    # Split into two numbers
                    nums = mul.split(",")

                    # If there are two numbers within the brackets
                    if (len(nums) == 2):
                        # Get rid of 'mul(' from first element to isolate number
                        first_num = nums[0].split("(")[1]
                        # Get rid of closing bracket from second element
                        second_num = nums[1][:-1]
                        # Add their product to the result
                        result += int(first_num) * int(second_num)

        # If there is a string of 'do'
        elif text[i] == 'd' and text[i+1] == 'o':

            # If the string says 'don't()'
            if text[i+2] == 'n' and text[i+3] == "'" and text[i+4] == 't' and text [i+5] == '(' \
            and text[i+6] == ')':
                do = False

            # If the string says 'do()'
            elif text[i+2] == '(' and text[i+3] == ')':
                do = True
        
    print(result)