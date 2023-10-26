import random
import time 
#code for insertion sort 
def insertion_sort(arr, left=0, right=None):
  if right is None:
      right = len(arr) - 1

  for i in range(left + 1, right+1):
      key_item = arr[i]
      j = i - 1
      while j >= left and arr[j] > key_item:
          arr[j + 1] = arr[j]
          j -= 1
      arr[j + 1] = key_item

  return arr

#code for merging 
def merge(left, right):
  if not left:
      return right

  if not right:
      return left

  if left[0] < right[0]:
      return [left[0]] + merge(left[1:], right)

  return [right[0]] + merge(left, right[1:])

#code that combines insertion sort and the merge function to create a new sorting algorithm
def tim_sort(arr):
  min_run = 32
  n = len(arr)

  for i in range(0, n, min_run):
      insertion_sort(arr, i, min((i + min_run - 1), (n-1)))

  size = min_run
  while size < n:
      for start in range(0, n, size*2):
          midpoint = start + size - 1
          end = min((start + size*2 - 1), (n-1))

          merged_array = merge(
              left=arr[start:midpoint + 1],
              right=arr[midpoint + 1:end + 1]
          )
          arr[start:start + len(merged_array)] = merged_array

      size *= 2

  return arr
#code for bubble sort to use in comparison 
def bubble_sort(arr):
 n = len(arr)
 for i in range(n):
     for j in range(0, n-i-1):
         if arr[j] > arr[j+1]:
             arr[j], arr[j+1] = arr[j+1], arr[j]
 return arr
#code for selection sort to use for comparison 
def selection_sort(arr):
 n = len(arr)
 for i in range(n):
     min_index = i
     for j in range(i+1, n):
         if arr[j] < arr[min_index]:
             min_index = j
     arr[i], arr[min_index] = arr[min_index], arr[i]
 return arr
   
randL = [random.randint(1,1000) for _ in range(1000)]
start_time = time.time()
sorted_bubble = bubble_sort(randL.copy())
end_time = time.time()
bubble_sort_time = end_time - start_time

# Measure execution time for Selection Sort
start_time = time.time()
sorted_selection = selection_sort(randL.copy())
end_time = time.time()
selection_sort_time = end_time - start_time

# Measure execution time for TimSort
start_time = time.time()
sorted_hybrid_adaptive = tim_sort(randL.copy())
end_time = time.time()
tim_sort_time = end_time - start_time

# Print the execution times
print("Bubble Sort time:", bubble_sort_time)
print("Selection Sort time:", selection_sort_time)
print("Tim Sort time:", tim_sort_time)