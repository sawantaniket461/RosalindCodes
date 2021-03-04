def adjustMultiFastaFiles(inputFileName = "", outputFileName = "tempFileMultiFastaAdjusted.txt"):
    inputFile = open (inputFileName, 'r')
    concatString = ''
    for line in inputFile.readlines():
        line = line.rstrip()
        if line.startswith('>'):
            line = line + '__'
        concatString = concatString + '' + line
    inputFile.close()
    outFile = open(outputFileName, 'w')
    sequenceDict = {}
    array_concat = concatString.split('>')
    array_concat.pop(0)
    #print (array_concat)
    for mem in array_concat:
        seqName = mem.split('__')[0]
        sequence = mem.split('__')[1]
        sequenceDict[seqName] = sequence
        outFile.write('>' + seqName + '\n' )
        outFile.write(sequence + '\n')

#adjustMultiFastaFiles('/home/aniket/Desktop/Personal/Aniket/Rosalind/Q13_AdjacencyGraphs/rosalind_grph.txt')
