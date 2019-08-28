'''
Program to find the maximum area of water in the container
'''
def maxArea(height):
    area = 0
    i = 0
    j = len(height) - 1
    
    while(i!=j):
        if height[i] < height[j]:   
            present_area = height[i] * (j - i)
            i = i + 1
        else:
            present_area = height[j] * (j - i)
            j = j - 1
        if present_area > area:
            area = present_area
    
    return area

if __name__ == '__main__':
    print(maxArea([1,8,6,2,5,4,8,3,7]))