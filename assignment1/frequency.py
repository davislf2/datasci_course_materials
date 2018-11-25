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
__date__ = '25/11/2018'

import sys
import json
import collections


def frequency(tweet_file):
    terms_dict = collections.defaultdict(int)
    terms_count = 0
    for line in tweet_file:
        tweet = json.loads(line)
        if 'text' in tweet:
            text = tweet['text']
            terms = text.split()
            terms_count += len(terms)
            for term in terms:
                terms_dict[term] += 1

    for k, v in terms_dict.items():
        if v != 0:
            print "%s %.6f" % (k, float(v)/terms_count)


def main():
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)


if __name__ == '__main__':
    main()
