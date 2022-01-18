from multiprocessing.sharedctypes import Value
from typing import Dict
from src.parse_tree import ParseTree

inputfile = input("Please enter input file: ")
#outputfile = input("Please enter output file: ")

filename = open("src/input.txt", 'r')
print(">>>Evaluation and sorting started:")

arr1 = []
arr2 = []
for lines in filename:
    line = lines.strip("\n")
    t = ParseTree(depth_symbol='.', mode=1)
    print(f"\n\nExpression Tree:{line}")
    t.read(line)
    t.build()
    print(f'Expression evaluates to:{t.evaluate(False)}')
    arr1.append(line)
    arr2.append(t.evaluate(False))
    arr3 = list(zip(arr1,arr2))
    


def mergeSort (l):
    if len (l) > 1:
        mid = int(len(l)/2)
        leftHalf = l[:mid]
        rightHalf = l[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)
        leftIndex,rightIndex,mergeIndex = 0,0,0

        mergeList= l
        while leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            if leftHalf[leftIndex ] < rightHalf[rightIndex]:

                mergeList[mergeIndex ] = leftHalf[leftIndex]
                leftIndex +=1
            else:
                mergeList[mergeIndex ] = rightHalf[rightIndex]
                rightIndex +=1
            mergeIndex +=1

        while leftIndex < len(leftHalf):
            mergeList[mergeIndex] = leftHalf[leftIndex]
            leftIndex +=1
            mergeIndex +=1

        while rightIndex < len(rightHalf):
            mergeList[mergeIndex ] = rightHalf[rightIndex]
            rightIndex +=1
            mergeIndex +=1

for i,j in arr3:
    mergeSort(j)

print(arr3)

