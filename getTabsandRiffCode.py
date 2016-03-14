# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:18:19 2016

@author: matt
"""
# Import packages =============================================================

import requests
from lxml import html
# =============================================================================


# Helper functions ============================================================
def getTab(url):
    page = requests.get(url)
    tree= html.fromstring(page.content)
    myxpath = '//*[@id="cont"]/pre[2]/text()'
    tab = tree.xpath(myxpath)
    return tab

def getTree(band, page):
    if type(page) == int:
        page = str(page)
    bandURL = 'https://www.ultimate-guitar.com/search.php?band_name=' + band + \
        '&type%5B1%5D=200&type2%5B0%5D=40000&rating%5B4%5D=5&tuning%5Bstandard%5D=standard&page=' \
        + page + '&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'
    pageBand = requests.get(bandURL)
    return html.fromstring(pageBand.content)

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
# ============================================================================


band = 'metallica'

# Read first search page to get total number of pages in search result ========
page = '1'
tree1 = getTree(band, page)
pages = tree1.find_class('paging')
maxPage = len(list(pages[0].iter('a')))
print('Max Page: '+ str(maxPage))


# Get song result links from first page =======================================
songs = tree1.find_class('song result-link')
songLinks = []
for i1 in songs:
    songLinks.append(i1.get('href'))        

# Get song result links from remaining pages in search ========================
for i2 in range(maxPage -1):
    looppage = i2 + 2
    looptree = getTree(band, str(looppage))
    loopsongs = looptree.find_class('song result-link')
    for song in loopsongs:
        songLinks.append(song.get('href'))  

print('No of tabs: ' + str(len(songLinks)))

# Grab tabs from the individual web pages from the given links using getTab fn 
myTabs = []
for i3 in songLinks:
    myTabs.append(getTab(i3))


k = 0 # counter for number of good tabs
outerLoopCounter = 0 # counter for number of processed tabs
allSongNotes= [0]*len(songLinks) # initialize result list

for ii in range(len(songLinks)):
    tab = myTabs[ii][0]
    col1 = []
    tab = str(tab).split('\\n')
    tab = (tab[0].rstrip()).split('\n')
#    print(tab) # see tab
    
#   Grab first 3 lines of tab to determin if tabluture    
    for lineno, linestr in enumerate(tab, start = 0):
        try:
            col1.append(linestr[:3])
        except:
            col1.append(linestr[0])
            
#   See if first 3 chars contain common chars for tabluture
    firstCol = map(int, [x[:2] == '|-' or x[:2] == '||' or check4Strings(x) for x in col1])

#   Determines first line of set pf tablutures 
    firstLineCol = [0]*(lineno+2)
    for i in range(len(firstCol)-1):
        if firstCol[i] > 0 and firstCol[i+1] > 0:
            firstCol[i+1] = firstCol[i] + 1
            if mod(firstCol[i+1], 6) == 0: # Finds the end of the line of tabluture
                firstLineCol[i-4] = 1      # i-4 to et to the beginning of tabluture
                
#    tab.seek(0)
    rowtype = 0    
    E1notes = []; B2notes = []; G3notes = []; D4notes = []; A5notes = []; E6notes = []
    nummE1 = 0; nummB2 = 0; nummG3 = 0; nummD4 = 0; nummA5 = 0; nummE6 = 0
    
#   Iterate through each line
    for lineno, linestr in enumerate(tab, start=0):
        if firstLineCol[lineno] == 1:
            rowtype = 1
        elif rowtype == 6 or rowtype == 0:
            rowtype = 0
        else:
            rowtype = 1 + rowtype
#        print 'rowtype: ' + str(rowtype)
#        print "line number: " + str(lineno) + ": " + linestr.rstrip()
        
#       Iterate throuh each column in line 
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
#    print 'lines ' + str(lineno)
    
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
