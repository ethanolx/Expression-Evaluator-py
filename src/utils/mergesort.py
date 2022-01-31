'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''


# Sorts an arbitrary list using the merge sort algorithm
def mergeSort(l):
    # Termination clause
    if len(l) > 1:
        # Calculate split indices
        mid = int(len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        # Sorts sub-lists recursively
        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # Reset merge indices
        leftIndex, rightIndex, mergeIndex = 0, 0, 0
        mergeList = l

        # Merges sub-lists
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex += 1
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex += 1
            mergeIndex += 1

        # Copies remaining items in left sub-list
        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex += 1
            mergeIndex += 1

        # Copies remaining items in right sub-list
        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex += 1
            mergeIndex += 1
