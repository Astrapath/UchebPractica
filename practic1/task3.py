def duplicates(nums):
    return len(nums) != len(set(nums))
nums = [1, 2, 3, 4]
print(duplicates(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(duplicates(nums))

nums = [1, 2, 3, 1]
print(duplicates(nums))