#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is the example module. This module does stuff.
"""
__author__ = ["[Davis Hong](https://github.com/davislf2)"]
__copyright__ = "Copyright 2018, The Boundary of Knowledge Project"
__credits__ = "Davis Hong"
__license__ = "MIT License"
__version__ = "0.1.0"
__maintainer__ = "Davis Hong"
__email__ = "davislf2.net@gmail.com"
__status__ = "Prototype"
__date__ = '24/11/2018'

import MapReduce
import sys
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

from itertools import permutations

def mapper(record):
    # key: document identifier
    # value: document contents
    person = record[0]
    friend = record[1]
    friendship_pair = [person, friend]
    mr.emit_intermediate(person, friendship_pair)


def reducer(key, list_of_pairs):
    # key: word
    # value: list of occurrence counts
    set_of_pairs = set(list_of_pairs)
    try:
        # names = mr.intermediate[key][3]

        # tot_pairs = list(permutations())
        for p in set_of_pairs:
            p[0], p[1] = p[1], p[0]
            mr.intermediate[key].append(p)
        for k, v in mr.intermediate.iteritems():
            mr.intermediate[k] = v[2] - set_of_pairs
    except:

    mr.result
    total_pairs = set()
    names = set()
    for pair in list_of_values:
        if [pair[1], pair[0]] in total_pairs:
            total_pairs.remove([pair[1], pair[0]])
    if key not in names:
        names.add(key)
        for n in names:
            if [n, key] not in total_pairs:
                total_pairs.add([n, key])
    list_of_values
    # for v in list_of_values:
    #     total += v
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
