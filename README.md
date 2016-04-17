# RiffChruncher

This project contains files that grabs tabluture from the internet, specifically 'ultimate-guitar.com' and reads them. 
Mining them for data on the various notes played in songs, the end goal would be analyse different genres of music. 

The end goal would be to try to understand why all coutry music sounds the same. I hypothesize that all country music sounds the same
becasue many songs all use the same chord progession, whereas many other genres of music have a greater variation in the chord 
progressions used.
A chord progression is the different chords used in songs, as well as the order in which they are used. For example Pearl Jam's 
'Elderly woman...' uses a chord progression D C G G for the much of the verse and chorus.
Both the notes used and their respective order is needed.

To run use the getChordsandPlot.py that sums up chord progressions used in country music.
The output is  2 bar charts, the first shows the count of chord progressions, the second shows the usage of various chords.

We find that Chords involving variations of G, C, and D are very popular in country music and those three chords account for about 45% of the total chords, if we look at the top 8 chords (G, C, D, A, F, Am, Em, E) they account for almost 75%. For context there are over 800 various chord combinations (see: https://tabs.ultimate-guitar.com/m/misc/all_the_chords_crd.htm). So we can see how these 8 chords and their various combinations can lead to music that may sound similar.