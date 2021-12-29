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
import string
from io import StringIO

#put unnecessary items into this list
removelist = ['googlegroups', 'yahoogroups', 'info@', 'contact@', 'travel@', 'bilgi@', 'resort']

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



def runmyscript():
    winpath='C:\\somepathofcsvfile\\contacts.csv'
    email=''
    if os.path.exists(winpath):
        contacts=open(winpath, 'r',codec='utf-8')
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
        print(f'Processed {linecount} lines.')                        
        contacts.close()
    else:
        email +='File does not exist'
    
    print(email)

if __name__ == '__main__': main()
