package main

func subsets(nums []int) [][]int {
	ans := make([][]int, 0)

	var backtrace func(pos, num int, cur []int)

	backtrace = func(pos, num int, cur []int) {
		if len(cur) == num {
			tmp := make([]int, len(cur))
			copy(tmp, cur)
			ans = append(ans, tmp)
			return
		}

		for i := pos; i < len(nums); i++ {
			cur = append(cur, nums[i])
			backtrace(i+1, num, cur)
			cur = cur[:len(cur)-1]
		}
	}

	for i := 0; i <= len(nums); i++ {
		cur := make([]int, 0, i)
		backtrace(0, i, cur)
	}

	return ans
}

