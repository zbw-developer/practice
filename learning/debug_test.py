
def calc(a, b):
    total = a + b
    return total


nums = [3,7,1,9,5]
biggest = nums[0]

for n in nums:
    if n >biggest:
        biggest = n
    print(f"当前 n={n},biggest={biggest}")

print(f"最大值 = {biggest}")
print(calc(2,3))