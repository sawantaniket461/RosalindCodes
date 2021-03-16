'''Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
probabilty of offspring having dominant trait ==> P(x)
    AA-AA (P(x) = 1)
    AA-Aa (P(x) = 1)
    AA-aa (P(x) = 1)
    Aa-Aa (P(x) = 0.75)
    Aa-aa (P(x) = 0.5)
    aa-aa (P(x) = 0)

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.'''

def calculateOffspring(fileinput=""):
    inputFile = open(fileinput, 'r')
    couples = inputFile.readline().rstrip()
    inputFile.close()
    array = couples.split(' ')
    expectedProbabilityOffspringDominant = 2*(int(array[0]) + int(array[1]) + int(array[2]) + int(array[3]) * 0.75 + int(array[4])*0.5 + 0 * int(array[5]))
    print(expectedProbabilityOffspringDominant)
calculateOffspring('rosalind_iev.txt')
