# Solomon Thang
# project2 - ngrams
# someFunctions.py
# CSC360
# Dr.Burhans
# 2.21.2022

############################## IMPORTS ##############################
from operator import ge
import re
import random

############################## VARIABLES ##############################

# endOfSentence
endOfSentence = [ ".", "!", "?" ]

# punctuation
punctuation = [
    ".", ",", "?", ";", "!", ":", "'",
    "(", ")", "[", "]", "\"", "-", "_",
    "/", "\\", "@", "{", "}", "*"

]

############################## FUNCTIONS ##############################

# count how many lines in a textfile
def countLines(someFile):
    """
        This function will count how many lines are there in a textfile

        Args: someFile ( type: file )

        Returns: lines ( type: int ) : count of lines in a textfile
    """
    
    INF = open(someFile, "r", encoding = "utf-8") # open file
    lines = len(INF.readlines()) # line count
    INF.close() # close file
    
    return lines # return the count of lines in the text file



# read whole text of a textfile
def readWholetext(someFile):
    """
        This function will read whole text of a textfile
        
        Args: someFile ( type: file )
        
        Returns: normalizedText ( type: string ) : wholetext of a text file
    """
    
    normalizedText = ""
    
    INF = open(someFile, "r", encoding = "utf-8") # open file
    wholeText = " ".join(INF.read().split("\n")) # split with "\n" ( removes "\n" ) and then join with " "
    
    # extract non-words with thier count
    nonWords = extractNonWord(wholeText)
    
    eos = [".", "!", "?"]
    
    # add space to both ends of char if it is non-word
    for char in wholeText: # go over each char in text
        
        
        if char in nonWords:   # if its non-word char 
            
            if char not in eos: # if char is not end of sentence like : ., !, ?
                    
                char = " " + char + " " # add space on both ends of char
            
            elif char in eos: # if char is end of sentence like : ., !, ?
                
                char = char + " " # add just one space at the end
        
        normalizedText += char
    
    INF.close() # close file
    
    return normalizedText # return the normalized wholetext of the textfile



# tokenization of sentences
def tokenizeSentences(someText):
    """
        This function will tokenize sentences on a given text
        
        Args: someText ( type: string )
        
        Returns: sentences ( type: list ) : list of sentences from a given text
    """
    sentencesList = [] # list
    sentence = "" # a sentence
    
    for char in someText:
        
        # if current letter is punction, then sentence ends.
        # and append it to the "sentences" list
        if char in endOfSentence:
            
            sentence += char # concatenate
            sentencesList.append(sentence.strip()) # append to the sentences
            sentence = "" # reset the sentence variables
        else:
            sentence += char # concatenate
    
    # add <s> for beginning of each sentences
    for i in range(len(sentencesList)):
        
        sentencesList[i] = "<s> " + sentencesList[i] 
    
    return sentencesList # return the list



# tokenization of words
def tokenizeWords(sentenceList):
    """
        This function will tokenize words given a text
        
        Args: someText ( type: string )
        
        Returns: tokensDict ( type: list ) : list of sentences from a given text
    """
    
    wordsDict = {} # dict with word as key and count as value
    

    for sentence in sentenceList:
        
        
        for word in sentence.split():
            
            # if word is not yet in the dictionary, then add it and set the count to 1
            if word not in wordsDict.keys(): 
                
                wordsDict[word] = 1;
            
            # if word is already in the dictionary, then just increment the count of the word
            elif word in wordsDict.keys():
                
                wordsDict[word] += 1;

    return wordsDict # return the dictionary



# remove certain item from list
def removeItem(someList, item):
    """
        This function will remove every item from the list that matches with the item, second arg.
        
        Args: someList (type: list), item (type: any)
        
        Returns: modifiedList (type: list) :  a list of modified list
    """
    
    # remove item that matches with "item" using list comprehension
    modifiedList = [i for i in someList if i != item] 
    
    return modifiedList # return the list



# extract all punctuations ( non-words ) from the text
def extractNonWord(someText):
    """
        This function will extract non-word characters from the text unqiuely except spaces.
        
        Args: someText ( type: string )
        
        Returns: modifiedList ( type : dict ) : a dict of unqiue non-word characters with value of thier count
    """
    modifiedList = []
    
    nonWordRE = re.compile(r"\W") # remove non-word using regex object
    nonSpaceRE = re.compile(r"[^ ]") # remove non-word using regex object
    
    modifiedListX = nonWordRE.findall(someText) # extract all non-word characters
    modifiedListX = nonSpaceRE.findall(" ".join(modifiedListX)) # remove spaces
    
    # remove duplicates
    for i in modifiedListX:
        
        if i not in modifiedList:
            
            modifiedList.append(i)
    
    return modifiedList # return the dict

