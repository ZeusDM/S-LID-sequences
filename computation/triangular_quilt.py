from pathlib import Path
from config import storage

file = storage / Path('triangular_quilt.txt')

def blocked(k):
    if k == 1:
        return set()
    if k == 2:
        return {1}
    if k == 3:
        return {2}
    if k == 4:
        return {1, 3}
    if k == 5:
        return {4}
    else:
        return {k-1, k-5}

def allowed(set_of_indices):
    if len(set_of_indices) == 0:
        yield []
    else:
        k = max(set_of_indices)
        # if k is not chosen
        set_aux = set_of_indices.difference({k})
        for allowed_sequence in allowed(set_aux):
            yield allowed_sequence
        set_aux = set_aux.difference(blocked(k))
        for allowed_sequence in allowed(set_aux):
            yield allowed_sequence+[k]

def computeNext():
    file.touch(exist_ok=True)

    with open(file, "r") as f:
        my_sequence = [int(line[:-1]) for line in f.readlines()]

    obtainable_numbers = set()

    for allowed_sequence in allowed(set(range(1, len(my_sequence)+1))):
        obtainable_numbers.add(sum([my_sequence[index - 1] for index in allowed_sequence]))

    new_term = next(i for i, e in enumerate(list(obtainable_numbers) + [ None ], 0) if i != e)

    with open(file, "a+") as f:
        f.write(f"{new_term}\n")

computeNext()
