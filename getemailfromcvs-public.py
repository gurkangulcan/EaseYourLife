#this code gets the outlook csv file and gathers all the e-mail addresses
#it can be used for any readible text file 
#outlook csv export contains multiple columns having e-mail addresses.
#this script does not convest cvs data into structured data model.
#it basically matches a regular expression for e-mail addresses.
#if you need to remove unnecessary e-mails with specific wording 
#you can use removelist.
#outlook puts Exchange server details in case the contact is taken from it
#the script is not taking care of these contacts and e-mails. use responsibly.
import os
import re
import math
import string
from io import StringIO

#put unnecessary items into this list
removelist = ['googlegroups', 'yahoogroups', 'info@', 'contact@', 'travel@', 'bilgi@', 'resort', 'help', 'siparis' ]

def main():
    runmyscript()

#this script checks if the e-mail address includes any item in the removelist
#this script also shows the removed e-mails from the latest e-mail text.
def checkremoving(newmail):
    text=''
    for checked in removelist:
        p=re.compile(checked)
        if p.search(newmail):
            print(f'removed:{newmail}')
            text=''
            break
        else:
            text=newmail
    return text

#this function is to do repetetive task
def addsemicolumn(newmail):
    return '; ' + newmail

def printseperated(text, seperator, count):
    wholetext=''
    splitted=text.split('; ')
    numofemails=len(splitted)
    seperatorcount=math.ceil(numofemails / count)
    i=0
    while i < seperatorcount :
        ji=1
        if ( i != seperatorcount-1):
            while (i*count+ji) <= count*(i+1) :
                if (ji <= count):
                    wholetext += addsemicolumn(splitted[i*count+ji])
                else:
                    wholetext += splitted[i*count+ji]
                ji += 1
        else:
            while (i*count+ji) < numofemails :
                if (ji <= count):
                    wholetext += addsemicolumn(splitted[i*count+ji])
                else:
                    wholetext += splitted[i*count+ji]
                ji += 1
               
        if ((i*count+ji) < numofemails-1):
            wholetext += '\n\nNEXT BUNCH:\n'
        i += 1
    print(wholetext)

def runmyscript():
    winpath='C:\\contacts.csv'
    email=''
    if os.path.exists(winpath):
        contacts=open(winpath, 'r', encoding='utf-8')
        linecount=0
        for line in contacts:
            linecount += 1
            newline=True
            firstmail=''
            p=re.compile(r'\w+[._]{0,1}\w+@+\w[.\-\_\w]{4,20}\w')
            temail=p.findall(line)
            if type(temail) is list:
                for eachmail in temail:
                    eachmail = checkremoving(eachmail)
                    if eachmail== '':
                        break
                    if linecount == 1:
                        if newline == True:
                            firstmail = eachmail
                            email += eachmail
                            newline = False 
                        else:
                            if firstmail != eachmail:
                                email += addsemicolumn(eachmail)
                                newline = True                             
                    else: 
                        if newline == True:
                            firstmail = eachmail
                            email += addsemicolumn(eachmail)
                            newline = False 
                        else:
                            if firstmail != eachmail:
                                email += addsemicolumn(eachmail)
                                newline = True
            else:
                print('NOT LIST\n')
        print(f'Processed {linecount} lines.')                        
        contacts.close()
    else:
        email +='File does not exist'
#sometimes mail servers dont allow more than some number of e-mail addresses in one e-mail.
#automatic splitting is possible, based on the below number
    numofemailinonechunk=350
    printseperated(email,'; ', numofemailinonechunk)

if __name__ == '__main__': main()
