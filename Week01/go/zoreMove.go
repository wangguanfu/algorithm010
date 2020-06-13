package main

import "fmt"

//var nums [5]int = [5]int{1, 2, 3, 4, 5}

func moveZeroes2(nums []int) {
	i := 0
	for j:=0; j < len(nums) ;j++ {
		if nums[i] != 0 {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	fmt.Println(nums)
}

func moveZeroes3(nums []int) {
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j] = nums[i]
			if i != j {
				nums[i] = 0
			}
			j++
		}
	}
	fmt.Println(nums)
}

func main() {
	var nums []int = []int{0, 0, 0, 1, 2, 3, 4, 5}
	moveZeroes3(nums)
	moveZeroes2(nums)

}
