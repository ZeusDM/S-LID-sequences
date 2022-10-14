from pathlib import Path
import slid

# This scripts generates and saves the next element of all S-LIDs sequences
# with fewer elements where S ranges over all subsets of [10]. The intented
# use of this script is to be running in the background to create more data
# about S-LID sequences where S is a subset of [10].

# powerset generates all subsets of seq, as lists.
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

# sets is a list of all non-empty subsets of [10]
sets = list(set(x) for x in powerset(list(range(1, 11))))[:-1]

size = []

for s in sets:
    file = Path(slid.filename(s))
    file.touch(exist_ok=True) # creates file for the S-LID sequence, if necessary
    size.append(sum(1 for line in open(slid.filename(s))))

m = min(size)

for i in range(len(sets)):
    if size[i] == m:
        slid.computeNext(sets[i])
