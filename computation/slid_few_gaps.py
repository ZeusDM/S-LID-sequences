from pathlib import Path
import slid

# This scripts generates and saves the next element of all S-LIDs sequences with
# fewer elements where S ranges over sets of the form [k] - (k-T). For small
# sets T. The intented use of this script is to be running in the background to
# create more data about S-LID sequences where S = [k] - (k-T).

sets = []
for k in range(4, 51):
    for c in range(max(1, k-10), k-4):
        sets.append((set(i for i in range(1, k+1) if i != c)))

size = []

for s in sets:
    file = Path(slid.filename(s))
    file.touch(exist_ok=True) # creates file for the S-LID sequence, if necessary
    size.append(sum(1 for line in open(slid.filename(s))))

m = min(size)

for i in range(len(sets)):
    if size[i] == m:
        slid.computeNext(sets[i])
