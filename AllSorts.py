Bold on main
Non bold on all sports

import time
import random
import os
# Your current working directory needs to see the AllSorts.py
# If you have issues you should comment out this line.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import AllSorts

def main():
  random.seed(2020) # This makes sure that the random list will be the same every time.


  numberTerms = 10000

  orderedList = []
  reversedList = []
  randomList = []

  for i in range(numberTerms):
    orderedList.append(i)
    reversedList.insert(0, i)
    randomList.append(random.randint(1, 10000))

  # Run each of the sorts in different python sessions.
  # The sorts are bubbleSort, bubbleSortEarlyExit, selectionSort, insertionSort, and mergeSort

  print("Begin Sorting %d elements." % numberTerms)

  startTime = time.time()
  AllSorts.mergeSort(orderedList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Ordered list time: %.5f seconds" % elapsedTime)

  startTime = time.time()
  AllSorts.mergeSort(reversedList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Reversed list time: %.5f seconds" % elapsedTime)

  startTime = time.time()
  AllSorts.mergeSort(randomList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Random list time: %.5f seconds" % elapsedTime)

  print("Sorting Complete")


if __name__ == '__main__':
    main()



LAB 12

AllSorts
#Source of search comes from Geeks For Geeks website



# Function to do insertion sort
def insertionSort(arr):

  # Traverse through 1 to len(arr)
  for i in range(1, len(arr)):

    key = arr[i]

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and key < arr[j] :
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key


def bubbleSort(arr):
  n = len(arr)

  # Traverse through all array elements
  for i in range(n):

      # Last i elements are already in place
    for j in range(0, n-i-1):

        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
      if arr[j] > arr[j+1] :
        arr[j], arr[j+1] = arr[j+1], arr[j]


def bubbleSortEarlyExit(arr):
  n = len(arr)

  # Traverse through all array elements
  for i in range(n):
    swapped = False
    # Last i elements are already in place
    for j in range(0, n-i-1):

      # traverse the array from 0 to n-i-1
      # Swap if the element found is greater
      # than the next element
      if arr[j] > arr[j+1] :
        swapped = True
        arr[j], arr[j+1] = arr[j+1], arr[j]

    #if there were no changes this run, it is sorted, we can quit.
    if swapped == False:
        break #quits the current loop

def selectionSort(arr):
  for i in range(len(arr)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j

    # Swap the found minimum element with
    # the first element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Python program for implementation of MergeSort
def mergeSort(arr):
  if len(arr) >1:
    mid = len(arr)//2 #Finding the mid of the array
    L = arr[:mid] # Dividing the array elements
    R = arr[mid:] # into 2 halves

    mergeSort(L) # Sorting the first half
    mergeSort(R) # Sorting the second half

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i+=1
      else:
        arr[k] = R[j]
        j+=1
      k+=1

    # Checking if any element was left
    while i < len(L):
      arr[k] = L[i]
      i+=1
      k+=1

    while j < len(R):
      arr[k] = R[j]
      j+=1
      k+=1
