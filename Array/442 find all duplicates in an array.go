package main 

import "fmt"

/*
	Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
	and each integer appears once or twice, return an array of all the integers that appears twice.

	You must write an algorithm that runs in O(n) time and uses only constant extra space.
*/

func findDuplicates(nums []int) []int {
    // 参考第 287 题
	var ans []int = make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if nums[abs(nums[i])-1] < 0 {
			ans = append(ans, abs(nums[i]))
		} else {
			nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
		}
	}
	return ans
}

func abs(num int) int {
	if num < 0 {
		return -num
	} else {
		return num
	}
}

func main() {
	fmt.Println(findDuplicates([]int{4, 3, 2, 7, 8, 2, 3, 1}))
}