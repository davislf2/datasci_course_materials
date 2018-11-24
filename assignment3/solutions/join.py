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
__date__ = '23/11/2018'


import MapReduce
import sys
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

import copy

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    # key2 = record[1]
    value = record[:]
    # words = value.split()
    # for w in value:
        # mr.emit_intermediate(key, w)
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in list_of_values:
        if v[0] == "order":
            # total.append(v[0:3])
            for w in v:
                total.append(w)
    for v in list_of_values:
        if v[0] == "line_item":
            # total.append(v[0:3])
            for w in v:
                total.append(w)
            # print "-----------"
            # print total
            mr.emit(copy.copy(total))
            for w in v:
                total.pop()
            # print total


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
