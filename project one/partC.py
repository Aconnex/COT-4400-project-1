# Use Quicksort algorithm (Lecture 5) to sort the following sequences:
# c. Choose your sequence with 1000 different (random) integer numbers

# mainA[] is the Array to be sorted,
# startI  is the Starting index,
# endI  is the Ending index

import random
def partition(mainA, startI, endI):
    i = (startI - 1)
    pivot = mainA[endI]  # pivot

    for j in range(startI, endI):
        if mainA[j] < pivot:
            i = i + 1
            mainA[i], mainA[j] = mainA[j], mainA[i]

    mainA[i + 1], mainA[endI] = mainA[endI], mainA[i + 1]
    return (i + 1)

# Quicksort function
def quickSort(mainA, startI, endI):
    if startI < endI:
        partitionIndex = partition(mainA, startI, endI)

        quickSort(mainA, startI, partitionIndex - 1)
        quickSort(mainA, partitionIndex + 1, endI)

mainA = []
for i in range(1000):
    n = random.randint(0,1000)
    mainA.append(n)
print("The array between 1 to 1000 are: ", mainA)
n = len(mainA)
quickSort(mainA, 0, n - 1)
print("The sorted array are:", mainA)