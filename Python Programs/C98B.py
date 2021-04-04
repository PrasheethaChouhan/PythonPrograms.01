def countwordsfromfile():
    filename = input("Enter the file name")
    wordcount = 0
    file = open(filename,'r')
    for line in file:
        words = line.split()
        wordcount = wordcount+len(words)
    print ("the number of words in this file is" + str(wordcount))

countwordsfromfile()