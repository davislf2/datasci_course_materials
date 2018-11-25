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
import heapq

def hw(tweet_file):
    count = 0
    tag_score = collections.defaultdict(int)
    for line in tweet_file:
        if count < 10000000:
            tweet = json.loads(line)
            # print json.dumps(tweet, indent=4, sort_keys=True)
            try:
                entities = tweet["entities"]
                hashtags = entities["hashtags"]
                for h in hashtags:
                    tag = h["text"]
                    # print tag
                    tag_score[tag] += 1

            except:
                pass
        else:
            break
        count += 1

    top_ten_tags = heapq.nlargest(10, tag_score, key=tag_score.get)
    # print top_ten_tags
    for tag in top_ten_tags:
        print tag, tag_score[tag]

    # term = ["{} {}".format(k.encode("utf-8"), v) for k, v in
    #         top_ten_tags.iteritems() if v != 0]
    # for t in term:
    #     print t
    # print []
    # print len_sent
    # print count
    # print count
    # print(tweet_score)

    # print tweet_file
    # with open("output.txt", 'r', 'UTF-8') as fobj:
    #     data = json.encode('UTF-8').load(fobj)

    # print data['text']
    # with open('data/stream_apple.json') as f:
    #     data = json.load(json.dumps([f]))
    # print(data)

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
