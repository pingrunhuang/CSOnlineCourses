"""
Document: a sequence of words
Word: string of chars
Idea: how to measure the similarity between 2 docs? Calculate the shared words 
Solution: document represented by a word of vector (D[w] = num of words occured in the doc)
"""
import numpy
import string

translation_table = {}
for x in string.punctuation:
    translation_table.update({x: " "})
for x in string.ascii_uppercase:
    translation_table.update({x: x.lower()})

def preprocess(path):
    word_count = {}
    def replace(line):
        pass

    def wordCount(line_list):
        for x in line_list:
            if word_count.get(x):
                word_count[x] += 1
            else:
                word_count[x] = 1
    
    def toWordVector():
        pass


def wordCount(doc):
    """
    """
    pass

def computeDotProduct(v1,v2):
    """
    Compute the similarity between 2 word of vectors here 
    """

def computeAngle():
    pass