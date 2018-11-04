# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:19:40 2017

@author: evansl
"""


def pentagonal_number(num):
    """How many dots exist in a pentagonal shape around a center dot on the Nth iteration.

    :param num: size of pentagon.
    :type num: int
    :returns: the number of dots that exist in the whole pentagon.

    """
    inner = 1
    outer = 0
    for i in range(1, num):
        inner = inner + outer
        outer = i*5
    return inner+outer


output = pentagonal_number(5)
print(output)
