package main

import (
	"fmt"
	"sort"
)

func minDifference(nums []int) int {
    sort.Ints(nums)
	var length int = len(nums)
	if length <= 4 {
		return 0
	}
	var min func(...int) int = func(array ...int) int {
		sort.Ints(array)
		return array[0]
	}
	return min(
		nums[length-1] - nums[3],	// Remove the three smallest
		nums[length-2] - nums[2],	// Remove the two smallest and the largest
		nums[length-3] - nums[1],	// Remove the smallest and the two largest
		nums[length-4] - nums[0],	// Remove the three largest
	)
}

func main() {
	fmt.Println(minDifference([]int{1, 5, 0, 10, 14}))
}
