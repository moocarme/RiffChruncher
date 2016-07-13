# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/matt/.spyder2/.temp.py
"""

test = ''


def AlphabatizeFrets(x):
    return 5    
    
    
def GenerateRiffCodeFromText(x): # x being the giant text string...

    riff_number = 0
    commonchar = None
    string_line = None
    lineresults = {} # or dict()

    for lineno, linestr in enumerate(x):

                linestr = linestr.rstrip('\r\n') #.strip()
                first3char = linestr[0:3]
                if len(linestr) > 0:   # not counting some common accent symbols in case tab author was crazy w solo accents
                    prev_commonchar = commonchar
                    mod_linestr = linestr.replace('~',' ').replace('\\',' ').replace('^',' ' )
                    commonchar = (collections.Counter(mod_linestr).most_common(1)[0])[0] # [0] is digit, [1] is freq
                    if commonchar == ' ':
                        try:
                            commonchar = (collections.Counter(mod_linestr).most_common(2)[1])[0] # [0] is digit, [1] is freq
                        except:
                            pass # ? not sure see 2x4
                    
                else:
                    prev_commonchar = commonchar
                    commonchar = 'DIVIDER'


                # find (probable) string lines and label them
                if (commonchar == '-' and linestr.find('P') < 0) or (commonchar.isdigit() and linestr.find('-') > 0): # so we don't grab the Palm Mute line...
                    if string_line == None:
                        prev_string_line = string_line
                        string_line = 1
                    else:
                        prev_string_line = string_line
                        string_line = string_line + 1
                    #lineresults[lineno] = string_line
                else:
                    prev_string_line = string_line
                    string_line = None


                # find (probable) meta / PM line ?
                if linestr.find('P') > 2 and string_line == None:
                    prev_string_line = string_line
                    string_line = 0

                # find (possible) section headers
                if len(linestr)<30 and commonchar.isalpha() and string_line == None and commonchar <> 'DIVIDER':
                    riff_name = 'riff name?'
                else:
                    riff_name = None

                #print "line number: " + str(lineno) + ": " + linestr.rstrip()+' ',
                #print '{' + commonchar + ' ' + str(string_line) + ' ' + str(riff_name) +'} Rnum' + str(riff_number) #+ 'prevst'+str(prev_string_line)


                if prev_string_line == 6:
                    riff_number = riff_number + 1
                elif (commonchar == 'DIVIDER' and prev_string_line < 6 and prev_string_line > None): 
                    riff_number = riff_number + 1


                # add all this shit to a dick(t)
                if not lineresults.has_key(riff_number):
                    lineresults[riff_number] = {}
                lineresults[riff_number][string_line] = {'linestr':linestr.rstrip(), 'commonchar':commonchar, 'string_line':string_line, 'riff_name':riff_name, 'riff_number':riff_number}
                #lineresults[riff_number] = {'linestr':linestr.rstrip(), 'lineno':lineno, 'string_line':string_line, 'riff_name':riff_name, 'riff_number':riff_number}

            #print 'done: ' + str(len(lineresults)) + ' lines'
            #pp.pprint(lineresults)


    linelengths = {}

    # get longest line ?
    for rnum in lineresults:
                linelengths[rnum] = 999
                for ln in lineresults[rnum]:
                    if ln > 0:
                        if len(lineresults[rnum][ln]['linestr']) < linelengths[rnum]:
                            linelengths[rnum] = len(lineresults[rnum][ln]['linestr'])
                if linelengths[rnum] == 999:
                    linelengths[rnum] = 0
                    

    result_dict = {}


    for rnum in lineresults:
                result_dict[rnum] = {}

                raw_lines = ''

                try:
                    raw_lines += str(lineresults[rnum][None]['linestr']) + "\n"
                    riff_name = str(lineresults[rnum][None]['linestr'])
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][0]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][1]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][2]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][3]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][4]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][5]['linestr']) + "\n"
                except:
                    pass
                try:
                    raw_lines += str(lineresults[rnum][6]['linestr']) + "\n"
                except:
                    pass

                result_dict[rnum]['raw_lines'] = raw_lines

                # alphabetize fret nums
                for i in lineresults[rnum]:
                    lineresults[rnum][i]['linestr_a'] = AlphabatizeFrets(lineresults[rnum][i]['linestr'])
                
                s = ''
                
                for column in range(linelengths[rnum]):
                    try:

                        # first attempt at simple PM recording..
                        try:
                            ##print lineresults[rnum][6]['linestr'][column],
                            if lineresults[rnum][0]['linestr_a'][column] <> ' ':
                                s += '#'
                            else:
                                s += '0' # record nothing?
                        except:
                            ##print '?',
                            s += '0'
                
                        
                        try:
                            ##print lineresults[rnum][6]['linestr'][column],
                            s += lineresults[rnum][6]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        try:
                            ##print lineresults[rnum][5]['linestr'][column],
                            s += lineresults[rnum][5]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        try:
                            ##print lineresults[rnum][4]['linestr'][column],
                            s += lineresults[rnum][4]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        try:
                            ##print lineresults[rnum][3]['linestr'][column],
                            s += lineresults[rnum][3]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        try:
                            ##print lineresults[rnum][2]['linestr'][column],
                            s += lineresults[rnum][2]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        try:
                            ##print lineresults[rnum][1]['linestr'][column],
                            s += lineresults[rnum][1]['linestr_a'][column].replace(' ','-')
                            ###sz = lineresults[rnum][1]['linestr_a'][column].replace(' ','-')
                        except:
                            ##print '?',
                            s += '?'
                        #print ',',
                        s += ' '
                        #print s,
                        
                    except:
                        pass #test


                #changing some chars for a test indexing run
                # constructing the "LONG CODE"
                #print s # original s code

                # check first "note" for bar notes
                if ("##" in s[:8] or "B" in s[:8] or "E" in s[:8] or "A" in s[:8] or "?" in s[:8] or "||" in s[:8] or "::" in s[:8]) and "-" not in s[:8]:
                    s = s[8:]
                    if ("##" in s[:8] or "B" in s[:8] or "E" in s[:8] or "A" in s[:8] or "?" in s[:8] or "||" in s[:8] or "::" in s[:8]) and "-" not in s[:8]:
                        s = s[8:]

                # check late "note" for bar notes
                if ("##" in s[-8:] or "E" in s[-8:] or "A" in s[-8:] or "?" in s[-8:] or "||" in s[-8:]) and "-" not in s[-8:]:
                    s = s[:-8]
                    if ("##" in s[-8:] or "E" in s[-8:] or "A" in s[-8:] or "?" in s[-8:] or "||" in s[-8:]) and "-" not in s[-8:]:
                        s = s[:-8]

                #s = s.replace('0EADGBE','').replace('0||||||','').replace('0::::::','')
                #s = s.replace('|||','')

                s = s.replace('0||||||','|') # riff bar seperators
                s = s.replace('#||||||','|') # riff bar seperators
                s = s.replace('?','-') # temp - work on it later (mark out missing tabbed strings)

                if ("| " in s[:2]):
                    s = s[2:]

                # now to change LONG CODE to SHORT CODE
                
                long_code = s
                long_code_list = long_code.split()
                short_code = ''

                for w in long_code_list:
                    #print w
                    if w == '|':
                        w = '|'
                        ww = '|'
                    elif w == '0------':
                        w = '.'
                        ww = '.'
                    else:
                        wd = {}
                        cnt = 0
                        cntf= 0
                        for l in w:
                            
                            if l == '#' or l == '0' or l == '-' or l == '/' or l == '(' or l == ')' or l == '\\':
                                wd[cnt] = str(l)
                            else:
                                wd[cnt] = str(7-cnt)+str(l)

                            cnt = cnt+1
                            #elif w[0:1] in [a-z]:
                            #   print 'tt'
                        #pp.pprint(wd)
                        ww = ''
                        for i in range(0,7):
                            try: # ? changed last minute
                                ww += wd[i]
                            except:
                                pass


                    #short_code += str(w)+' '
                    wdee = str(ww)
                    wdee = wdee.replace('0-----','')
                    wdee = wdee.replace('0----','')
                    wdee = wdee.replace('0---','')
                    wdee = wdee.replace('0--','')
                    wdee = wdee.replace('0-','')
                    wdee = wdee.replace('0','')
                    wdee = wdee.replace('#-----','*')
                    wdee = wdee.replace('#----','*')
                    wdee = wdee.replace('#---','*')
                    wdee = wdee.replace('#--','*')
                    wdee = wdee.replace('#-','*')
                    wdee = wdee.replace('#','*')

                    if wdee[-5:] == '-----':
                        wdee = wdee[:-5]
                    elif wdee[-4:] == '----':
                        wdee = wdee[:-4]
                    elif wdee[-3:] == '---':
                        wdee = wdee[:-3]
                    elif wdee[-2:] == '--':
                        wdee = wdee[:-2]
                    elif wdee[-1:] == '-':
                        wdee = wdee[:-1]

                    if "H" in wdee:
                        wdee = '>'
                    if "P" in wdee:
                        wdee = '<'

                    short_code += str(wdee)+' '

                result_dict[rnum]['short_code'] = short_code
                result_dict[rnum]['long_code'] = long_code
                result_dict[rnum]['riff_name'] = riff_name


    #return short_code
    return result_dict
    
GenerateRiffCodeFromText(test)
