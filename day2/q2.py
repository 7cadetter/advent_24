def safeTest(nums):
    increasing = False
    decreasing = False
    
    # If numbers are decreasing
    if nums[0] > nums[1] and nums[0] - nums[1] < 4:
        decreasing = True
    # If numbers are increasing
    elif nums[0] < nums[1] and nums[1] - nums[0] < 4:
        increasing = True

    i = 2    
    while (decreasing or increasing) and i < len(nums):
        # If numbers stop decreasing properly
        if decreasing and (nums[i-1] <= nums[i] or nums[i-1] - nums[i] > 3):
            decreasing = False
        # If numbers stop increasing properly
        elif increasing and (nums[i-1] >= nums[i] or nums[i] - nums[i-1] > 3):
            increasing = False
        i += 1

    # If everything went fine
    if increasing or decreasing:
        return True
    else:
        return False
    
        

safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        strs = line.split()
        nums = list(map(int, strs))
        # If numbers are fine already
        if safeTest(nums):
            safe += 1
        else:
            i = 0
            # For each number in line, make a new list that excludes that number
            while i in range(len(nums)):
                new_nums = []
                # Put number in new list if it's not the excluded one
                for j in range(len(nums)):
                    if j != i:
                        new_nums.append(nums[j])
                if (safeTest(new_nums)):
                    safe += 1
                    # Break from loop
                    i = len(nums)
                else:
                    i += 1              

print(safe)