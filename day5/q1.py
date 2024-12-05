with open('input_rules.txt', 'r') as rules:
    after = {}

    for line in rules:
        num1 = line[:2]
        num2 = line[3:5]
        
        if num1 not in after:
            after[num1] = []

        # Add each element that should come after a certain number to that number's dict values
        after[num1].append(num2)

with open('input.txt', 'r') as text:
    result = 0
    for line in text:
        safe = True
        nums = line.split(',')
        # Remove \n
        nums[-1] = nums[-1][:-1]
        
        for i in range(len(nums)):
            j = i + 1
            for j in range(j, len(nums)):
                # If the number that comes before nums[j] should come after it
                if nums[j] in after and nums[i] in after[nums[j]]:
                    safe = False
                    break
        if safe:
            # Add middle of list to result if safe
            result += int(nums[int((len(nums) - 1) / 2)])
    
    print(result)
            



