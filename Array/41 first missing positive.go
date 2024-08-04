package main

import "fmt"

func firstMissingPositive(nums []int) int {
	// Method: to position elements at correct index
	var n int = len(nums)

    for i := 0; i < n; i++ {
		var num int = nums[i] // current element
		for 1 <= num && num <= n && num != i+1 && nums[num-1] != num {
			nums[i], nums[num-1] = nums[num-1], nums[i]
			num = nums[i] // update the current element
		}
	}

	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i+1
		}
	}
	return n+1
}

func main() {
	fmt.Println(firstMissingPositive([]int{3, 4, -1, 1}))
}