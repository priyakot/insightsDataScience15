# example of program that calculates the total number of times each word has been tweeted.

from collections import Counter, defaultdict
import re
import sys
import random
import math
import os
import operator
import pickle

wordCount = Counter()

def tokenize(text):
	return text.split(' ')
    #return re.findall('[a-z0-9]+', text)

def readTrainingFile(fileName):
    vocab = defaultdict(int)

    with open(fileName,errors='ignore') as f:
        for line in f:
        	print(line)
        	for word in tokenize(line):
        		vocab[word] += 1 
        		wordCount[word] += 1
    return (vocab, wordCount)
    
def main():
	count = 0
	trainingFile = sys.argv[1]
	#modelFile = sys.argv[2]
	(vocab, wordCount) = readTrainingFile(trainingFile)
	for key, word in vocab.items():
		print("word: ", word,key)
	print("wordcount ",wordCount)
	print("Tweets dictionary: ",vocab)
	
if __name__ == '__main__':
    main()

