#!/usr/bin/python3
# FILE: walkBlocks.py
# fUNCTIONS for various directrory tree walk types 

"""
-------------------------------
function: walk(path)
function: walk2list(path)
function: walk4specific(path,filetype)
--------------------------------

os.walk(path)

ANALOGY
1) GO TO NEXT ROOM:
2) CHECK FOR ARTICLES AND SUBROOMS:
3-N) IF NO ARTICLES AND SUBROOMS: COME OUT FOR STEP (1)
3-Y) IF ATRICLES FOUND: NOTE DOWN; IF SUBROOMS FOUND: NOTE DOWN
4) GO TO SUB ROOM
5) REPEAT STEP (2),(3-N),(3-Y)

THATS HOW IT WORKS.
"""

import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 1. fUNCTION: Walk just to count number of files and folders
def walk2count(path):
    folcount = 0
    filecount = 0
    print('walking...')
    for fol, sf, file in os.walk(path):
        folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
        
    print('\nFiles : %d nos.'%filecount)
    print('Folders : %d nos.'%folcount+'\n---in complete path tree')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 2. fUNCTION: Walk to list contents
def walk2list(path):
    folcount = 0
    filecount = 0
    for fol, sf, file in os.walk(path):
        folcount+=1
        print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            filecount+=1
            print('\t\tFILE IN: '+str(fol)+':'+str(f))
        for s in sf:
            print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
        
    print('\nFiles : %d nos.'%filecount)
    print('Folders : %d nos.'%folcount+'\n---in complete path tree')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 3. fUNCTION: Walk to search a particular extension filetype
def walk4fext(path,fileType):
    count=0
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if f.endswith(fileType):
                print(str(fol)+' : '+str(f))
                count+=1
                #print('\n'+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
    if count==0:
        print('~~~~~~~~~~\nZERO mathces\n~~~~~~~~~~\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 4. fUNCTION: Walk for general search 
"""
finds for matching string in filename
"""
def walksearch(path, string):
    count=0
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if string in f:
                print(str(fol)+' : '+str(f))
                count+=1
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
            
    if count==0:
        print('~~~~~~~~~~\nZERO mathces\n~~~~~~~~~~\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 5. fUNCTION: Walk for exact match
def walkexact(path, search):
    count=0
    for fol, sf, file in os.walk(path):
        #folcount+=1
        #print('\n'+ 'CURRENT FOLDER: '+str(fol))
        for f in file:
            #filecount+=1
            #print('\t\tFILE IN: '+str(fol)+':'+str(f))
            if f == search:
                print(str(fol)+' : '+str(f))
        #for s in sf:
            #print('\tSUBFOLDER OF: '+str(fol)+':'+str(s))
    if count==0:
        print('~~~~~~~~~~\nZERO mathces\n~~~~~~~~~~\n')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
