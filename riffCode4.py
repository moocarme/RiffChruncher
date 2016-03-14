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
#tabs = f
strings= ['e','a','d','g','b','E','A','D','G','B']

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def check4Strings(myStr):
    t1 = any([x == i for x in myStr for i in strings])
    t2 = any([x == '|' or x == '-' or is_int(x) for x in myStr])
    return t1 and t2

k = 0
outerLoopCounter = 0

allSongNotes= [0]*len(songLinks)
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
            if mod(firstCol[i+1], 6) == 0: # Finds the end of the line
                firstLineCol[i-4] = 1      # i-4 to et to the beginning of the bar
    #print(firstCol, firstLineCol)
            
#    tab.seek(0)
    rowtype = 0
    
    E1notes = []
    B2notes = []
    G3notes = []
    D4notes = []
    A5notes = []
    E6notes = []
    nummE1 = 0
    nummB2 = 0
    nummG3 = 0
    nummD4 = 0
    nummA5 = 0
    nummE6 = 0
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
                nummE1 = nummE1 + 1
            elif rowtype == 2: #'2B'
                B2notes.append(alphabetizeFrets(rowtype, str(linecol)))                
                nummB2 = nummB2 + 1
            elif rowtype == 3: #'3G'
                G3notes.append(alphabetizeFrets(rowtype, str(linecol)))
                nummG3 = nummG3 + 1
            elif rowtype == 4: #'4D'
                D4notes.append(alphabetizeFrets(rowtype, str(linecol)))                
                nummD4 = nummD4 + 1
            elif rowtype == 5: #'5A'
                A5notes.append(alphabetizeFrets(rowtype, str(linecol)))                
                nummA5 = nummA5 + 1
            elif rowtype == 6: #'6E'
                E6notes.append(alphabetizeFrets(rowtype, str(linecol)))                
                nummE6 = nummE6 + 1
            
    
    print 'cols ' + '  ' + str(nummE1) + '  ' + str(nummB2) + '  ' + str(nummG3) + '  ' + str(nummD4) + '  ' + str(nummA5) + '  ' + str(nummE6)
    print 'lines ' + str(lineno)
    
    allNotes=[]
    if all([i == nummE1 for i in [nummB2, nummG3, nummD4, nummA5, nummE6]]) and nummE1 != 0:
        for i in range(nummE1):
            try:
                inputNote = ''  
                if E1notes[i][1] != '-':
                    inputNote = inputNote + E1notes[i]
                if B2notes[i][1] != '-':
                    inputNote = inputNote + B2notes[i]
                if G3notes[i][1] != '-':
                    inputNote = inputNote + G3notes[i]
                if D4notes[i][1] != '-':
                    inputNote = inputNote + D4notes[i]
                if A5notes[i][1] != '-':
                    inputNote = inputNote + A5notes[i]
                if E6notes[i][1] != '-':
                    inputNote = inputNote + E6notes[i]
                if inputNote and inputNote !='1b2c3d4e5f6g': 
                    allNotes.append(inputNote)   
                
            except:
                print('Some error')
        allSongNotes[k] = allNotes
        k = k + 1
    else:
        print('Columns in tab not same length')
    outerLoopCounter = outerLoopCounter +1
print('Total tabs = ' + str(k) + ' out of ' + str(outerLoopCounter))

#f.close()
