# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 11:42:56 2016

@author: matt
"""

#import requests, pprint, json, pymssql, psutil, urllib
#import time, os, string, sys, time
#import pymssql
#
#mssql_db = pymssql.connect(host='localhost:1450',  user='sa', password='****', database='FretLogic')
#mssql_cursor = mssql_db.cursor()
#
#pp = pprint.PrettyPrinter(indent=3)

# For converting WELL FORMATTED (FULL) tablature to MSSQL Server Tables for later analysis...
f = open('sandmantab-modded.txt')

line = f.readline()

PMfretlogic = dict()
E1fretlogic = dict()
B2fretlogic = dict()
G3fretlogic = dict()
D4fretlogic = dict()
A5fretlogic = dict()
E6fretlogic = dict()
PRTfretlogic = dict()
POfretlogic = dict()

E1notes = []
B2notes = []
G3notes = []
D4notes = []
A5notes = []
E6notes = []

part_type = ' '

nummPM = 0
nummE1 = 0
nummB2 = 0
nummG3 = 0
nummD4 = 0
nummA5 = 0
nummE6 = 0
def alphabetizeFrets(StringNo, fretNo):
    if type(StringNo) == int:
        StringNo = str(StringNo)
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l', \
             'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    try:
        alphFret = alphabet[int(fretNo)]
    except ValueError:
        alphFret = '-'
        
    return StringNo + alphFret
    
for lineno, linestr in enumerate(f, start=0):
    print "line number: " + str(lineno) + ": " + linestr.rstrip()
    rowtype = linestr[0] #what string, what type of  data
    print rowtype

    if rowtype == '?': #grab song data from ?string|shit
        ##Artist|Song|Album|link
        print('Works')
        artist_data = str(linestr.rstrip()).replace('?','')
        artist = artist_data.split('|', 1)[0]
        song = artist_data.split('|', 2)[1]
        album = artist_data.split('|', 3)[2]
        links = artist_data.split('|', 4)[3]
     
    if rowtype == '+':
        part_type = str(linestr.rstrip()).replace('+','').replace(':','')
        part_order = str(part_type[0])+str(part_type[1])
        print part_order
        part_type = part_type[2:]
        print part_type

       #print part_type

    for colno, linecol in enumerate(linestr):
        #print "line number: " + str(lineno) + " col number: " + str(colno) + ": " + linecol.rstrip()

        if rowtype == '#':   #'PALM MUTER line'
            if linecol <> '|':
                PMfretlogic[nummPM] = str(linecol).replace("\n",'')
                PRTfretlogic[nummPM] = str(part_type)
                POfretlogic[nummPM] = str(part_order)
                nummPM = nummPM + 1
        elif rowtype == '1': #'1E'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                E1fretlogic[nummE1] = note
                PRTfretlogic[nummE1] = str(part_type)
                POfretlogic[nummE1] = str(part_order)
                E1notes.append(alphabetizeFrets(rowtype, note))
                nummE1 = nummE1 + 1
        elif rowtype == '2': #'2B'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                B2fretlogic[nummB2] = note
                PRTfretlogic[nummB2] = str(part_type)
                POfretlogic[nummB2] = str(part_order)
                B2notes.append(alphabetizeFrets(rowtype, note))                
                nummB2 = nummB2 + 1
        elif rowtype == '3': #'3G'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                G3fretlogic[nummG3] = note
                PRTfretlogic[nummG3] = str(part_type)
                POfretlogic[nummG3] = str(part_order)
                G3notes.append(alphabetizeFrets(rowtype, note))
                nummG3 = nummG3 + 1
        elif rowtype == '4': #'4D'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                D4fretlogic[nummD4] = note
                PRTfretlogic[nummD4] = str(part_type)
                POfretlogic[nummD4] = str(part_order)
                D4notes.append(alphabetizeFrets(rowtype, note))                
                nummD4 = nummD4 + 1
        elif rowtype == '5': #'5A'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                A5fretlogic[nummA5] = note
                PRTfretlogic[nummA5] = str(part_type)
                POfretlogic[nummA5] = str(part_order)
                A5notes.append(alphabetizeFrets(rowtype, note))                
                nummA5 = nummA5 + 1
        elif rowtype == '6': #'6E'
            if linecol <> '|':
                note = str(linecol).replace("\n",'')
                E6fretlogic[nummE6] = note
                PRTfretlogic[nummE6] = str(part_type)
                POfretlogic[nummE6] = str(part_order)
                E6notes.append(alphabetizeFrets(rowtype, note))                
                nummE6 = nummE6 + 1
        

#pp.pprint(B2fretlogic)
print 'cols ' + str(nummPM) + '  ' + str(nummE1) + '  ' + str(nummB2) + '  ' + str(nummG3) + '  ' + str(nummD4) + '  ' + str(nummA5) + '  ' + str(nummE6)
print 'lines ' + str(lineno)

allNotes= []
j = 0
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

#for i in range(nummE1):
#    try:
#
#        if str(E1fretlogic[i]) == '1' and str(B2fretlogic[i]) == '2' and str(G3fretlogic[i]) == '3' and str(D4fretlogic[i]) == '4' and str(A5fretlogic[i]) == '5' and str(E6fretlogic[i]) == '6':
#            pass
#        elif str(E1fretlogic[i]) == '':
#            pass
#        else:
#            print str(i) + '-' +str(artist) + ' ' + str(song) + ' ' + str(album) + ' ' + str(links) + ' ' +str(PRTfretlogic[i]) + ' ' + str(PMfretlogic[i]) + ' ' + str(E1fretlogic[i]) + ' ' + str(B2fretlogic[i]) + ' ' +  str(G3fretlogic[i]) + ' ' +  str(D4fretlogic[i]) + ' ' +  str(A5fretlogic[i]) + ' ' +  str(E6fretlogic[i])
#            mssql_cursor.execute("""insert into FretLogic.dbo.TabData (PickId, Test, Artist, Song, Album, TabLink, Part, PartOrder, PM, E1, B2, G3, D4, A5, E6) values ('""" + str(i) + """', GETDATE(), '""" + str(artist) + """', '""" + str(song) + """', '""" + str(album) + """', '""" + str(links) + """', '""" +str(PRTfretlogic[i]) + """', '""" +str(POfretlogic[i]) + """', '""" + str(PMfretlogic[i]) + """', '""" + str(E1fretlogic[i]) + """', '""" + str(B2fretlogic[i]) + """', '""" +  str(G3fretlogic[i]) + """', '""" +  str(D4fretlogic[i]) + """', '""" +  str(A5fretlogic[i]) + """', '""" +  str(E6fretlogic[i]) + """' )""")
#
#    except:
#        print 'cols ' + str(nummPM) + ' ' + str(nummE1) + '  ' + str(nummB2) + '  ' + str(nummG3) + '  ' + str(nummD4) + '  ' + str(nummA5) + '  ' + str(nummE6)
#        print 'lines ' + str(lineno)
#        print sys.exc_info()[0] #debug for fuckups
#        print sys.exc_info()[1] #debug for fuckups

print artist
print song
print album

#mssql_cursor.execute("update TabData set Vert = (E1 + CHAR(13) + B2 + CHAR(13) + G3 + CHAR(13) + D4 + CHAR(13) + A5 + CHAR(13) + E6)")
#
#mssql_db.commit()
f.close()
#Let's drink!