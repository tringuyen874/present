import math
import random
import time
import matplotlib.pyplot as plt

# pos = low + [(x - arr[low]) * (high - low) / (arr[high] - arr[low])]
# O(log(log(n)))

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


def interpolation_search(arr, target, low, high):
    # low = 0
    # high = len(arr) - 1
    
    if low > high or target < arr[low] or target > arr[high]:
        return -1 
    
    if arr[low] == arr[high]:
        if arr[low] == target:
            return low
        else:
            return -1
    #select pivot
    pivot_pos = low + int((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
    
    if arr[pivot_pos] == target:
        return pivot_pos
    
    if arr[pivot_pos] < target:
        return interpolation_search(arr, target, pivot_pos+1, high)
    
    return interpolation_search(arr, target, low, pivot_pos-1)

def jump_search(arr, target, low, high) :
    # low = 0
    # high = len(arr) - 1
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
    
    return jump_search(arr, target, prev+1, high)

# def ternary_search(arr,target, left, right) :
#     left = 0
#     right = len(arr) - 1
#     middle_1 = int(left + (right - left) / 3)
#     middle_2 = int(right - (right - left) / 3)
    
#     if (arr[middle_1] == target) :
#         return middle_1
#     if (arr[middle_2] == target) :
#         return middle_2
#     if (target  < arr[middle_1]) :
#         return ternary_search(arr, target, left, middle_1 - 1)
#     elif (target > arr[middle_2]) :
#         return ternary_search(arr, target, middle_2 + 1, right)
#     return ternary_search(arr, target, middle_1 - 1, middle_2 + 1)
    
def createData():
    for i in range(1, 6):    
        length = 200000000 * i # 200tr
        data = [i for i in range(0, length, 100)]
        
        # Open file in write mode
        with open("data.txt", "a") as f:
            f.write("\n")
            # Write data to file
            for item in data:
                f.write("%s" % item)
                f.write(" ")

        f.close()

def createRandomData():
    for i in range(1, 6):    
        length = 200000000 * i
        data = [random.randint(1, 10000000) for i in range(0, length, 100)]
        
        # Open file in write mode
        with open("randomdata.txt", "a") as f:
            f.write("\n")
            # Write data to file
            for item in data:
                f.write("%s" % item)
                f.write(" ")

        f.close()

def readData():
    input = []
    with open("data.txt", "r") as f:
        for line in f:
    # Read the contents of the file
            input.append(line)
    return input

def readRandomData():
    input = []
    with open("randomdata.txt", "r") as f:
        for line in f:
    # Read the contents of the file
            input.append(line)
    
    return input

def testIS(input, step):
    inputSize = []
    timeComplexityT = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[int(length * step)]
        inputSize.append(length)

        result = interpolation_search(newData, x, 0, length - 1)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityT.append(end - start)

    for i in range(len(timeComplexityT)):
        print(f"Time passed: {timeComplexityT[i]}")
        print(inputSize[i])
    return timeComplexityT, inputSize, x

def testJ(input, step):
    inputSize = []
    timeComplexityJ = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[int(length * step)]
        inputSize.append(length)

        result = interpolation_search(newData, x, 0, length - 1)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityJ.append(end - start)

    for i in range(len(timeComplexityJ)):
        print(f"Time passed: {timeComplexityJ[i]}")
        print(inputSize[i])
    return timeComplexityJ, inputSize

def testT(input):
    inputSize = []
    timeComplexityJ = []

    for i in range(len(input)):
        start = time.time()
        newData = input[i].split(" ")
        newData.pop(-1)
        newData = [int(i) for i in newData]
        newData.sort()
        # x = 150000000 * (i + 1)
        length = len(newData)
        x = newData[length//3]
        inputSize.append(length)

        result = interpolation_search(newData, x, 0, length - 1)
        # print(result)
        if result == -1:
            print(f"Element {x} not found in the array.")
        else:
            print(f"Element {x} found at index {result}.")
        end = time.time()
        timeComplexityJ.append(end - start)

    for i in range(len(timeComplexityJ)):
        print(f"Time passed: {timeComplexityJ[i]}")
        print(inputSize[i])
    return timeComplexityJ, inputSize

def main():
    input = readRandomData()
    # input = readData()
    del input[0]
    tempSize = 200000
    # print(a//19)

    step = []
    for i in range(0, tempSize + 1, tempSize//20):
        step.append(i/tempSize)
    del step[-1]
    for i in step:
        timeComplexityIS = testIS(input, i)[0]
        timeComplexityJ, inputSize = testJ(input, i)
        # makeStatistics(timeComplexityIS, timeComplexityJ, inputSize, i * 20)
        makeStatisticsFromRandomData(timeComplexityIS, timeComplexityJ, inputSize, i * 20)

    # createData()
    # createRandomData()
    
    
    # timeComplexityT = testT(input)[0]
    # drawGraph(timeComplexityIS, timeComplexityJ, inputSize)
    # print(f"Time passed: {end - start}")

def makeStatistics(timeIS, timeJ, size, index):
    with open("stat.txt", 'a') as f:
        timeISArray = [str(elem) for elem in timeIS]
        timeJArray = [str(elem) for elem in timeJ]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity IS: \n")
        f.write(" ".join(timeISArray))
        f.write("\nTime complexity J: \n")
        f.write(" ".join(timeJArray))
        f.write("\n")
    f.close() 

def makeStatisticsFromRandomData(timeIS, timeJ, size, index):
    with open("statRandom.txt", 'a') as f:
        timeISArray = [str(elem) for elem in timeIS]
        timeJArray = [str(elem) for elem in timeJ]
        sizeArray = [str(elem) for elem in size]
        f.write(f"\nIndex: {index}th\n")
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity IS: \n")
        f.write(" ".join(timeISArray))
        f.write("\nTime complexity J: \n")
        f.write(" ".join(timeJArray))
        f.write("\n")
    f.close()

def drawGraph(timeIS, timeJ, size):
# Sample data for three lines
    with open("stat.txt", 'a') as f:
        timeISArray = [str(elem) for elem in timeIS]
        timeJArray = [str(elem) for elem in timeJ]
        sizeArray = [str(elem) for elem in size]
        f.write("Input size:  \n")
        f.write(" ".join(sizeArray))
        f.write("\nTime complexity IS: \n")
        f.write(" ".join(timeISArray))
        f.write("\nTime complexity J: \n")
        f.write(" ".join(timeJArray))
        f.write("\n")
    f.close()        
    fig, ax = plt.subplots()
    # Plot the three lines
    ax.plot(size, timeIS, label='IS')
    ax.plot(size, timeJ, label='J')
    # ax.plot(size, timeT, label='T')
    # Add a legend to the plot
    plt.legend()

    # Add labels to the x and y axes
    plt.xlabel('Input size')
    plt.ylabel('Time complexity(seconds)')

    # Set the title of the plot
    plt.title('Relation between input size and time complexity  ')

    # Display the plot
    plt.show()

main()

# Example  ahjkfgjksdhfg


