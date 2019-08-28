'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
'''

def twoSum(nums, target):
  indexes = []
  #print(len(nums))
  for i in range(0,len(nums)):
    #print('in i: ',i)
    for j in range(i+1,len(nums)):
      #print('in j: ',j)
      if (nums[i] + nums[j] == target):
        indexes.append(i)
        indexes.append(j)
        return(indexes)

print(twoSum([2,7,11,15],9))