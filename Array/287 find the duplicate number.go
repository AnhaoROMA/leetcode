package main

import "fmt"

/*
	Given an array of integers nums containing n+1 integers where each integer is in the range [1, n] inclusive.

	There is only one repeated number in nums, return this repeated number.

	You must solve the problem using only constant extra space.
*/

func findDuplicate(nums []int) int {
    // Method: to mark visited element negative
	for i := 0; i < len(nums); i++ {
		var ind int = abs(nums[i])
		if nums[ind] < 0 {
			return ind
		}
		nums[ind] = -nums[ind]
	}
	return -1
}

func abs(num int) int {
	if num < 0 {
		return -num
	} else {
		return num
	}
}

func main() {
	fmt.Println(findDuplicate([]int{1, 3, 4, 2, 2}))
	fmt.Println(findDuplicate([]int{3, 1, 3, 4, 2}))
}