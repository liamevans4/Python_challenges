# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:33:22 2017

@author: evansl
"""

import operator
import itertools

start_pos = (0, 0)
finish_pos = (4, 4)

inp = "drdr??rrddd?"
inp2 = "???rrurdr?"


def insert_possible_values(instr, rps):
    """Replace the ?s with the possible combination.

    :param instr: input string with ?s.
    :param rps: possible permutation to replace ?s.
    :type instr: str
    :type rps: str
    :returns: possible path with ?s replaced.

    """
    for i in rps:
        j = instr.find('?')
        instr = instr[:j] + i + instr[j+1:]
    # print(instr)
    return instr


def compute_string(string):
    """Caclulate the path of the string and print if it reaches the end.

    :param string: input path string.
    :type string: str

    """
    visited_sqrs = []
    lst_str = list(string)
    current_pos = start_pos
    for i in lst_str:
        step = {'u': (0, -1), 'd': (0, 1), 'r': (1, 0), 'l': (-1, 0)}
        current_pos = tuple(map(operator.add, current_pos, step[i]))
        visited_sqrs.append(current_pos)
    if current_pos == finish_pos:
        if len(visited_sqrs) == len(set(visited_sqrs)):
            print(current_pos)
            print(string)


def generate_all_combinations(l):
    """
    :param l: elements to permutate.
    :type l: str
    :returns: list of combinations of giving string elements.
    """
    yield from itertools.product(*([l] * num_qs))


num_qs = inp2.count('?')
for x in generate_all_combinations('lrud'):
    if ''.join(x).endswith(('r', 'd')):
        # print(x)
        outp = insert_possible_values(inp2, x)
        compute_string(outp)
