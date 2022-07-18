import array
import operator
from functools import reduce


def and_(clauses: array):
    if len(clauses) == 0:
        return None

    return reduce(operator.and_, clauses)