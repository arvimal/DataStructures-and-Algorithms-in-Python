#!/usr/bin/env python2.7

# Binary Search Algorithm
# Example 1

# A Binary Search Algorithm searches an Array/List for an element.
# The Array/List has to be sorted in order to get Binary Search to work.
#
# https://www.youtube.com/watch?v=5xlIPT1FRcA
# https://www.youtube.com/watch?v=D5SrAga1pno


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


# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_list = [1, 2, 3, 4, 5, 6]
print binary_search(my_list, 5)
