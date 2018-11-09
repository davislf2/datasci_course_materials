import sys
import json
import copy

def hw(sent_file, tweet_file):
    scores, len_sent = get_scores(sent_file)
    # print(scores.items()) # Print every (term, score) pair in the dictionary
    # with open(tweet_file) as f:
    #     data = f.readlines()

    # tweet_file_copy = copy.deepcopy(tweet_file)
    count = 0
    tweet_score = {}
    for line in tweet_file:
    # for line in tweet_file_copy:
        
        if count < 10:
            # print(line)
            try:
                tweet = json.loads(line) #.decode("utf-8")
                # print(tweet["text"])
                # tweet_score[tweet["text"]] = 0
                tweet_score = 0
                # words = tweet["text"].split()
                # print [w.encoding for w in words]
                # print words[0] == 'RT'
                # if "gain" in scores.keys():
                #     print "gain"

                for word in tweet["text"].split():
                    # print word
                    if word in scores: #scores.keys(): 
                        # tweet_score[tweet["text"]] += scores[word]
                        tweet_score += scores[word]
                        # print word
                print tweet_score
                
            except:
                pass #print 0
        else:
            break
        count += 1
    
    print len_sent
    print count
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

def get_scores(sent_file):
    scores = {}
    len = 0
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        len += 1
    return scores, len

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
