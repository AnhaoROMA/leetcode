"""
https://leetcode.com/problems/tuple-with-same-product/
"""


def tuple_same_product(nums: list[int]) -> int:
    ans = 0

    nums.sort()
    length = len(nums)

    # # TLE 的做法（ 10^3 ）：
    # for i_1 in range(length-3):
    #     for i_2 in range(i_1+3, length):
    #         temp_product = nums[i_1] * nums[i_2]
    #         temp_set = set()
    #         for j in range(i_1+1, i_2):
    #             if nums[j] in temp_set:
    #                 ans += 1
    #                 temp_set.remove(nums[j])
    #                 continue
    #             if temp_product % nums[j] == 0:
    #                 temp_set.add(temp_product//nums[j])

    # 10^2
    temp_record = dict()
    for i in range(length):
        for j in range(i+1, length):
            ixj = nums[i] * nums[j]
            if ixj in temp_record:
                ans += temp_record[ixj]
                temp_record[ixj] += 1
            else:
                temp_record[ixj] = 1

    return ans * 8


print(
    tuple_same_product(
        [1, 2, 4, 5, 10]
    )
)
print(
    tuple_same_product(
        [2, 3, 4, 6, 8, 12]
    )
)
