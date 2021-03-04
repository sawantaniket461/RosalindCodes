#Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#Return: The adjacency list corresponding to O3. You may return edges in any order.
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/aniket/Desktop/Personal/Aniket/Rosalind/AllPurpose')

from adjustingMultiFastaFiles import adjustMultiFastaFiles
def adjacencyMatrix(fileName = "rosalind_grph.txt"):
    inputFileName = open (fileName, 'r')
    dict = {}
    keys = []
    seqName = ""
    for line in inputFileName.readlines():
        line = line.rstrip()
        #print (line)
        if line.startswith('>'):
            seqName = line.split('>')[1]
            keys.append(seqName)
        else:
            dict[seqName] = line

    for i in range(0, len(keys)):
        for j in range(0, len(keys)):
            #print (keys[i] + " ==> " + keys[j])
            if not(keys[i] == keys[j]):
                if (dict[keys[i]][-3:] == dict[keys[j]][0:3]):
                    print (keys[i] + " " + keys[j])
            '''    if (dict[keys[i]][0:3] == dict[keys[j]][-3]):
                    print (keys[j] + " " + keys[i])
'''
            #print ("ASDFGH"[0:3])
'''
    for k,v in dict.items():
        print (k + " " + v)
'''

adjustMultiFastaFiles('/home/aniket/Desktop/Personal/Aniket/Rosalind/Q13_AdjacencyGraphs/rosalind_grph.txt')
adjacencyMatrix("tempFileMultiFastaAdjusted.txt")
#adjacencyMatrix()
