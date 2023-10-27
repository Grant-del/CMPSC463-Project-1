# CMPSC463-Project-1

Project goals: Create a new sorting algorithm that is more efficient and usable than others 

Algorithm Created: I made an algorithm called TimSort that combines insertion sort and the merge function from merge sort. The algorithm divides the data into smaller chunks, then uses insertion sort on those chunks, then merges them using a modified merging algorithm. 

Benchmarking Results: I tested the code using a list of 1000 random integers from 1 to 1000, I tested this in comparison to two other sorting algorithms, that being bubble sort and selection sort and then calculating the time it took to perform the sorting. Bubble Sort took 0.2870 seconds to complete, Selection Sort took 0.1175 seconds to complete, and the Tim Sort took 0.0733 to compile which is the fastest. The time complexity for Bubble Sort and Selection Sort being O(n^2) while Tim Sort is O(n log n) which is why it is able to process a large set of 1000 numbers faster than the other algorithms. 

Conclusion: The implementation and analysis of these sorting algorithms have shown that TimSort, with its adaptability and efficient merging strategy, outperforms traditional sorting algorithms. This project highlights the importance of selecting the appropriate sorting algorithm based on the characteristics of the input data.
