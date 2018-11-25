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


def mapper(record):
    # key: document identifier
    # value: document contents
    value = record
    if record[0] == 'a':
        for k in range(5):
            key = (record[1], k)
            # print "a ", k, value
            mr.emit_intermediate(key, value)
    else:
        for i in range(5):
            key = (i, record[2])
            # print "b ", i, value
            mr.emit_intermediate(key, value)
    # key = record[1]
    # mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    pair = None
    while list_of_values:
        val = 0
        if pair is None:
            pair = list_of_values.pop()
        else:
            for v in list_of_values:
                if pair[0] == "a" and v[0] == "b":
                    if pair[2] == v[1]:
                        # print pair, v
                        val += pair[3]*v[3]
                elif pair[0] == "b" and v[0] == "a":
                    if pair[1] == v[2]:
                        # print pair, v
                        val += pair[3]*v[3]
            pair = None
        total += val
    mr.emit((key[0], key[1], total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
