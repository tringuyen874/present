import math
#abvdlskjgfkds
from matplotlib import pyplot as plt
def binay_search(arr, target) :
    #base case : if arr is empty
    if (len(arr) == 0) :
        return 0
    
    # divide arr into 2 subarr
    middle_pos = len(arr) //2
    left = arr[:middle_pos]
    right = arr[middle_pos + 1:]
    
    if (arr[middle_pos] == target) :
        return middle_pos
    
    if arr[middle_pos] > target :
        return binay_search(left, target)
    
    return binay_search(right, target)


def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    if low > high or target < arr[low] or target > arr[high]:
        return -1 
    
    #select pivot
    pivot_pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
    
    if arr[pivot_pos] == target:
        return pivot_pos
    
    if arr[pivot_pos] < target:
        return interpolation_search(arr, target, pivot_pos+1, high)
    
    return interpolation_search(arr, target, low, pivot_pos-1)

def jump_search(arr, target) :
    low = 0
    high = len(arr) - 1
    if low > high :
        return -1
    step = int(math.sqrt(len(arr)))
    prev = low
    
    # Jumping through the array
    while arr[min(step, high)-1] < target:
        prev = step
        step += int(math.sqrt(high-low))
        if prev >= high:
            return -1
    
    # Linear search within the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, high):
            return -1
    
    # If element is found, return its index
    if arr[prev] == target:
        return prev
    if arr[prev] > target:
        return jump_search(arr, target, low, prev-1)
    
    return jump_search(arr, target, prev + 1, high)

def ternary_search(arr,target) :
    left = 0
    right = len(arr) - 1
    pivot_1 = int(left + (right - left) / 3)
    pivot_2 = int(right - (right - left) / 3)
    
    if (arr[pivot_1] == target) :
        return pivot_1
    if (arr[pivot_2] == target) :
        return pivot_2
    if (target  < arr[pivot_1]) :
        return ternary_search(arr, target, left, pivot_1 - 1)
    elif (target > arr[pivot_2]) :
        return ternary_search(arr, target, pivot_2 + 1, right)
    return ternary_search(arr, target, pivot_1 - 1, pivot_2 + 1)

def main() :
    arr = [1,2,3,4,5,6]
    postion = binay_search(arr,4)
    postion1 = interpolation_search(arr,4)
    postion3 = jump_search(arr,4)
    postion4 = ternary_search(arr,4)
    print(postion)
    print(postion1)
    print(postion3)
    print(postion4)
main()