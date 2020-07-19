package main

func maxSubArray(nums []int) int {
	max:=func( x,y int) int {
		if (x<=y) {
			return y;
		}
		return x;
	}
	ans:=nums[0]
	sum:=0
	for _,v := range(nums){
		if (sum<0) {
			sum=v
		}else {
			sum+=v
		}
		ans=max(ans,sum)

	}
	return ans;

}




