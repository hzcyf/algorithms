"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
for example: input:[1, [2, 3], [4, [5, 6], 7], 8], output: [1, 2, 3, 4, 5, 6, 7, 8]
"""
from collections import Iterable


# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)
        else:
            output_arr.append(ele)
    return output_arr


# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element
