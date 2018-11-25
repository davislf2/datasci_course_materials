import sys
import json
import copy

def getScoresOfSentiment(sent_file):
    scores = {}
    len = 0
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        len += 1
    return scores, len


def hw(sent_file, tweet_file):
    word_scores, len_sent = getScoresOfSentiment(sent_file)
    # print(word_scores.items()) # Print every (term, score) pair in the dict

    count = 0
    for line in tweet_file:
    #     if count < 100:
        tweet = json.loads(line)  # .decode("utf-8")
        try:
            tweet_score = 0
            for word in tweet["text"].split(" "):
                # print word
                if word in word_scores: #scores.keys():
                    # tweet_score[tweet["text"]] += scores[word]
                    tweet_score += word_scores[word]
                    # print word
            print tweet_score

        except:
            pass  # print 0
        # else:
        #     break
        count += 1
    
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

'''
This default method will cause ValueError: Mixing iteration and read methods would lose data
Because sent_file and tweet_file have iterated all lines, so it doesn't has any line
'''
# def lines(fp):
#     return str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
