def mergeSort(l):
    if len(l) > 1:
        mid = int(len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        leftIndex, rightIndex, mergeIndex = 0, 0, 0

        mergeList = l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex] < rightHalf[rightIndex]:
                mergeList[mergeIndex] = leftHalf[leftIndex]
                leftIndex += 1
            else:
                mergeList[mergeIndex] = rightHalf[rightIndex]
                rightIndex += 1
            mergeIndex += 1

        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex += 1
            mergeIndex += 1

        while rightIndex < len(rightHalf):
            mergeList[mergeIndex] = rightHalf[rightIndex]
            rightIndex += 1
            mergeIndex += 1
