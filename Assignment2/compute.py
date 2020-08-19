#Assignment 2- Submission 

#Why sys was imported
import sys
def isstopword(word):
    stopword=["a","on","this","was","where","had","him","her","i","is","are","the", "an", "of", "and","he", "she", "his", "that", "there","by","to"]
    if word.lower() in stopword:
        return True
    else:
        return False

def readFile(file_name):
    fp=open(file_name, 'r')
    return fp.read()

def wordCount(contents):
    return len(contents.split())

def topTenCount(content):
    #Splitting the words into list
    wordslist=content.split()
    #Creating Empty dictionary to store 
    wordfreq={}
    #Iterating over the list and adding values in the dictionary
    i=0
    for word in wordslist:
        if(word.lower() in wordfreq):
            wordfreq[word.lower()]+=1
        else:
            wordfreq[word.lower()]=1
        i=i+1
    #Sorting the dictionary by value
    i=0
    maxct=0
    
    #Understand the 2nd argument in sorted function 

    sortedorders=sorted(wordfreq.items(), key=lambda x: x[1],reverse=True)
    #print(sortedorders)
    #type(sortedorders)
    if len(sortedorders)<10:
        maxct=len(sortedorders)
    else:
        maxct=10
    #PT-1
    print("Top 10 words Including stop-words are")
    while i<maxct:
        print(sortedorders[i])
        i=i+1
    #PT-2    
    stoporder=[]
    i=0
    for pair in sortedorders:
        if(isstopword(pair[0])==False):
            stoporder.append(pair)
        i=i+1
    if len(stoporder)<10:
       maxct=len(stoporder)
    else:
        maxct=10
    i=0
    print("Top 10 words excluding stop-words are")
    while i<maxct:
        print(stoporder[i])
        i=i+1


def main():
    filename=sys.argv[1]
    contents=readFile(filename)
    wordCountDict=wordCount(contents)
    #Printing Contents of the file
    #print("Content In file\n"+contents)
    #Priting Number of wordcounts
    print("Total Number of words")
    print(wordCountDict)
    #Printing Top words Including Stopword
    contents=contents.replace(".", " ")
    contents=contents.replace(","," ")
    topTenCount(contents)  

#Explain the concept of if __name__=="__main__"
if __name__ == "__main__":
    main()

    
