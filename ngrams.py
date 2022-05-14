# Solomon Thang
# project2 - ngrams
# ngrams.py
# CSC360
# Dr.Burhans
# 2.21.2022


############################## IMPORTS ##############################

############################## N-GRAMS ##############################

# selectionSort
def selectionSort(alist):
    """
       This is selection sort.
    """
    for i in range(len(alist)):
        
        min_index = i
        
        for j in range(i+1, len(alist)):
            
            if (alist[min_index][2] > alist[j][2]):
                
                min_index = j
        
        alist[i], alist[min_index] = alist[min_index], alist[i] # swap
    
    return alist # return sorted list

# Unigram
def unigram(wordTokens, tokenCount):
    """
    This is function unigram. It will take word tokens (dict) and tokenCount (int) a as arguments and will return a dict
    with unigrams as keys and probability as its values.

    Args:
        wordTokens (_type: dict): a dict of unique words in the textfile with count
        vocabCount ( type: int) : count of all tokens in the textfile

    Returns:
        unigram_dict (_type: dict_) : unigram as key and probability of the unigram as its value
    """
    
    # variables
    unigram_dict = {}
    alist = []
    
    # caculate probabilites 
    for key, value in wordTokens.items():
        
        probability = round((value/tokenCount), 5) # divide to get probability and round off to the hundred
        
        x = [key, value, probability]
        
        alist.append(x)
    
    # convert into dict with word as key and probabilty as its value
    for i in alist:
        
        unigram_dict[i[0]] = i[2]
    
    return unigram_dict # return unigram

    
# Bigram
def bigram(sentenceList, wordTokens):
    """
    This is function for bigram. It will take sentenceList (list) and wordTokens (dict) a as arguments and will return a nested dict with
    a bigram (tuple) as key and probability as the value.

    Args:
        sentenceList (type : list) : a list of sentences
        wordTokens (_type: dict): a dict of unique words in the textfile with count

    Returns: a tuple - ( bigram_dict, someDict )
        bigram_dict (_type: dict) : a dictionary of bigrams - current word as keys and a dict as value. In the inner dict, keys are words after
        current word with probabilty of each as values
        someDict (type: dict) : a dictionary of bigram with words as keys and count of those words as values
    """
    
    # variables
    someDict = {} 
    bigram_dict = {}
    someList = []
    
    # get bigrams in tuples
    for sentence in sentenceList:
        
        sentence = sentence.split()
        
        for i in range(len(sentence)-1):
            
            atuple = (sentence[i], sentence[i+1])
            someList.append(atuple)
    
    # calculate count for duplicates
    for x in someList:
        
        if x in someDict.keys():
            
            someDict[x] += 1
        
        elif x not in someDict.keys():
            
            someDict[x] = 1    
            
    someList.clear() # clear someList
    
    # caculate probabilites 
    for key, value in someDict.items():
        
        probability = round((value/wordTokens[key[0]]), 5) # divide to get probability and round off to the hundred
        
        alist = [key, value, probability]
        
        someList.append(alist)
    
    # convert into nested dict
    # the key is current word, value with nested dict
    # in the nested dict, keys are the next word after current word with probabilies of each as values
    for i in someList:
        
        key = i[0][0] # current word
        value = i[0][1] # the next word
        probability = i[2]
        
        if key not in bigram_dict.keys():
            
            bigram_dict[key] = {value: probability}
        
        else:
            
            bigram_dict[key][value] = probability # add into inner dict
    
    return bigram_dict, someDict # return bigram


# Trigram
def trigram(sentenceList, wordTokens):
    """
    This is function for bigram. It will take sentenceList (list) and wordTokens (dict) a as arguments and will return a nested dict with
    current word as key and an inner dict as value. In the inner dict, the key is the next two word (tuple) after the current word and the probability of each
    as values.

    Args:
        sentenceList (type : list) : a list of sentences
        wordTokens (_type: dict): a dict of unique words in the textfile with count

    Returns:
        trigram_dict (_type: dict) : a dictionary of bigrams - current word as keys and an inner dict as values.In the inner dict, keys are two words (tuple) and values are
        another dictionary. The keys in this dictionary are the words that could comes after the said tuple of two words and the probability as the values.
    """
    
    # variables
    
    someList = [] # used to store a tuple of three words, including duplicates
    someDict = {} # used in calculating the count of duplicates of tuple of three words
    
    trigram_dict = {} # trigram
    
    bigramDict = bigram(sentenceList, wordTokens)[1] # bigram with count
    
    # get bigrams in tuples
    for sentence in sentenceList:
        
        # split into list of words
        sentence = sentence.split()
        
        for i in range(len(sentence)-2):
            
            # make tuple of three words
            atuple = (sentence[i], sentence[i+1], sentence[i+2])
            someList.append(atuple) # append it to the someList
    
    # calculate count for duplicates
    for x in someList:
        
        # if it is duplicate, increment count by 1
        if x in someDict.keys():
            
            someDict[x] += 1
        
        # if it is not duplicate, store in someDict and set value to 1
        elif x not in someDict.keys():
            
            someDict[x] = 1    
            
    someList.clear() # clear someList
    
    # caculate probabilites 
    # key in here is the a tuple with 3 words
    # value is the count or occurence of the key (tuple)
    for key, value in someDict.items():
        
        # atuple of first two words in the 3 words tuple
        atuple = (key[0], key[1])
        
        # get the count of occurences of the the first two words
        # using the bigramDict - this is a dictionary with a tuple (two words) as key and count of it as value-
        # from the bigram function
        lookBackCount = bigramDict[atuple]
        
        probability = round((value/lookBackCount), 5) # divide to get probability and round off to the hundred
        
        # create a list of key, value and prob
        alist = [key, value, probability]
        
        someList.append(alist) # append it to someList
    
    # convert into nested dict
    # the key is the twoLookBack, value with nested dict
    # in the nested dict, keys are the next the words after the twoLookBack with probabilies of each as values
    for i in someList:
        
        key = (i[0][0], i[0][1]) # previous two word
        value = i[0][2] # next word or the third word
        probability = i[2] # probability of it
        
        # if the twoLookBack is not already in the trigram_dict
        # add dict of {nextword: probability} as value and use key (twoLookBack) as the as the key
        if key not in trigram_dict.keys():
            
            trigram_dict[key] = {value: probability}
        
        else:
            
            trigram_dict[key][value] = probability # add into inner dict
        
        
    return trigram_dict # return trigram

