# Sentence Generator

## Summary
> A sentence generator using n-gram model. This program have three models that can be used to generate sentences: uni-gram, bi-gram, and tri-gram. It can be trained using some text files and the program will generate sentences using those data. The quality of sentences that are generated will be depends on the size and quality of the input data, and the n-gram model it is used.    

> In my case, I use "The Project Gutenberg eBook of The Complete Works of William Shakespeare, by William Shakespeare" which includes all the works of Shakespeare. This text file can be found in the "data" folder.

## Outputs

![uni-gram output screenshot](./screen-shots/unigram.jpg?raw=true "uni-gram output")
> uni-gram model's output   

![bi-gram output screenshot](./screen-shots/bigram.jpg?raw=true "uni-gram output")
> bi-gram model's output   

![tri-gram output screenshot](./screen-shots/trigram.jpg?raw=true "tri-gram output")
> tri-gram model's output   

## Guide to run the program

> The program takes at least three arguments, 'ngram model', 'number of sentences to generate', and 'textfiles', in that order. As said above, there are only three ngram models in this program (1. unigram, 2. bigram, 3. trigram). There can be multiple textfiles to train the program, they just have be after the 'number of sentences to generate' argument.   

> Below is an example. 

```
'''
    main.py -> the main program name
    3       ->  uses tri-gram model
    10      ->  # sentences to generate
    
    'dracula.txt' and 'macbeth.txt' files are used to train the program.
'''
python3 main.py 3 10 dracula.txt macbeth.txt
```