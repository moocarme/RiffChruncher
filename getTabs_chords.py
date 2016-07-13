# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:12:54 2016

@author: matt
"""
import shelve
import requests
from lxml import html
from lxml.etree import tostring

def getTab(url):
    webPage = requests.get(url)
    webTree= html.fromstring(webPage.content)
    tabXpath = '//*[@id="cont"]/pre[2]/text()'
    tab = webTree.xpath(tabXpath)
    return tab
    
def getChords(url):
    webPage = requests.get(url)
    webTree= html.fromstring(webPage.content)
    tabContentClass = webTree.find_class('js-tab-content')
    chordsList = list(tabContentClass[0].iter('span')) # starts at element 0
    return [tostring(chordsList[i], with_tail = False).strip('</span>') for i in range(len(chordsList))]

#allchordsURL = 'https://tabs.ultimate-guitar.com/m/misc/all_the_chords_crd.htm'
#allChordsTab = getTab(allchordsURL)
#
#allChordsTab = str(allChordsTab[0]).split('\\n')
#allChordsTab = (allChordsTab[0].rstrip()).split('\n')
#col1 = []
#for lineno, linestr in enumerate(allChordsTab):
#        try:
#            col1.append(linestr[:9])
#            if linestr[15:25] != '          ':
#                col1.append(linestr[15:25])
#        except:
#            col1.append(linestr[0])
#allChords = []
#for i in col1:
#    if i not in allChords:    
#        str(i).replace(' ','')
#        allChords.append(i) 
#allChords = [x.strip(' ') for x in allChords[6:-3]]
    
    
band = 'radiohead'
page = '1'

genresDict = {'alternative': '20', 'country': '6', 'blues': '2', 'classical':'5', \
    'jazz':'11', 'pop':'14', 'reggae': '24', 'rock':'21', 'world':'19'}
genre = 'country'

def getBandTree(band, page):
    if type(page) == int:
        page = str(page)
    theURL = 'https://www.ultimate-guitar.com/search.php?band_name=' + band + \
        '&type%5B2%5D=300&type2%5B0%5D=40000&rating%5B4%5D=5&tuning%5Bstandard%5D=standard&page=' \
        + page +'&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'
    pageBand = requests.get(theURL)
    return html.fromstring(pageBand.content)

def getGenreTree(genre, page):
    if type(page) == int:
        page = str(page)
#    theURL = 'https://www.ultimate-guitar.com/search.php?band_name=' + band + \
#        '&type%5B2%5D=300&type2%5B0%5D=40000&rating%5B4%5D=5&tuning%5Bstandard%5D=standard&page=' \
#        + page +'&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'
    theURL = 'https://www.ultimate-guitar.com/search.php?type[2]=300&type2[0]=40000&rating[4]=5' \
        + '\&tuning[standard]=standard&genres[0]=' + genresDict[genre]+ '&page=' + page \
        + '&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'
        
    pageBand = requests.get(theURL)
    return html.fromstring(pageBand.content)
    

tree1 = getGenreTree(genre, page)
pages = tree1.find_class('paging')
maxPage = len(list(pages[0].iter('a')))
print('Max Page: '+ str(maxPage))

songs = tree1.find_class('song result-link')
songLinks = []
for i in songs:
    songLinks.append(i.get('href'))        

for i in range(maxPage -1):
    looppage = i + 2
    looptree = getGenreTree(genre, str(looppage))
    loopsongs = looptree.find_class('song result-link')
    for song in loopsongs:
        songLinks.append(song.get('href'))
    

print('No of tabs: ' + str(len(songLinks)))
myChords = []
j = 0
for i in songLinks:
    myChords.append(getChords(i))
    j = j + 1

#filename='shelve.out'
#my_shelf = shelve.open(filename,'n') 

#for key in dir():
#    try:
#        my_shelf[key] = globals()[key]
#    except TypeError:
#        #
#        # __builtins__, my_shelf, and imported modules can not be shelved.
#        #
#        print('ERROR shelving: {0}'.format(key))
#        
#my_shelf.close()