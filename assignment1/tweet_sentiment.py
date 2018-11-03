import sys
import json

def hw(sent_file, tweet_file):
    scores = get_scores(sent_file)
    print(scores.items()) # Print every (term, score) pair in the dictionary
    # with open(tweet_file) as f:
    #     data = f.readlines()

    with open(tweet_file, 'r') as fobj:
        data = json.load(fobj)

    print data['text']
    # with open('data/stream_apple.json') as f:
    #     data = json.load(json.dumps([f]))
    # print(data)

def lines(fp):
    print(str(len(fp.readlines())))

def get_scores(sent_file):
    scores = {}
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
