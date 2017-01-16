# DataStructures and Algorithms in Python

* This is a collection of code snippets and notes made while studying Algorithms and Data Structures.

* All of the code here is in Python.

***

Table of Contents
=================

* [01. Linear Search](#01-linear-search)
* [02. Binary Search](#02-binary-search)

***

## 01. Linear Search

Linear Search is an algorithm to search a data set for an element of interest. It is one of the many search algorithms available and is also the most direct and simple of the lot.

Linear search looks for the element of interest in a dataset starting from the first element and moves on to the consecutive elements till it finds the one we’re interested in. Due to this behaviour, it’s not the fastest search algorithm around.

In the worst case, when the element of interest is the last one (or near-last) in the data set, linear-search has to sift through till the last element. The larger the data set, the more iterations it takes to find the element of interest, in the worst case. Hence, the performance of Linear search takes a toll as the size of the data set grows.

Linear search works on a sorted or unsorted data set equally since it has to go through the elements one by one, and doesn’t mind if the data is ordered or not.

### Performance

#### 1. Worst-case performance: O(n)

A worst-case analysis is done with the upper bound of the running time of the algorithm. ie.. the case when the maximum number of operations are executed.

The worst-case scenario for a linear search happens when the element-of-interest is not present in the dataset. A near worst-case scenario is when the element-of-interest is the last element of the dataset. In the first case, the search has to go through each element only to find that the element is not present in the dataset. In the second scenario, the search has to be done till the last element, which still takes iterations.

In the worst-case, the performance is O(n), where  n  is the number of elements in the dataset.

#### 2. Best-case performance: O(1)

In the best-case, where the element-of-interest is the first element in the dataset, only one search/lookup is needed. Hence the performance is denoted as O(1), for `n` elements.

#### 3. Average performance: O(n/2)

On an average, the performance can be denoted as O(n/2).

### Observations:

Linear Search iterates through every element in the dataset until it finds the match.
In Linear Search, the number of iterations grows linearly if the data set grows in size.
This algorithm is called  Linear Search  due to this linear increase in the complexity depending on the dataset.
The Best case is when the first iteration finds the element.
The Worst case is when the element of interest is not present in the dataset.
A very near worse case is when the element of interest is the last one in the dataset.
How does Linear Search work?

#### Linear search progresses as following:

1. Takes in a dataset as well as an element of interest.
2. Checks if the first element is the element of interest.
3. If yes, returns the element.
4. If not, move to the next element in the dataset.
5. Iterate till the dataset is exhausted.
6. Return  None if the element of interest is not present in the dataset.

### Example 1:

```python
def linear_search(my_list, item):
    """Linear search"""

    low_position = 0
    high_position = len(my_list) - 1

    while low_position < high_position:

        if my_list[low_position] == item:
            print("Your search item {0} is at position {1}".format(
                item, low_position))
            return low_position
        else:
            low_position += 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    linear_search(my_list, 5)
```

### Example 2:

This is the same example as above, but with a little more information being printed out.

```python
def linear_search(my_list, item):
    """Linear search"""

    low_position = 0
    high_position = len(my_list) - 1

    print("\nDataset size : {0}".format(len(my_list)))
    print("Item of choice : {0}\n".format(item))

    while low_position < high_position:

        print("Searching at index {0} of the dataset".format(low_position))

        if my_list[low_position] == item:
            print("Your search item {0} is at position {1}".format(
                item, low_position))
            return low_position
        else:
            print("{0} is not at index {1}\n".format(item, low_position))
            low_position += 1


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    linear_search(my_list, 16)
```

***

## 02. Binary Search

###Introduction

Binary Search is a search method used to find an object in a data set. This is much faster compared to the Linear Search algorithm we saw in a previous post. 

This algorithm works on the Divide and Conquer principle. Binary Search gets its speed by essentially dividing the list/array in half in each iteration, thus reducing the data-set size for the next iteration.

Imagine searching for an element in a rather large dataset. Searching for an element one by one using Linear Search would take n iterations. In a worst case scenario, if the element being searched is not present in the dataset or is at the end of the dataset, the time taken to find the object/element would be proportional to the size of the dataset.

The element of interest is returned if it is present in the dataset, else a NULL/None value is.

***Note:***

- Binary search will only work effectively on a Sorted collection.
- The code implementation will need minor changes depending on how the dataset is sorted, ie.. either in an increasing order or in a decreasing order.


### Performance

#### 1. Worst-case performance: log(n)

As discussed in the post on Linear Search, a worst-case analysis is done with the upper bound of the running time of the algorithm. ie.. the case when the maximum number of operations are needed/executed to find/search the element of interest in the dataset.

Of course, the worst-case scenario for any search algorithms is when the element of interest is not present in the dataset. The maximum number of searches has to be done in such a case, and it still ends up with no fruitful result. A similar but less worse-case is when the element is found in the final (or somewhere near the last) iteration.

Due to the divide-and-conquer method, the maximum number of iterations needed for a dataset of n elements is log(n), where the log base is 2.

Hence, for a data set of 10240 elements, Binary Search takes a maximum of 13 iterations.

```python
In [1]: import math

In [2]: math.log(10240, 2)
Out[2]: 13.321928094887364
```

For a data set of 50,000 elements, Binary Search takes 16 iterations in the worst case scenario while a Linear Search may take 50,000 iterations in a similar case.

```python
In [1]: import math

In [2]: math.log(50000, 2) 
Out[2]: 15.609640474436812
```

ie.. the Worst case for Binary search takes log(n) iterations to find the element.


#### 2. Best-case performance: O(1)

The best case scenario is when the element of interest is found in the first iteration itself. Hence the best-case would be where the search finishes in one iteration.

ie.. The best-case scenario would be O(1).

### How does Binary Search work?

Imagine a sorted dataset of 100 numbers and we're searching for  98 is in the list. A simple search would start from index 0 , moves to the element at index 1, progresses element by element until the one in interest is found. Since we're searching for 98, it'll take n iterations depending on the number of elements between the first element in the dataset and 98.

Binary Search uses the following method, provided the dataset is sorted.

- Find the length of the data set.
- Find the lowest (index 0), highest (index n), and the middle index of the data set.
- Find the subsequent elements residing in the first, last, and middle index.
- Check if the element of interest is the middle-element.
- If not, check if the element-of-interest is higher or lower than the middle element.
- If it is higher, assuming the dataset is sorted in an increasing order, move the lower index to one above the middle index.
- If it is lower, move the highest index to one below the middle index. 
- Check if the element of interest is the middle-element in the new/shorter dataset.
- Continue till the element of interest is found.



![Binary Search - Source: Wikipedia](/home/vimal/Dropbox/CODE/Programming-Studies/Future-Googler/DataStructures-and-Algorithms-in-Python/Binary_Search_Depiction.svg.png  "Binary Search")

**Figure 1 : Binary Search - Source: Wikipedia**

The figure above shows how Binary Search works on a dataset of 16 elements, to find the element 7.

- Index 0 , Index 16, and the middle index are noted.
- Subsequent values/elements at these indices are found out as well.
- Check if the element of interest 7 is equal to, lower, or higher than the middle element 14 at index 8.
- Since it's lower and the dataset is sorted in an increasing order, the search moves to the left of the middle index, ie.. from index 0 to index 7.
----
- The lower index is now 0, the higher index is now 7, and the middle index is now 3, the element in the middle index is 6.
- Check if the element of interest 7 is lower or higher than the middle element 6 at index 3.
- Since it's higher and the dataset is sorted in an increasing order, the search moves to the right of the middle index, ie.. from index 4 to index 7.
----
- So on and so forth.. till we arrive at the element of interest, ie.. 7.

As noted eariler, the data set is divided into half in each iteration. A numeric representation on how Binary search progresses can be seen as:


***

100 elements -> 50 elements -> 25 elements -> 12 elements -> 6 elements - 3 elements -> 1 element


***

### Code

#### Example 1 : (Data set sorted in Increasing order)

```python

def binary_search(my_list, item):

    # Find and set the low and high positions of the data set
    # Note that these are not the values, but just positions.
    low_position = 0
    high_position = len(my_list) - 1

    # Ideally `low_position` is always lower than `high_position`,
    # no matter how the list shrinks in each iteration.
    # Hence, we use a `while` loop which is always `True` to the condition
    while low_position <= high_position:

        # Find the middle position from the low and high positions
        mid_position = (low_position + high_position) // 2

    # Find the element residing in the middle position of the data set.
        mid_element = my_list[mid_position]

    # Check if the middle element is our element-of-interest, ie.. `item`
    # If so, return the position of our element-of-interest.
        if mid_element == item:
            print("Item is {0}".format(item))
            print(my_list[mid_element])
            return

    # Check if the middle element is a value higher than our element-of-interest.
    # If so, our element-of-interest falls *below* the middle element
    # Hence, we re-adjust the high_position to the middle position, thus
    # reducing the data set size by half.
        elif mid_element > item:
            high_position = mid_position - 1

    # Check if the middle element is lower than our element-of-interest.
    # If so, our element-of-interest falls *above* the middle element.
    # Hence, we re-adjust the low_position to the middle position, and
    # reduces the data set by half, as we did in the case above.
        else:
            low_position = mid_position + 1

    # Since these three conditions are in a `while True` loop, this gets
    # executed until the data set is reduced to a size where the
    # element-of-interest remains and is identified.

    # If the element-of-interest is not present in the data set, this code
    # returns None.
    return None


if __name__ == "__main__":
    my_list = ['a', 'b', 'c', 'd', 'e', 'f']
    # my_list = [1, 2, 3, 4, 5, 6]
    binary_search(my_list, "f")
```

#### Example 2 : (Data set sorted in Decreasing order)

```python
def binary_search(my_list, item):
    pass
    
```

### Observations:

- Binary Search needs a Sorted dataset to work.
- It can work on datasets sorted in both increasing and decreasing order.
- Binary Search finds the element of interest in logarithmic time, hence is also known as Logarithmic Search.
- Binary Search searches through a dataset of n elements in log(n) iterations, in the worst case scenario.

### References:

- [https://en.wikipedia.org/wiki/Binary_search_algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm)
- [http://quiz.geeksforgeeks.org/binary-search/](http://quiz.geeksforgeeks.org/binary-search/)
- [https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/](https://www.hackerearth.com/practice/algorithms/searching/binary-search/tutorial/)
- [http://research.cs.queensu.ca/home/cisc121/2006s/webnotes/search.html](http://research.cs.queensu.ca/home/cisc121/2006s/webnotes/search.html)



