# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# FUNCTIONS
def bubbleSort(anArray):
    for i in range(len(anArray)):
        for nums in range(0, len(anArray) - i - 1):
            if anArray[nums] > anArray[nums + 1]:
                temp = anArray[nums]
                anArray[nums] = anArray[nums + 1]
                anArray[nums + 1] = temp

def selectionSort(anArray):
    for fillsl in range(0, len(anArray) - 1):
        minpos = fillsl
        for i in range(fillsl+1, len(anArray)):
            if anArray[i] < anArray[minpos]:
                minpos = i
        anArray[fillsl], anArray[minpos] = anArray[minpos], anArray[fillsl]

def insertionSort(anArray):
    for ins in range(1, len(anArray)):
        insertval = anArray[ins]
        testpos = ins - 1 
        while testpos >= 0 and insertval < anArray[testpos]:
            anArray[testpos + 1] = anArray[testpos]
            testpos -= 1
        anArray[testpos + 1] = insertval 


# COLLECTING DATA
# Bubble Sort
startTime = time.time()
bubbleSort(randomData)
endTime = time.time()
print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
startTime = time.time()
bubbleSort(reversedData)
endTime = time.time()
print(f"Bubble Sort Reversed Data: {endTime - startTime} seconds")
startTime = time.time()
bubbleSort(nearlySortedData)
endTime = time.time()
print(f"Bubble Sort Nearly Sorted Data: {endTime - startTime} seconds")
startTime = time.time()
bubbleSort(fewUniqueData)
endTime = time.time()
print(f"Bubble Sort Few Unique Data: {endTime - startTime} seconds")

# Selection Sort
startTime = time.time()
selectionSort(randomData)
endTime = time.time()
print(f"Selection Sort Random Data: {endTime - startTime} seconds")
startTime = time.time()
selectionSort(reversedData)
endTime = time.time()
print(f"Selection Sort Reversed Data: {endTime - startTime} seconds")
startTime = time.time()
selectionSort(nearlySortedData)
endTime = time.time()
print(f"Selection Sort Nearly Sorted Data: {endTime - startTime} seconds")
startTime = time.time()
selectionSort(fewUniqueData)
endTime = time.time()
print(f"Selection Sort Few Unique Data: {endTime - startTime} seconds")

# Insertion Sort
startTime = time.time()
insertionSort(randomData)
endTime = time.time()
print(f"Insertion Sort Random Data: {endTime - startTime} seconds")
startTime = time.time()
insertionSort(reversedData)
endTime = time.time()
print(f"Insertion Sort Reversed Data: {endTime - startTime} seconds")
startTime = time.time()
insertionSort(nearlySortedData)
endTime = time.time()
print(f"Insertion Sort Nearly Sorted Data: {endTime - startTime} seconds")
startTime = time.time()
insertionSort(fewUniqueData)
endTime = time.time()
print(f"Insertion Sort Few Unique Data: {endTime - startTime} seconds")

# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")


