# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 19:40:45 2016

@author: Matt
"""
notes = ['E2 ', 'F2 ', 'F#2 ', 'G2 ', 'G#2 ', 'A2 ', 'A#2 ', 'B2 ', 'C2 ', 'C#2 ', 'D2 ', 'D#2 ',\
        'E3 ', 'F3 ', 'F#3 ', 'G3 ', 'G#3 ', 'A3 ', 'A#3 ', 'B3 ', 'C3 ', 'C#3 ', 'D3 ', 'D#3 ',\
        'E4 ', 'F4 ', 'F#4 ', 'G4 ', 'G#4 ', 'A4 ', 'A#4 ', 'B4 ', 'C4 ', 'C#4 ', 'D4 ', 'D#4 ',\
        'E5 ', 'F5 ', 'F#5 ', 'G5 ', 'G#5 ', 'A5 ', 'A#5 ', 'B5 ', 'C5 ', 'C#5 ', 'D5 ', 'D#5 ',
        'E6 ', 'F6 ', 'F#6 ', 'G6 ', 'G#6 ', 'A6 ', 'A#6 ', 'B6 ', 'C6 ', 'C#6 ', 'D6 ', 'D#6 ','']

noteCount =[0]*len(notes)
for i in range(len(notes)):
    for j in range(len(allSongPitch)):
        noteCount[i] = noteCount[i] + allSongPitch[j].count(notes[i])

while noteCount[-1] == 0:
    noteCount.pop()

plt.figure(1); plt.clf()
plt.bar(range(len(noteCount)), noteCount)
plt.xticks(range(len(noteCount)), list(notes[:len(noteCount)]), ha = 'left', rotation = 60)
plt.draw()