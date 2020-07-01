def canJump(self, nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal




def canJump2(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True




