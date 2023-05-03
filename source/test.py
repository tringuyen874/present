def binay_search(arr,target) :
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
def main() :
    arr = [1,2,3,4,5,6]
    postion = binay_search(arr,4)
    print(postion)
main()