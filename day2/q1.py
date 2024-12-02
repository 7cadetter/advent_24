safe = 0

with open('input.txt', 'r') as file:
    for line in file:
        print('\n')
        increasing = False
        decreasing = False
        strs = line.split()
        nums = list(map(int, strs))
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
            safe += 1
            

print(safe)