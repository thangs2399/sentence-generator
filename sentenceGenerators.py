# Solomon Thang
# project2 - ngrams
# sentenceGenerators.py
# CSC360
# Dr.Burhans
# 2.21.2022

############################## IMPORTS ##############################
import re # regex
import random

from ngrams import unigram, bigram, trigram 
############################## Sentence Generators ##############################


##### GENERATE SENTENCES USING UNIGRAM #####

def generateSentencesUnigram(wordTokens, tokensCount, num):
    """
        Function to generate sentences using unigram.
        
        Args:
            - wordTokens (type: dict) : word as keys and count as values
            - tokensCount (type: int) : total count of everytokens in the text
            - num (type: int) : num of sentences to generate
        
        returns:
            - sentences (type: list) : a list of sentences
    """
    ############# VARIABLES ##########
    
    # firstWord
    firstWord = True
    
    # to track of generated sentences
    generated = 0 
    curWord = "<s>"
    
    # used in picking the next word with highest probability
    somelist=[] # to store the items
    weightList = [] # to store the items' probability
    
    # used in generating sentences
    sentences = [] # list of sentences that is returned
    sentence = ""  # a string of sentence
    
    # regEx that is used to check last word (word ending with period)
    lastWordRE = re.compile(r".*[\.\?\!]$") # lastword
    
    # unigram (dict)
    ngram = unigram(wordTokens, tokensCount)
    
    nonWordRE = re.compile(r"\W") # used to check non-word using regex object
    
    ###############################################
    
    
    while (generated < num):
        
        # check to see if curWord is last word
        if (lastWordRE.search(curWord)):
            
            sentence = sentence + " " + curWord
            
            # do not add sentences that have less than 3 words
            if (not (len(sentence.split()) < 3)):
                
                sentences.append(sentence) # append the sentence
                generated += 1
            
            #reset sentence, curWord, and increment generated 
            sentence = ""
            curWord = "<s>"
            firstWord = True # new sentence
            
        else:
            
            curWordNext_dict = ngram
            
            for k, v in curWordNext_dict.items():
            
                somelist.append(k)
                weightList.append(v)
                
            
            if (curWord == "<s>" and firstWord):
                
                sentence += ""
                
                # uses choices method to get choice with higher probability
                curWord = random.choices(somelist, weightList)[0] # select random next word 
                
                # do not start sentence with non-word char
                while (nonWordRE.search(curWord)):
                    
                    curWord = random.choices(somelist, weightList)[0] # select random next word 
                
                firstWord = False
                    
            else:
                
                if (curWord != "\ufeff" and curWord != "<s>"): # remove \ufeff
                    
                    sentence = sentence + " " + curWord
                    
                # uses choices method to get choice with higher probability
                curWord = random.choices(somelist, weightList)[0] # select random next word
            
            # reset lists
            somelist.clear()
            weightList.clear()
        
    return sentences


##### GENERATE SENTENCES USING BIGRAM #####

def generateSentencesBigram(sentenceList, wordTokens, num):
    """
        Function to generate sentences using bigram.
        
        Args:
            - sentenceList (type: list) : list of all sentences from the text
            - wordTokens (type: dict) : word as keys and count as values
            - num (type: int) : num of sentences to generate
        
        returns:
            - sentences (type: list) : a list of sentences
    """
    
    ############# VARIABLES ##########
    
    # to track of generated sentences
    generated = 0
    oneLookBack = "<s>" # lookBack
    
    # used in picking the next word with highest probability
    somelist=[] # to store the items
    weightList = [] # to store the items' probability
    
    # used in generating sentences
    sentences = [] # list of sentences that is returned
    sentence = ""  # a string of sentence
    
    # regEx that is used to check last word (word ending with period)
    lastWordRE = re.compile(r".*[\.\?\!]$") # lastword
    
    # bigram ( dict )
    ngram = bigram(sentenceList, wordTokens)[0] # bigram
    
    
    nonWordRE = re.compile(r"\W") # used to check non-word using regex object
    
    ################################################################
    
    
    while (generated < num):
        
        # check to see if curWord is last word
        if (lastWordRE.search(oneLookBack)):
            
            sentence = sentence + " " + oneLookBack # append to sentence
            
            # only generate sentences that are have at least 3 words.
            if (not (len(sentence.split()) < 3)):
                
                sentences.append(sentence) # append the sentence
                generated += 1 # increment generated
            
            #reset sentence, curWord, and increment generated 
            sentence = ""
            oneLookBack = "<s>"
        
        else:
            
            nextWord_dict = ngram[oneLookBack] # dict of next words with probability after the word of oneLookBack's value
        
            # append keys and values to somelist and weightlist respectively
            # the goal of these two lists is to able to use random.choices() function
            # random.choices() randomly selects based on the weight of the options. So, item with higher weight has 
            # more probability than items with lesser weight
            for k, v in nextWord_dict.items():
            
                somelist.append(k)
                weightList.append(v)
                
            
            # if the oneLookBack is <s> then it is the beginning of the sentence
            if (oneLookBack == "<s>"):
                
                sentence += "" # needed??????????????
                
                # uses choices method to get choice with higher probability
                oneLookBack = random.choices(somelist, weightList)[0] # select random next word 
                
                while(nonWordRE.search(oneLookBack)): # don't start sentence with non-word char
                    
                    oneLookBack = random.choices(somelist, weightList)[0] # select random next word
                    
            else:
                
                if (oneLookBack != "\ufeff"): # remove \ufeff
                    
                    # if curWord to append to the sentence is "$" add a space between
                    if (oneLookBack == "$"):
                        
                        sentence = sentence + " " + oneLookBack
                    
                    # if curWord to append is non-word char
                    # do not add a space 
                    elif (nonWordRE.search(oneLookBack)):
                        
                        sentence += oneLookBack
                    
                    # otherwise add a space
                    else:
                        
                        sentence = sentence + " " + oneLookBack
                          
                # uses choices method to get choice with higher probability
                oneLookBack = random.choices(somelist, weightList)[0] # select random next word from the dict of next words
            
            # reset lists
            somelist.clear()
            weightList.clear()
        
    return sentences   # return the list of sentences



##### GENERATE SENTENCES USING TRIGRAM #####

def generateSentencesTrigram(sentenceList, wordTokens, num):
    """
        Function to generate sentences using trigram.
        
        Args:
            - sentenceList (type: list) : list of all sentences from the text
            - wordTokens (type: dict) : word as keys and count as values
            - num (type: int) : num of sentences to generate
        
        returns:
            - sentences (type: list) : a list of sentences
    """
    
    ############# VARIABLES ##########
    
    oldWords = [""] * 10 # save previous 10 words
    
    firstWord = True
    
    # to track of generated sentences
    generated = 0
    
    # two look back
    twoLookBack = ""
    
    # used in picking the next word with highest probability
    wordToPick_list = [] # list of tuples (two items) that will be used to pick for next word
    weightList = [] # this list is used to store wordToPick_list items' probability accordingly by indexes
    
    # used in generating sentences
    sentences = [] # list of sentences that is returned
    sentence = ""  # a string of sentence
    
    # regEx that is used to check last word (word ending with period)
    lastWordRE = re.compile(r".*[\.\?\!]$") # lastword
    
    # trigram ( dict )
    ngram = trigram(sentenceList, wordTokens)
    
    bigramDict = bigram(sentenceList, wordTokens)[1] # bigram with count
    
    
    nonWordRE = re.compile(r"\W") # used to check non-word using regex object
    
    ##########################################################################
    
    
    while (generated < num):
        
        # it is firstword if it's true ( = new sentence )
        if (firstWord):
            
            # pick tuples from bigramDict's keys that has "<s>" words 
            for k, v in bigramDict.items():
                
                if (not nonWordRE.search(k[1])): # do not start sentences with nonWord char
                    
                    if "<s>" in k:
                        
                        wordToPick_list.append(k)
                        weightList.append(v)

            # uses choices method to get choice with higher probability
            twoLookBack = random.choices(wordToPick_list, weightList)[0]
            
            # clear both lists
            wordToPick_list.clear()
            weightList.clear()
        
        # check to see if nextWord is last word
        if ( lastWordRE.search(twoLookBack[1])):
            
            # do not add a space if previous added word is a non-word char
            if (nonWordRE.search(twoLookBack[0])):
                
                sentence += twoLookBack[1]
            
            else:
                
                sentence = sentence + " " + twoLookBack[1]
            
            # only generate sentences that are have at least 3 words.
            if (not (len(sentence.split()) < 3)):
            
                sentences.append(sentence) # append the sentence
                generated += 1 # increment generated
            
            
            #reset sentence, curWord, and increment generated 
            sentence = ""
            firstWord = True
            twoLookBack = ""
            
        else:
            
            nextWords_dict = ngram[twoLookBack] # get dictionary of next words using twoLookBack as key
            
            # append keys and values to somelist and weightlist respectively
            # the goal of these two lists is to able to use random.choices() function
            # random.choices() randomly selects based on the weight of the options. So, item with higher weight has 
            # more probability than items with lesser weight
            for k, v in nextWords_dict.items():
            
                wordToPick_list.append(k)
                weightList.append(v)
                
                
            # beginning of sentence
            if ("<s>" in twoLookBack):
                
                sentence = sentence + " " + twoLookBack[1] # append it to sentence
                
                # uses choices method to get choice with higher probability
                nextWord = random.choices(wordToPick_list, weightList)[0] # select random next two words ( tuple )
                
                # make a tuple (2 elements) using second word from twoLookBack as first element and nextWord as the second element
                # then update that tuple as the new "twoLookBack"
                atuple = (twoLookBack[1], nextWord)
                twoLookBack = atuple
                
                firstWord = False
                    
            else:
   
                if ("\ufeff" not in twoLookBack): # remove \ufeff
                    
                    # if curWord to append to the sentence is "$" add a space between
                    if (twoLookBack[1] == "$"):
                        
                        sentence = sentence + " " + twoLookBack[1]
                    
                    # if curWord to append is non-word char
                    # do not add a space 
                    elif (nonWordRE.search(twoLookBack[1])):
                        
                        sentence += twoLookBack[1]
                    
                    # otherwise add a space
                    else:
                        
                        sentence = sentence + " " + twoLookBack[1]
                
                # uses choices method to get choice with higher probability
                nextWord = random.choices(wordToPick_list, weightList)[0] # select random next word
                
                # make a tuple (2 elements) using second word from twoLookBack as first element and nextWord as the second element
                # then update that tuple as the new "twoLookBack"
                atuple = (twoLookBack[1], nextWord)
                twoLookBack = atuple
            
            # reset lists
            wordToPick_list.clear()
            weightList.clear()
        
        
        
    return sentences   