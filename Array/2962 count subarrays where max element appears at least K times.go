package main

import "fmt"

/*
    You are given an integer array nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.

    Constraints:
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^6
        1 <= k <= 10^5
*/
func countSubarrays(nums []int, k int) int64 {
    var length int = len(nums)
    var ans int = 0
    var maxElement int = 0
    for i := 0; i < length; i++ {
        if nums[i] > maxElement {
            maxElement = nums[i]
        }
    }
    var freq map[int]int = make(map[int]int)
    var i int = 0
    var j int = 0
    for i < length {
        freq[nums[i]] += 1
        for freq[maxElement] >= k {
            ans += length - i
            freq[nums[j]] -= 1
            j += 1
        }
        i += 1
    }
    return int64(ans)
}

func main() {
    fmt.Println(countSubarrays([]int{1, 3, 2, 3, 3}, 2))
}
