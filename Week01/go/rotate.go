package main
func rotate1(nums []int, k int)  {
	k %= len(nums)
	ans := append(nums[len(nums)-k:], nums[:len(nums)-k]...)
	nums = append(nums[:0], ans...)
}
//方法二：三次翻转（108ms）
//
//reverse前半部分、后半部分、全部，时间复杂度是O(n)，空间复杂度 O(1)



func reverse(nums []int) {  // 翻转数组
	i,j := 0, len(nums)-1
	for i<j {
		nums[i],nums[j] = nums[j],nums[i]
		i++
		j--
	}
}

func rotate(nums []int, k int)  {
	k = k%len(nums)
	reverse(nums[:len(nums)-k])
	reverse(nums[len(nums)-k:])
	reverse(nums)
}
