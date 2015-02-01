import math
nums = range(1,101)
nums_sum = math.fsum(nums)**2
sq_sum = math.fsum([i ** 2 for i in nums])
print nums_sum - sq_sum