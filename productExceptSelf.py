
def productExceptSelf(nums: list[int]) -> list[int]:
	output = [1] * (len(nums) + 2)

	# Do first pass for prefixes
	pre = 1
	for i, v in enumerate(nums):
		output[i+1] = pre
		pre *= v 
	print(output)

	# Do second pass backwards for postfixes
	post = 1
	for i in range(len(nums)-1, -1, -1):
		output[i+1] *= post
		post *= nums[i]
	print(output)
	
	return output[1:-1]
		


print(productExceptSelf([1,2,3,4]))
