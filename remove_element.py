def removeElement(nums,val):
  current_length = len(nums)
  i = 0
  while(i<current_length):
    if (nums[i] == val):
      del nums[i]
      current_length = current_length - 1
      i = i - 1
    i = i + 1
  return(len(nums))


removeElement([0,1,2,2,3,0,4,2,1],2)