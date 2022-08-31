r"""
ref: pg 122 Python Cookbook

Problem (TypeError: 'generator' object is not subscriptable):
    
    You want to take a slice of data produced by an iterator (a sequence in general),
    but the normal slicing operator doesn't work.


>>> def count(n):
...     while True:
...             yield n
...             n += 1
...
>>> c = count(0)
>>> c[10:20]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'generator' object is not subscriptable
>>> # Now using islice()

Solution:

>>> import itertools
>>> for x in itertools.islice(c, 10, 20):
...     print(x)
...
10
11
12
13
14
15
16
17
18
19
>>>

Solution v2

data = {
    "name": "ACME",
    "shares": 100,
    "price": 542.23,
}

data.items()[:2]
data.items()["name"]
Solution => itertools.islice(Iterable, start, end)
islice(data.items(), 0, 2)

Discussion:

Iterators and generators can't normally be sliced, because no information is known about
their length (and they don't implement indexing). The result of islice() is an iterator
that produces the desired slice items, but it does this by consuming and discarding all
of the items up to the starting slice index. Further items are then produced by the islice
object until the ending index has been reached.
It's important to emphasize that islice() will consume data on the supplied iterator.
Since iterators can't be rewound, that is something to consider. If it’s important to go
back, you should probably just turn the data into a list first.
"""
import itertools

data = {
    "name": "ACME",
    "shares": 100,
    "price": 542.23,
}


def slice_subscriptable_dict(iterable):
    return iterable.items()[:2]


if __name__ == "__main__":
    sliced_data = itertools.islice(data.items(), 0, None)
    print(list(sliced_data))
