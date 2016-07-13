# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:12:07 2016

@author: matt
"""
import matplotlib.pyplot as plt

#notes = ['E2 ', 'F2 ', 'F#2 ', 'G2 ', 'G#2 ', 'A3 ', 'A#3 ', 'B3 ', 'C3 ', 'C#3 ', 'D3 ', 'D#3 ',\
#        'E3 ', 'F3 ', 'F#3 ', 'G3 ', 'G#3 ', 'A4 ', 'A#4 ', 'B4 ', 'C4 ', 'C#4 ', 'D4 ', 'D#4 ',\
#        'E4 ', 'F4 ', 'F#4 ', 'G4 ', 'G#4 ', 'A5 ', 'A#5 ', 'B5 ', 'C5 ', 'C#5 ', 'D5 ', 'D#5 ',\
#        'E5 ', 'F5 ', 'F#5 ', 'G5 ', 'G#5 ', 'A6 ', 'A#6 ', 'B6 ', 'C6 ', 'C#6 ', 'D6 ', 'D#6 ',
#        'E6 ', 'F6 ', 'F#6 ', 'G6 ', 'G#6 ', 'A7 ', 'A#7 ', 'B7 ', 'C7 ', 'C#7 ', 'D7 ', 'D#7 ','']

def sortAndCount(myList):
    list2dictCount = dict((x, myList.count(x)) for x in myList)
    sortedDictCount = sorted(list2dictCount.items(), key = lambda x:(x[1], x[0]), reverse= True)
    sortedDictCountVal = [x[1] for x in sortedDictCount]
    sortedDictCountKey = [x[0] for x in sortedDictCount]
    return sortedDictCount, sortedDictCountVal, sortedDictCountKey

def stringShift(string, shift):
    return string[shift:] + string[:shift]
# Join all lists ============================
chordsTotal = []
for i in range(len(myChords)):
    chordsTotal = chordsTotal + myChords[i]
    

sortedChordsDict, sortedChordsDictVal, sortedChordsDictKey = sortAndCount(chordsTotal)
sumChords = float(sum(sortedChordsDictVal))
fracSortedChordsDictVal = [i/sumChords*100 for i in sortedChordsDictVal]

# Test chord progression for 1 set of chords
chordProgressionLen = 4
testChords = chordsTotal
chordProgression = [0]*(len(testChords)-chordProgressionLen)
mainChordProgression = [0]*(len(testChords)-chordProgressionLen)
chordTypeProgression = [0]*(len(testChords)-chordProgressionLen)
for i in range(len(testChords) - chordProgressionLen):
    chordProgression[i] = ''.join(testChords[i:i+chordProgressionLen])
    mainChordProgression[i] = testChords[i][0] + testChords[i+1][0] + testChords[i+2][0] + testChords[i+3][0]

#sortedMainChordProgDict, sortedMainChordProgDictVal, sortedMainChordProgDictKey = sortAndCount(mainChordProgression)
sortedMainChordProgDict, sortedMainChordProgDictVal, sortedMainChordProgDictKey = sortAndCount(chordProgression)

newSet = []
newVals = []
noEntries = 100
for j in range(len(sortedMainChordProgDictKey[:noEntries])):
    permutationsTmp = [stringShift(sortedMainChordProgDictKey[j],k) for k in range(len(sortedMainChordProgDictKey[j]))]
    if not any([[jj == x for x in newSet] for jj in permutationsTmp]):
        newSet.append(sortedMainChordProgDictKey[j])
        newVals.append(sortedMainChordProgDictVal[j])
        
plt.figure(4); plt.clf()
res = 20
plt.bar(range(len(newSet[:20])), newVals[:20], align='center')
plt.xticks(range(len(newVals[:20])), newSet[:20], rotation = 60)

#plt.figure(5)
#plt.pie(fracSortedChordsDictVal, labels = sortedChordsDictKey, autopct='%1.1f%%')





#noteCount =[0]*len(notes)
#
#for i in range(len(notes)):
#    for j in range(len(allSongPitch)):
#        noteCount[i] = noteCount[i] + allSongPitch[j].count(notes[i])
#
#chordCount = [0]*len(chords)
#chordIndex = [0]*len(chords)
#unfoundChord = 0
#
#i = 0
#for key in chords:
#    for j in range(len(allSongPitch)):
#        chordCount[i] = chordCount[i] + allSongPitch[j].count(key)
#    chordIndex[i] = chords[key]
#    i = i+1
#         
#while noteCount[-1] == 0:
#    noteCount.pop()
#
#plt.figure(1); plt.clf()
#plt.bar(range(len(noteCount)), noteCount)
#plt.xticks(range(len(noteCount)), list(notes[:len(noteCount)]), ha = 'left', rotation = 60)
#plt.figure(2); plt.clf()
#plt.bar(range(len(chordCount)), chordCount)
#plt.xticks(range(len(chordCount)), list(chordIndex), ha = 'left', rotation = 60)
#plt.draw()