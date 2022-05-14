# Solomon Thang
# project2 - ngrams
# main.py
# CSC360
# Dr.Burhans
# 2.21.2022

############################## IMPORTS ##############################
from operator import mod
import sys
import re

# local
import someFunctions as SF
import sentenceGenerators as SG
import ngrams

############################## RAISE ERROR ##############################

if len(sys.argv) < 3: # if there are less than 3 args
    raise ValueError("Insufficient arguments to run program")

############################## VARIABLES ##############################

# sys
model = int(sys.argv[1])
numSent = int(sys.argv[2])
infiles = sys.argv[3:]

# text related
lines = 0 # count of lines for each textfile
wholeText = "" # wholetext of each textfile

sentenceTokens = [] # sentences of each textfile
wordTokens = {} # words of each textfile with occurence counts

sentenceCount = {} # count of sentences of each textfile
vocabCount = 0 # count of unique words(token) of each textfile
tokenCount = 0# count of total words(token) of each textfile

# N-gram
ngram = {}

############################## MAIN PROGRAM ##############################

# count lines of each textfile
for file in infiles:
    
    lines += SF.countLines(file)

# read whole text of each textfile
for file in infiles:
    
    wholeText += SF.readWholetext(file)


# iterate over files and tokenize sentences
for file in infiles:
    
    sentenceTokens = SF.tokenizeSentences(wholeText)
    sentenceCount = len(sentenceTokens) # sentence count assigned

# iterate over files and tokenize words, and also get the count of vocab and token counts

    
# tokenize words
words = SF.tokenizeWords(sentenceTokens)

wordTokens = words

# vocab count
vocabCount = len(wordTokens) 

# count the total tokens in the file(s)
for value in wordTokens.values():
    
    tokenCount += value 



############################################## generate sentences using Unigram (OUTPUT) ##############################################

print()
print()
print(222 * "*")
print()
print(f"There are {lines} lines, {vocabCount} vocabs & {tokenCount} tokens and {sentenceCount} sentences in this file(s), \"{infiles}\".")
print()
print(222 * "*")
print()
print()
print(f"Generating {numSent} sentences.....")
print()

count = 1 # to number the sentences

# generate sentences using Unigram
if (model == 1):
    
    sentencesToGenerate = SG.generateSentencesUnigram(wordTokens, tokenCount, numSent)

    for s in sentencesToGenerate:
        
        print(f" ({count})", end="")
        print(s) # print out sentences one by one
        print()
        count += 1

# generate sentences using Bigram
elif (model == 2):
    
    sentencesToGenerate = SG.generateSentencesBigram(sentenceTokens, wordTokens, numSent)

    for s in sentencesToGenerate:
        
        print(f" ({count})", end="")
        print(s) # print out sentences one by one
        print()
        count += 1

# generate sentences using Trigram
elif (model == 3):

    sentencesToGenerate = SG.generateSentencesTrigram(sentenceTokens, wordTokens, numSent)

    for s in sentencesToGenerate:
        
        print(f" ({count})", end="")
        print(s) # print out sentences one by one
        print()
        count += 1

print()
print(222 * "-")

