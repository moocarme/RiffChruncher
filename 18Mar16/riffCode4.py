# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:42:56 2016
This differs from riffCode2.py as the lines do not have to indicate the string 
tuning and assumes standard tuning
@author: matt
"""

def alphabetizeFrets(StringNo, fretNo):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l', \
             'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if type(StringNo) == int:
        StringNo = str(StringNo)
    try:
        alphFret = alphabet[int(fretNo)]
    except ValueError:
        alphFret = '-'    
    return StringNo + alphFret
    
def fret2note(StringNo, fretNo):
    try:
        fretNo = int(fretNo)
    except ValueError:
        index = 0
        fretNo = -1
    notes = ['E2 ', 'F2 ', 'F#2 ', 'G2 ', 'G#2 ', 'A3 ', 'A#3 ', 'B3 ', 'C3 ', 'C#3 ', 'D3 ', 'D#3 ',\
        'E3 ', 'F3 ', 'F#3 ', 'G3 ', 'G#3 ', 'A4 ', 'A#4 ', 'B4 ', 'C4 ', 'C#4 ', 'D4 ', 'D#4 ',\
        'E4 ', 'F4 ', 'F#4 ', 'G4 ', 'G#4 ', 'A5 ', 'A#5 ', 'B5 ', 'C5 ', 'C#5 ', 'D5 ', 'D#5 ',\
        'E5 ', 'F5 ', 'F#5 ', 'G5 ', 'G#5 ', 'A6 ', 'A#6 ', 'B6 ', 'C6 ', 'C#6 ', 'D6 ', 'D#6 ',
        'E6 ', 'F6 ', 'F#6 ', 'G6 ', 'G#6 ', 'A7 ', 'A#7 ', 'B7 ', 'C7 ', 'C#7 ', 'D7 ', 'D#7 ','']
    if abs(fretNo) >= len(notes):
        fretNo = fretNo%len(notes)
    if StringNo == 6:  # low E string
        index = 0
    elif StringNo == 5: # A string
        index = 5
    elif StringNo == 4: # G string
        index = 10
    elif StringNo == 3: # D string
        index = 15
    elif StringNo == 2: # A string
        index = 19   
    elif StringNo == 1: # A string
        index = 24 
    return notes[index + fretNo]
    
#tabs = f

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

strings= ['e','a','d','g','b','E','A','D','G','B']
def check4Strings(myStr):
    t1 = any([x == i for x in myStr for i in strings])
    t2 = any([x == '|' or x == '-' or is_int(x) for x in myStr])
    return t1 and t2

k = 0
outerLoopCounter = 0

allSongNotes, allSongPitch = [],[]
for ii in range(len(songLinks)):
    tab = myTabs[ii][0]
    col1 = []
    tab = str(tab).split('\\n')
    tab = (tab[0].rstrip()).split('\n')
#    print(tab)
    for lineno, linestr in enumerate(tab, start = 0):
        try:
            col1.append(linestr[:3])
        except:
            col1.append(linestr[0])
            
    firstCol = map(int, [x[:2] == '|-' or x[:2] == '||' or check4Strings(x) for x in col1])
    
    firstLineCol = [0]*(lineno+2)
    for i in range(len(firstCol)-1):
        count = 0
        if firstCol[i] > 0 and firstCol[i+1] > 0:
            firstCol[i+1] = firstCol[i] + 1
            if firstCol[i+1] % 6 == 0: # Finds the end of the line
                firstLineCol[i-4] = 1      # i-4 to et to the beginning of the bar
    #print(firstCol, firstLineCol)
            
#    tab.seek(0)
    rowtype = 0
    E1notes, B2notes, G3notes, D4notes, A5notes, E6notes = [], [], [], [], [], []
    E1pitch, B2pitch, G3pitch, D4pitch, A5pitch, E6pitch = [], [], [], [], [], [] 
    nummE1, nummB2, nummG3, nummD4, nummA5, nummE6 = 0, 0, 0, 0, 0, 0
    
    for lineno, linestr in enumerate(tab, start=0):
    #    rowtype = linestr[0] #what string, what type of  data
        if firstLineCol[lineno] == 1:
            rowtype = 1
        elif rowtype == 6 or rowtype == 0:
            rowtype = 0
        else:
            rowtype = 1 + rowtype
#        print 'rowtype: ' + str(rowtype)
#        print "line number: " + str(lineno) + ": " + linestr.rstrip()
        
        for colno, linecol in enumerate(linestr):
#            print "line number: " + str(lineno) + 'rowtype: ' + str(rowtype) +" col number: " + str(colno) + ": " + linecol.rstrip()
    
            if rowtype == 1: #'1E'
                E1notes.append(alphabetizeFrets(rowtype, str(linecol)))
                E1pitch.append(fret2note(rowtype, linecol))
                nummE1 = nummE1 + 1
            elif rowtype == 2: #'2B'
                B2notes.append(alphabetizeFrets(rowtype, str(linecol))) 
                B2pitch.append(fret2note(rowtype, linecol))
                nummB2 = nummB2 + 1
            elif rowtype == 3: #'3G'
                G3notes.append(alphabetizeFrets(rowtype, str(linecol)))
                G3pitch.append(fret2note(rowtype, linecol))
                nummG3 = nummG3 + 1
            elif rowtype == 4: #'4D'
                D4notes.append(alphabetizeFrets(rowtype, str(linecol)))   
                D4pitch.append(fret2note(rowtype, linecol))
                nummD4 = nummD4 + 1
            elif rowtype == 5: #'5A'
                A5notes.append(alphabetizeFrets(rowtype, str(linecol)))   
                A5pitch.append(fret2note(rowtype, linecol))
                nummA5 = nummA5 + 1
            elif rowtype == 6: #'6E'
                E6notes.append(alphabetizeFrets(rowtype, str(linecol)))  
                E6pitch.append(fret2note(rowtype, linecol))
                nummE6 = nummE6 + 1
            
    
    print 'cols ' + '  ' + str(nummE1) + '  ' + str(nummB2) + '  ' + str(nummG3) + '  ' + str(nummD4) + '  ' + str(nummA5) + '  ' + str(nummE6)
    print 'lines ' + str(lineno)
    
    allNotes, allPitch = [],[]
    if all([i == nummE1 for i in [nummB2, nummG3, nummD4, nummA5, nummE6]]) and nummE1 != 0:
        for i in range(nummE1):
            try:
                inputNote, inputPitch = '',''  
                if E1notes[i][1] != '-':
                    inputNote = inputNote + E1notes[i]
                    inputPitch = inputPitch + E1pitch[i]
                if B2notes[i][1] != '-':
                    inputNote = inputNote + B2notes[i]
                    inputPitch = inputPitch + B2pitch[i]
                if G3notes[i][1] != '-':
                    inputNote = inputNote + G3notes[i]
                    inputPitch = inputPitch + G3pitch[i]
                if D4notes[i][1] != '-':
                    inputNote = inputNote + D4notes[i]
                    inputPitch = inputPitch + D4pitch[i]
                if A5notes[i][1] != '-':
                    inputNote = inputNote + A5notes[i]
                    inputPitch = inputPitch + A5pitch[i]
                if E6notes[i][1] != '-':
                    inputNote = inputNote + E6notes[i]
                    inputPitch = inputPitch + E6pitch[i]
                if inputNote and inputNote !='1b2c3d4e5f6g': 
                    allNotes.append(inputNote)  
                    allPitch.append(inputPitch)
                
            except:
                print('Some error')
#Count instances of notes        
        d1 = dict((x, allPitch.count(x)) for x in allPitch)
#        plt.bar(range(len(d1)), d1.values())
#        plt.xticks(range(len(d1)), list(d1.keys()))
        allSongNotes.append(allNotes)
        allSongPitch.append(allPitch)
        k = k + 1
    else:
        print('Columns in tab not same length')
    outerLoopCounter = outerLoopCounter +1
print('Total tabs = ' + str(k) + ' out of ' + str(outerLoopCounter))

#f.close()