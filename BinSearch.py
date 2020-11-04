inp = input().split()
nums = []
for elem in inp:
    nums.append(int(elem))
nums.sort()
x = int(input("What to search? "))
left = 0
right = len(nums) - 1
result = None

while (left <= right) and (result is None):
    shaft = (left + right) // 2

    if nums[shaft] == x:
        result = shaft
    elif nums[shaft] > x:
        right = shaft - 1
    else:
        left = shaft + 1
if result:
    print("Find at:", result)
else:
    print("Not find...")