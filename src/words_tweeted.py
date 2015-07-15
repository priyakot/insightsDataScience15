# example of program that calculates the total number of times each word has been tweeted.

from collections import Counter, defaultdict, OrderedDict
import re
import sys
import random
import math
import os
import operator
import pickle
import fileinput
from heapq import heappush, heappop

wordCount = Counter()
heap = []
numbers = []
leftElement, rightElement = [], []
keylist = defaultdict(int)

def tokenize(text):
	return text.split(' ')
    #return re.findall('[a-z0-9]+', text)

def readTrainingFile(fileName):
    vocab = defaultdict(int)
    tweet = Counter()
    likelihood = defaultdict(Counter)
    i = 0
    with open(fileName,errors='ignore') as f:
        for line in f:
        	for word in tokenize(line):
        		vocab[word] += 1 
        		wordCount[word] += 1
        		tweet[i] += 1
        		likelihood[i][word] += 1
        	i += 1
    return (vocab, wordCount, tweet,likelihood)

def findMedian(n):
    global leftElement, rightElement
    if len(leftElement) <= len(rightElement):
        heappush(leftElement, -n)
    else:
        heappush(rightElement, n)
    if rightElement and -leftElement[0] > rightElement[0]:
        heappush(leftElement, -heappop(rightElement))
        heappush(rightElement, -heappop(leftElement))
    if len(leftElement) > len(rightElement):
        return -leftElement[0]
    return (rightElement[0] - leftElement[0]) / 2.0
    
def main():
	count = 0
	trainingFile = "tweet_input/tweets.txt"
	(vocab, wordCount, tweet,likelihood) = readTrainingFile(trainingFile)
	keylist = OrderedDict(sorted(vocab.items()))

	with open("tweet_output/ft1.txt", "w") as f:
		for key, word in keylist.items():
			print(key.rstrip(),word,file=f)
			
	with open("tweet_output/ft1.txt","r") as fl1:
		lines=fl1.readlines()
	with open("tweet_output/ft1.txt","w") as fl1:  
		[fl1.write(line) for line in lines if line.strip() ]
	
	with open("tweet_output/ft2.txt", "w") as f1:
		for tweetNo in tweet.keys():
			print(findMedian(len(likelihood[tweetNo])),file=f1)			
		
if __name__ == '__main__':
    main()

