import random

nums = []
for i in range(10):
    num = random.randrange(1, 100)
    nums.append(bin(num))
print(nums)


fin_nums = []
for i in range(len(nums)):
    trans_num = 0
    multiplier = 1
    for j in range(len(nums[i])-2):
        trans_num += multiplier * int(nums[i][-1-(j)])
        multiplier *= 2
    fin_nums.append(trans_num)

print(fin_nums)
print([int(x[2:], 2) for x in nums])
if fin_nums == [int(x[2:], 2) for x in nums]:
    print('true')
