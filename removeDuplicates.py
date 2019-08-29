def removeDuplicates(nums):
    current_length = len(nums)
    i = 0
    j = 0
    while(i < (current_length - 1)):
        #print(nums)
        #print('in while loop 1')
        j = i + 1
        #print('i : ',i)
        #print('j : ',j)
        while ((nums[i] == nums[j]) and (j < current_length)):
            #print('in while loop 2')
            #print('nums[i]: ',nums[i])
            #print('nums[j]: ',nums[j])
            del nums[j]
            current_length = current_length - 1
            #print(current_length)
            #print('j : ',j)
            #print('out of while loop 2')
            if (j == current_length):
                return(current_length)
        i = i + 1
    return(len(nums))


print(removeDuplicates([1,2,2]))
        