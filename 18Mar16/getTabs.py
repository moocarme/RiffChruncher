# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 15:12:54 2016

@author: matt
"""
import shelve
import requests
from lxml import html


def getTab(url):
    page = requests.get(url)
    tree= html.fromstring(page.content)
    myxpath = '//*[@id="cont"]/pre[2]/text()'
    tab = tree.xpath(myxpath)
    return tab

band = 'radiohead'
page = '1'

genresDict = {'alternative': '20', 'country': '6', 'blues': '2', 'classical':'5', \
    'jazz':'11', 'pop':'14', 'reggae': '24', 'rock':'21', 'world':'19'}
genre = 'world'

def getTree(band, page):
    if type(page) == int:
        page = str(page)
#    theURL = 'https://www.ultimate-guitar.com/search.php?view_state=advanced' + \
#        '&band_name=&song_name=&type%5B%5D=200&rating%5B%5D=5&tuning%5B%5D=standard&' + \
#        'version_la=&genres%5B%5D='+ genresDict[band]
#    theURL = 'https://www.ultimate-guitar.com/search.php?band_name=' + band + \
#        '&type%5B1%5D=200&type2%5B0%5D=40000&rating%5B4%5D=5&tuning%5Bstandard%5D=standard&page=' \
#        + page + '&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'
    theURL = 'https://www.ultimate-guitar.com/search.php?band_name=' + band + \
        '&type%5B1%5D=300&type2%5B0%5D=40000&rating%5B4%5D=5&tuning%5Bstandard%5D=standard&page=' \
        + page + '&view_state=advanced&tab_type_group=text&app_name=ugt&order=myweight'

    pageBand = requests.get(theURL)
    return html.fromstring(pageBand.content)
#urlBand = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value=metallica+'

#pageBand = requests.get(getURL(band, page))
#tree1 = html.fromstring(pageBand.content)

tree1 = getTree(band, page)
pages = tree1.find_class('paging')
maxPage = len(list(pages[0].iter('a')))
print('Max Page: '+ str(maxPage))

songs = tree1.find_class('song result-link')
songLinks = []
for i in songs:
    songLinks.append(i.get('href'))        

for i in range(maxPage -1):
    looppage = i + 2
    looptree = getTree(band, str(looppage))
    loopsongs = looptree.find_class('song result-link')
    for song in loopsongs:
        songLinks.append(song.get('href'))
    

print('No of tabs: ' + str(len(songLinks)))
myTabs = []
j = 0
for i in songLinks:
    myTabs.append(getTab(i))
    j = j + 1

filename='shelve.out'
my_shelf = shelve.open(filename,'n') 

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