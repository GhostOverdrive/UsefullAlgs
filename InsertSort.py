inp = input().split()
nums = []
for elem in inp:
    nums.append(int(elem))
print("Before:", nums)
for i in range(len(nums)):
    lowest = i
    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j
    nums[i], nums[lowest] = nums[lowest], nums[i]
print("After:", nums)