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
    # key  : person
    # value: friend
    person = record[0]
    friend = record[1]
    mr.emit_intermediate(person, friend)


def reducer(person, list_of_friends):
    # key: person
    # value: list of friends
    print person, list_of_friends
    for friend in list_of_friends:
        try:
            # retrieve the friend's list_of_friends
            friends_list_of_friends = mr.intermediate[friend]
            # the friend doesn't connect back to the person
            if person not in friends_list_of_friends:
                mr.emit((person, friend))
                mr.emit((friend, person))
        # the friend doesn't have outer connection (list_of_friends)
        except KeyError:
                mr.emit((person, friend))
                mr.emit((friend, person))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
