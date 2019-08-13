def next_permute(nums):
    if not nums or len(nums) == 0:
        return
    precede = len(nums) - 2
    # find the longest decreasing sequence
    while (precede >= 0 and nums[precede+1] <= nums[precede]):
        precede -= 1
    
    # if the entire list is the largest permute, we just reverse the list
    if (precede >= 0):
        smallestHigher = len(nums) - 1
        # find the smallest element that is higher than the precede
        while (smallestHigher >= 0 and nums[smallestHigher] <= nums[precede]):
            smallestHigher -= 1
        # Swap precede with smallest higher than precede
        nums[precede], nums[smallestHigher] = nums[smallestHigher], nums[precede]
    nums[precede+1:] = nums[precede+1:][::-1]
