# DataStructures and Algorithms in Python

* This is a collection of code snippets and notes made while studying Algorithms and Data Structures.

* All of the code here is in Python.

***

[TOC]

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

***

## 02. Binary Search

### Example 1

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