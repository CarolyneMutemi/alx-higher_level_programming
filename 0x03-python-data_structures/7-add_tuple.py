#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples."""
    new = ()
    for x, y in zip(tuple_a, tuple_b):
        if tuple_a.index(x) < 2 and tuple_b.index(y) < 2:
            new += (x + y,)
    return new
