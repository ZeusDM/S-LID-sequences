from pathlib import Path
from config import storage

def filename(S):
    return storage / f"slid_{'_'.join(str(i) for i in sorted(list(S)))}.txt"

def blocked(k, S):
    return {k-i for i in S}

def allowed(set_of_indices, S):
    if len(set_of_indices) == 0:
        yield []
    else:
        k = max(set_of_indices)
        # if k is not chosen
        set_aux = set_of_indices.difference({k})
        for allowed_sequence in allowed(set_aux, S):
            yield allowed_sequence
        set_aux = set_aux.difference(blocked(k, S))
        for allowed_sequence in allowed(set_aux, S):
            yield allowed_sequence+[k]

def computeNext(S):
    file = filename(S)
    file.touch(exist_ok=True)

    with open(file, "r") as f:
        my_sequence = [int(line[:-1]) for line in f.readlines()]

    obtainable_numbers = set()

    for allowed_sequence in allowed(set(range(1, len(my_sequence)+1)), S):
        obtainable_numbers.add(sum([my_sequence[index - 1] for index in allowed_sequence]))

    new_term = next(i for i, e in enumerate(list(obtainable_numbers) + [ None ], 0) if i != e)

    with open(file, "a+") as f:
        f.write(f"{new_term}\n")
