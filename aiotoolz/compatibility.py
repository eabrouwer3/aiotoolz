import operator
import sys
from paco import map, filter
PY3 = sys.version_info[0] == 3 and sys.version_info[1] > 4
PYPY = hasattr(sys, 'pypy_version_info')

__all__ = ('map', 'filter', 'range', 'zip', 'reduce', 'zip_longest',
           'iteritems', 'iterkeys', 'itervalues', 'filterfalse',
           'PY3', 'PYPY')

if PY3:
    map = map
    filter = filter
    range = range
    zip = zip
    from functools import reduce
    from itertools import zip_longest
    from itertools import filterfalse
    iteritems = operator.methodcaller('items')
    iterkeys = operator.methodcaller('keys')
    itervalues = operator.methodcaller('values')
    from collections.abc import Sequence
