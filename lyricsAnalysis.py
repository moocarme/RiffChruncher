# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:49:11 2016

@author: matt-666
"""

import matplotlib.pyplot as plt
from collections import Counter
from nltk.corpus import stopwords
import random
import pickle

# = Helper Functions =========================================================

def WeightedPick(d):
    r = random.uniform(0, sum(d.values()))
    s = 0.0
    for k, w in d.iteritems():
        s += w
        if r < s: return k
    return k

# ================================================================

# = Post-scrape ===============================================================

# = grab from pickle file
songLyrics = pickle.load(open("songLyrics.p", "rb"))

# = compress into onle long list
flatSongLyrics = [item for sublist in songLyrics for item in sublist]

# = remove stopwords
flatSongLyrics_noStopwords = [word for word in flatSongLyrics if word not in (stopwords.words('english'))]

# = the word 'chorus' remains, so we remove
flatSongLyrics_noStopwords[:]  = [x for x in flatSongLyrics_noStopwords if x != 'chorus']

#Count all instances of words that are not stop words
wordCount = Counter(flatSongLyrics_noStopwords)

# = sort dictionary by value
sortedKeys, sortedVals = [], []
for key, value in sorted(wordCount.iteritems(), key=lambda (k,v): (v,k)):
    sortedKeys.append(key.title())
    sortedVals.append(value)
# = have to reverse since the sort is in ascending order
sortedKeys.reverse(); sortedVals.reverse()

# = Plot in bar chart        
plt.figure(44); plt.clf(); res = 40
plt.bar(range(res), sortedVals[:res]/sum(sortedVals)*100., align='center')
plt.xticks(range(res), sortedKeys[:res], rotation = 60)
plt.xlabel('Lyric'); plt.ylabel('Count (%)')

# = Country-Robo lyric machine ===============================================
# = Uses a naive-Bayes approach to choose the likely next word to create a lyric

# = Create dictionary of dictionary to see what words come are likely to come after each one
lyricDict= {}
for song in songLyrics:
    for word in range(len(song)-1):
        try:
            lyricDict.setdefault(song[word], {})[song[word+1]] += 1
        except KeyError: # if key doesnt exist
            lyricDict.setdefault(song[word], {})[song[word+1]] = 1

# initiliaxe with random word
robo_lyric = [random.choice(lyricDict.keys())]
lyricLen = 10 # length of lyric
for i in range(lyricLen):
    robo_lyric.append(WeightedPick(lyricDict[robo_lyric[-1]]))
robo_lyric[0] = robo_lyric[0].title() 
robo_lyric = ' '.join(robo_lyric)
print(robo_lyric)
# Actual Lyric '27 seconds on a party bone is the party for me' XD XD XD
