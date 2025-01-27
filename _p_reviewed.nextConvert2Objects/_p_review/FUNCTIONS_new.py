'''
======================================
FUNCTIONS:

appopen(filepath)
write2file(fileobject, key)
pathcreation(filename_endstring)
dictInput()
listInput()
tupleInput()
dictFrom2list(keylist, valuelist)
======================================
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def appopen(filepath):
#OPEN FILE IN DEFAULT APP
    import subprocess
    subprocess.call(["xdg-open",filepath])
    
#write output to a file
#Usage: inside other programs
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def write2file(fileobject, key):
    #assuming file is open
    #write from python data structures: list
    count = 0
    while True:
        fileobject.write(key+'\n')
        count += 1
    fileobject.close()
    print('write count = %d'%count)

    

def pathcreation(filename_endstring):
    '''------------------------------------
    pathcreation(filename_endstring): 
    Function creates a 'new file' with 'time string' on 'file name' 
    '''
    import time
    filename = str(int(time.time()))+filename_endstring
    filepath = '/home/kishore/p/outputdata/'+ filename
    return filepath
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Dictionary input
#For creating dictionary
#EASY USER INPUT

#dictionary value only 'str' type


def dictInput():
    print('Dictionary creation'.center(40,'='))
    dictTemp = {}
    #print('Input for Dictionary Name: ')
    #dictName = input()
    
        

    #print('Dictionary:: '+dictName+' created')
# set name of dictionary

    while True:
        print('\n\tEnter key: ',end=' ' )
        dictKey = input()
        if dictKey == '':
            break
        if dictKey in dictTemp:
            print('key exists:: '+dictKey+' : '+dictTemp[dictKey])
        else:
            print('\tEnter value: ',end=' ')
            dictValue = input()
            dictTemp[dictKey] = dictValue
            print('--value added successfully.')

    print('Dictionary created successfully'.center(50,'='))
    return dictTemp
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#for list creation
#EASY USER INPUT

#list values only 'int' or 'str' Type  

def listInput():
    print('List creation'.center(40,'='))
    tempList = []

    while True:
        print('\tEnter value: ',end=' ')
        listValue = input()
        if listValue == '':
            break
        try:
            tempList = tempList + [int(listValue)]
        except:
            tempList = tempList + [listValue]
     
    print('List created successfully'.center(40,'='))
    return tempList    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#for tuple creation
#EASY USER INPUT

#list values only 'int' or 'str' Type  

def tupleInput():
    print('Tuple creation'.center(40,'='))
    tempTuple = ()

    while True:
        print('\tEnter value: ',end=' ')
        tupleValue = input()
        if tupleValue == '':
            break
        tempList = list(tempTuple)
        try:            
            tempList = tempList + [int(tupleValue)]
        except:
            tempList = tempList + [tupleValue]
        tempTuple = tuple(tempList)
    print('Tuple created successfully'.center(40,'='))    
    return tempTuple    
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Program INPUT: 2 NOS. OF list :: OUTPUT: 1 dictionary

from myFunc import *

def dictFrom2list(keyList, valueList):
    #print('Dictionary creation from 2 lists'.center(50,'='))
    dictTemp = {}
    i = -1
    if len(keyList) != len(valueList):
        return '\n ---x x x Size mismatch'
    for key in keyList:
        i+=1
        dictTemp[key] = valueList[i]

    print('Success:: Dictionary created from 2 lists'.center(50,'='))
    return dictTemp
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

