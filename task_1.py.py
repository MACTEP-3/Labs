numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
def solve(nums : list):
    s = 0
    c = len(nums)
    for num in nums:
        if (num != None):
            s += num
    ans = s / c
    for i in range(len(nums)):
        if (nums[i] == None):
            nums[i] = ans
    return nums

print("Измененный список:", solve(numbers))
