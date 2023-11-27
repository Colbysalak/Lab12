# The purpose of this lab is to see the speed of different sorting techniques.
# Use the same random seed to create the same random list of nubmers for each run.
# You can change the number of elements in the arrays
# We will test 3 arrays, one that is already in order, one that is sorted in reverse order, and one that it random.

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
  AllSorts.bubbleSort(orderedList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Ordered list time: %.5f seconds" % elapsedTime)

  startTime = time.time()
  AllSorts.bubbleSort(reversedList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Reversed list time: %.5f seconds" % elapsedTime)

  startTime = time.time()
  AllSorts.bubbleSort(randomList)
  endTime = time.time()
  elapsedTime = endTime - startTime
  print("Random list time: %.5f seconds" % elapsedTime)

  print("Sorting Complete")


if __name__ == '__main__':
  main()
