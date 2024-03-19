package main

import (
	"fmt"
	"sort"
)

func leastInterval(tasks []byte, n int) int {
	table := map[byte]int{}
	for _, c := range tasks {
		table[c] += 1
	}
	queue := make([]int, 0)
	for _, num := range table {
		queue = append(queue, num)
	}
	sort.Ints(queue)
	gapsNum := queue[len(queue)-1] - 1
	idleNums := gapsNum * n
	for i := len(queue) - 2; i > -1; i-- {
		if gapsNum < queue[i] {
			idleNums -= gapsNum
		} else {
			idleNums -= queue[i]
		}
	}
	if idleNums < 0 {
		return len(tasks)
	} else {
		return len(tasks) + idleNums
	}
}

func main() {
	fmt.Println(leastInterval([]byte{'A', 'A', 'A', 'B', 'B', 'B', 'C'}, 2))
}
