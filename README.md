# DataStructures and Algorithms in Python

This is a collection of code snippets and the corresponding notes that I made while studying DataStructures and Algorithms using Python.



***

## Binary Search

### Example 1



	def binary_search(my_list, item):

            low_position = 0
            high_position = len(my_list) - 1

            while low_position <= high_position:
                mid_position = (low_position + high_position) // 2

                guess = my_list[mid_position]

                if guess == item:
                    return mid_position

                elif guess > item:
                    high_position = mid_position - 1

                else:
                    low_position = mid_position + 1

            return None
    my_list = [1, 2, 3, 4, 5, 6]
    print binary_search(my_list, 5)


