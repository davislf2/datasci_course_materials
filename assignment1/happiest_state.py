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


def getScoresOfSentiment(sent_file):
    scores = {}
    len = 0
    for line in sent_file:
        term, score = line.split(
            "\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        len += 1
    return scores, len


def happiest(sent_file, tweet_file):
    word_scores, len_sent = getScoresOfSentiment(sent_file)

    count = 0
    geo_score = collections.defaultdict(int)
    highest_score = 0
    happiest_state = None
    # term_score = {}
    for line in tweet_file:
        if count < 10000000:
            tweet = json.loads(line)
            try:
                # print json.dumps(tweet, indent=4, sort_keys=True)
                # with open("results.json", "a") as f:
                #     f.write(json.dumps(tweet, indent=4, sort_keys=True)+"\n")

                tweet_score = 0
                for word in tweet["text"].split(" "):
                    if word in word_scores:
                        tweet_score += word_scores[word]

                place = tweet["place"]
                if place and place["country_code"] == "US":
                    full_name = place["full_name"]
                    state = full_name.split()[-1]
                    city = full_name.split()[0]
                    geo_score[state] += tweet_score
                    if geo_score[state] > highest_score:
                        highest_score = geo_score[state]
                        happiest_state = state

            except:
                pass
        else:
            break
        count += 1

    # term = ["{} {}".format(k.encode("utf-8"), v) for k, v in
    #         geo_score.iteritems() if v != 0]
    # for t in term:
    #     print t

    print happiest_state




def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    happiest(sent_file, tweet_file)


if __name__ == '__main__':
    main()
