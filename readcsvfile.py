import os
import csv

csvColumns=[]    
csvLines=[[]]
numofColumns=0
numofLines=0

def readcsvfile(file='empty.csv'):
    global csvColumns   
    global csvLines
    global numofColumns
    global numofLines
    FileError=''
    if os.path.exists(file):
        csvfile=open(file, encoding='utf-8')
        csvcontent = csv.reader(csvfile, delimiter=',')
        for line in csvcontent:
            if numofLines==0:
                for columnName in line:
                    csvColumns.append(columnName)
                    numofColumns += 1
                numofLines += 1
            else:
                templist=[]
                tempnum=0
                for columnData in line:
                    templist.append(columnData)
                    tempnum+=1
                #do we have data in all columns
                while tempnum < numofColumns:
                    templist.append('')
                csvLines.append(templist)
                numofLines += 1
        csvfile.close()
    else:
        FileError +='File does not exist'
    
    return FileError

def returnline(linenum=1):
    global numofLines
    global csvLines
    if linenum <= numofLines:
        return csvLines[linenum]
    else:
        return 'Out of Range'

def returncolumn(colnum=1):
    global numofColumns
    global csvLines
    line = []
    returntext=[]
    if colnum <= numofColumns:
        for line in csvLines:
            colindex=0
            for cell in line:
                colindex +=1
                if colindex == colnum:
                    returntext.append(cell)
        return returntext
    else:
        return 'out of range'

def parsecsv():
    print('reading')
    filepath='C:\\csvfilepath\\csvfile.csv'
    error=readcsvfile(filepath)
    if error:
        print(error)
    else:
        print('parsed')

def printformatted(linenum=1):
    global numofColumns
    for column in csvColumns:
        n=0
        if n < numofColumns:
            # in case the column content is longer than 15 characters
            # there can be control to fit into the columns
            # but I did not implement in this version 
            print(f'{column:15}', end='')
        elif n == numofColumns:
            print(f'{column}')
        n+=1
    print('')
    n=0
    while n <= (15 * (numofColumns)):
        print(f'-', end='')
        n+=1
    print('')       
    for item in returnline(linenum):
        print(f'{item:15}', end='')

def main():
    parsecsv()
    print(f'the CSV file has {numofColumns} columns and {numofLines} lines')
    print(f'Column names are {csvColumns}')
    n=8
    print(f'The Line {n} contains: {returnline(n)}')
    printformatted(n)

if __name__ == '__main__': main()
