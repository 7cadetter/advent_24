def safe_check(nums):
    """
    Checks if a list of numbers is safe according to the rules in the dictionary
    """
    safe = True

    for i in range(len(nums)):
            j = i + 1
            for j in range(j, len(nums)):
                # If the number that comes before nums[j] should come after it
                if nums[j] in after and nums[i] in after[nums[j]]:
                    safe = False
                    # Return indexes to be swapped
                    return (i, j)
    if safe:
        # Return the middle of list if safe
        return int(nums[int((len(nums) - 1) / 2)])

with open('input_rules.txt', 'r') as rules:
    # Each key in this dictionary will have a list of values that should come after it
    after = {}

    for line in rules:
        num1 = line[:2]
        num2 = line[3:5]
        
        if num1 not in after:
            after[num1] = []

        # Add number that should come after key to value list
        after[num1].append(num2)

with open('input.txt', 'r') as text:
    total = 0
    for line in text:
        nums = line.split(',')
        # Remove \n
        nums[-1] = nums[-1][:-1]


        result = safe_check(nums)
        # While nums are not safe
        while not isinstance(result, int):
            # Swap the offending numbers and try again
            nums[result[0]], nums[result[1]] = nums[result[1]], nums[result[0]]
            result = safe_check(nums)
            # Add result once it's safe
            if isinstance(result, int):
                total += result
            
    
    print(total)