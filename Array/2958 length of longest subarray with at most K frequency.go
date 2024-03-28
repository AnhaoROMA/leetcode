package main

import "fmt"

func maxSubarrayLength(nums []int, k int) int {
    var length int = len(nums)
    var count map[int]int = make(map[int]int)
    var i, j, ans int
    for i < length && j < length {
        count[nums[j]] += 1
        for count[nums[j]] > k {
            count[nums[i]] -= 1
            i += 1
        }
        if j-i+1 > ans {
            ans = j - i + 1
        }
        j += 1
    }
    return ans
}

func main() {
    fmt.Println(maxSubarrayLength([]int{1, 2, 3, 1, 2, 3, 1, 2}, 2))
}
