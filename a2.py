def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    len1 = len(dna1)
    len2 = len(dna2)
    return len1 > len2



def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    lst= ('A', 'T', 'C', 'G')
    for m in range (0,len(dna)):
 
        if dna[m] not in lst:
            return False
    return True

def insert_sequence(a,b,n):
    lsta=list(a)
    lsta.insert(n-1,b)
    return ''.join(lsta)

def get_complement(nucleotide):
    pair= {'T':'A','A':'T','C':'G','G':'C'}
    return pair.get(nucleotide)


def get_complementary_sequence(dna):
    pair= {'T':'A','A':'T','C':'G','G':'C'}
    dna=list(dna)
    lst=[]
    for n in dna:
        lst.append(pair.get(n))
   
    return ''.join(lst)
