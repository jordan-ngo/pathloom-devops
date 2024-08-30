from itertools import permutations, islice
from typing import List, Tuple

def permutation_func(lst: List[any], limit=100) -> List[Tuple[any]]:
    # generate permutations for the given list of strings
    perms = permutations(lst)
    
    # limit due to large number of permutations for tests
    limit_perm = islice(perms, limit)

    # store unique permutations
    unique_perms = set(limit_perm)
    
    return unique_perms
