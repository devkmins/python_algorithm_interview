def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

print(arrayPairSum(1, 4, 3, 2))