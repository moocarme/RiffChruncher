# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:55:53 2016
Plotting independent notes
@author: matt
"""

notes = ['E2 ', 'F2 ', 'F#2 ', 'G2 ', 'G#2 ', 'A3 ', 'A#3 ', 'B3 ', 'C3 ', 'C#3 ', 'D3 ', 'D#3 ',\
        'E3 ', 'F3 ', 'F#3 ', 'G3 ', 'G#3 ', 'A4 ', 'A#4 ', 'B4 ', 'C4 ', 'C#4 ', 'D4 ', 'D#4 ',\
        'E4 ', 'F4 ', 'F#4 ', 'G4 ', 'G#4 ', 'A5 ', 'A#5 ', 'B5 ', 'C5 ', 'C#5 ', 'D5 ', 'D#5 ',\
        'E5 ', 'F5 ', 'F#5 ', 'G5 ', 'G#5 ', 'A6 ', 'A#6 ', 'B6 ', 'C6 ', 'C#6 ', 'D6 ', 'D#6 ',
        'E6 ', 'F6 ', 'F#6 ', 'G6 ', 'G#6 ', 'A7 ', 'A#7 ', 'B7 ', 'C7 ', 'C#7 ', 'D7 ', 'D#7 ','']
frets = 25

E1, B2, G3, D4, A5, E6 = [0]*len(notes), [0]*len(notes), [0]*len(notes), [0]*len(notes), [0]*len(notes), [0]*len(notes)
E6[:frets] = [1 for i in range(frets)]
A5[5:frets+5] = [1 for i in range(frets)]
D4[10:frets+10] = [1 for i in range(frets)]
G3[15:frets+15] = [1 for i in range(frets)]
B2[19:frets+19] = [1 for i in range(frets)]
E1[24:frets+24] = [1 for i in range(frets)]
dependentNotes = [E1[i] + B2[i] + G3[i] + D4[i] + A5[i] + E6[i] for i in range(len(E1))]

#while dependentNotes[-1] == 0:
#    dependentNotes.pop()

plt.figure(3); plt.clf()
plt.bar(range(len(dependentNotes)), dependentNotes)
plt.xticks(range(len(dependentNotes)), list(notes[:len(dependentNotes)]), ha = 'left', rotation = 60)
