"""
https://leetcode.com/problems/4sum/
"""


def three_sum(nums, sum):
    result = list()
    length = len(nums)
    for i in range(length):
        target = sum - nums[i]
        hashmap = dict()
        for j in range(i+1, length):
            if target - nums[j] in hashmap:
                temp = [nums[i], nums[hashmap[target - nums[j]]], nums[j]]
                temp.sort()
                if temp not in result:
                    result.append(temp)
            else:
                hashmap[nums[j]] = j
    return result


def four_sum(nums, sum=0):
    result = list()
    length = len(nums)
    for i in range(length):
        target = sum - nums[i]
        option = nums[:]
        option.pop(i)
        sub_result = three_sum(option, target)
        for p in sub_result:
            temp = [nums[i]] + p
            temp.sort()
            if temp not in result:
                result.append(temp)
    return result


a = [1, 0, -1, 0, -2, 2]
print(four_sum(a))
