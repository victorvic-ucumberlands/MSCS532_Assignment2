#Generate 6 random arrays in orders of magnitude 10^2, 10^3, 10^4, 10^5, 10^6 and 10^7
import numpy as np

#Memory profiler
import tracemalloc
#Time profiler
import time

#Merge sort implementation
def merge_sort(arr):
    #Base case: if the array is empty or has one element, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        #Divide the array into two halves
        mid_idx = len(arr) // 2
        left_arr = merge_sort(arr[:mid_idx])
        right_arr = merge_sort(arr[mid_idx:])
        #Merge the sorted halves
        return merge(left_arr, right_arr)

def merge(left, right):
    merged_arr = []
    i  = 0
    j = 0
    #Merge the two halves while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    #If there are remaining elements in the left half, add them to the merged array
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
    #If there are remaining elements in the right half, add them to the merged array
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
    return merged_arr


arr1 = np.random.randint(0, 10000000, 100)
arr2 = np.random.randint(0, 10000000, 1000)
arr3 = np.random.randint(0, 10000000, 10000)
arr4 = np.random.randint(0, 10000000, 100000)
arr5 = np.random.randint(0, 10000000, 1000000)
arr6 = np.random.randint(0, 10000000, 10000000)

#Sort arrays in ascending order using python's built-in sorted() function
sorted_arr1 = sorted(arr1)
sorted_arr2 = sorted(arr2)
sorted_arr3 = sorted(arr3)
sorted_arr4 = sorted(arr4)
sorted_arr5 = sorted(arr5)
sorted_arr6 = sorted(arr6)

#Sort arrays in descending order using python's built-in sorted() function
sorted_arr1_desc = sorted(arr1, reverse=True)
sorted_arr2_desc = sorted(arr2, reverse=True)
sorted_arr3_desc = sorted(arr3, reverse=True)
sorted_arr4_desc = sorted(arr4, reverse=True)
sorted_arr5_desc = sorted(arr5, reverse=True)
sorted_arr6_desc = sorted(arr6, reverse=True)


#Measure time and memory usage of quick sort on each array
time_random = []
time_sorted = []
time_sorted_desc = []

memory_random = []
memory_sorted = []
memory_sorted_desc = []

# Measure time and memory usage of quick sort on each sorted array (random)
for arr in [arr1, arr2, arr3, arr4, arr5, arr6]:
    start_time = time.time()
    tracemalloc.start()
    merge_sort(arr)
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    memory_random.append(peak / 1024)  # Convert to KB
    time_random.append(end_time - start_time)


print("Time taken for merge sort on random arrays:", time_random)
print("Memory usage for merge sort on random arrays (KB):", memory_random)


# Measure time and memory usage of quick sort on each sorted array (ascending)
for arr in [sorted_arr1, sorted_arr2, sorted_arr3, sorted_arr4, sorted_arr5, sorted_arr6]:
    start_time = time.time()
    tracemalloc.start()
    merge_sort(arr)
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    memory_sorted.append(peak / 1024)  # Convert to KB
    time_sorted.append(end_time - start_time)

print("Time taken for merge sort on sorted arrays (ascending):", time_sorted)
print("Memory usage for merge sort on sorted arrays (ascending) (KB):", memory_sorted)

# Measure time and memory usage of quick sort on each sorted array (descending)
for arr in [sorted_arr1_desc, sorted_arr2_desc, sorted_arr3_desc, sorted_arr4_desc, sorted_arr5_desc, sorted_arr6_desc]:
    start_time = time.time()
    tracemalloc.start()
    merge_sort(arr)
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    tracemalloc.stop()
    memory_sorted_desc.append(peak / 1024)  # Convert to KB
    time_sorted_desc.append(end_time - start_time)

print("Time taken for merge sort on sorted arrays (descending):", time_sorted_desc)
print("Memory usage for merge sort on sorted arrays (descending) (KB):", memory_sorted_desc)


#Plot data using matplotlib
import matplotlib.pyplot as plt

sizes = [1e2, 1e3, 1e4, 1e5, 1e6, 1e7]

# Plot time analysis
plt.figure(figsize=(10, 6))
plt.plot(sizes, time_random, marker='o', label='Random')
plt.plot(sizes, time_sorted, marker='o', label='Sorted Ascending')
plt.plot(sizes, time_sorted_desc, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Time (seconds)')
plt.title('Merge Sort Time Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()

# Plot memory analysis
plt.figure(figsize=(10, 6))
plt.plot(sizes, memory_random, marker='o', label='Random')
plt.plot(sizes, memory_sorted, marker='o', label='Sorted Ascending')
plt.plot(sizes, memory_sorted_desc, marker='o', label='Sorted Descending')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Peak Memory Usage (KB)')
plt.title('Merge Sort Memory Usage Analysis')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.tight_layout()
plt.show()




   
