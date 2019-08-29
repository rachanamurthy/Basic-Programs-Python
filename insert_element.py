'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
'''

def searchInsert(nums, target):
    for i in range(0,len(nums)):
        if (nums[i] == target):
            return(i)
    for i in range(0,len(nums)):
        if nums[i] > target:
            return(i)
    return(len(nums))

print(searchInsert([1,3,5,6], 7))


        