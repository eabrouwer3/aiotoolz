aiotoolz
========

|Build Status| |Coverage Status| |Version Status|

An async port of the wonderful pytoolz/toolz library.

See the PyToolz documentation at https://toolz.readthedocs.io and the github page at https://github.com/pytoolz/toolz.

LICENSE
-------

New BSD. See `License File <https://github.com/pytoolz/toolz/blob/master/LICENSE.txt>`__.

Install
-------

``aiotoolz`` is not yet on the Python Package Index (PyPI), but soon you can install it like so:

::

    pip install aiotoolz
    
Currently, you can install it like so:

::

    pip install git+https://github.com/eabrouwer3/aiotoolz.git

Structure and Heritage
----------------------

``toolz`` is implemented in three parts:

|literal itertoolz|_, for operations on iterables. Examples: ``groupby``,
``unique``, ``interpose``,

|literal functoolz|_, for higher-order functions. Examples: ``memoize``,
``curry``, ``compose``,

|literal dicttoolz|_, for operations on dictionaries. Examples: ``assoc``,
``update-in``, ``merge``.

.. |literal itertoolz| replace:: ``itertoolz``
.. _literal itertoolz: https://github.com/pytoolz/toolz/blob/master/toolz/itertoolz.py

.. |literal functoolz| replace:: ``functoolz``
.. _literal functoolz: https://github.com/pytoolz/toolz/blob/master/toolz/functoolz.py

.. |literal dicttoolz| replace:: ``dicttoolz``
.. _literal dicttoolz: https://github.com/pytoolz/toolz/blob/master/toolz/dicttoolz.py

These functions come from the legacy of functional languages for list
processing. They interoperate well to accomplish common complex tasks.

Read our `API
Documentation <https://toolz.readthedocs.io/en/latest/api.html>`__ for
more details.

Example
-------

This builds a standard wordcount function from pieces within ``toolz``:

.. code:: python

    >>> def stem(word):
    ...     """ Stem word to primitive form """
    ...     return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")

    >>> from toolz import compose, frequencies, partial
    >>> from toolz.curried import map
    >>> wordcount = compose(frequencies, map(stem), str.split)

    >>> sentence = "This cat jumped over this other cat!"
    >>> wordcount(sentence)
    {'this': 2, 'cat': 2, 'jumped': 1, 'over': 1, 'other': 1}

Dependencies
------------

``aiotoolz`` supports Python 3.5+ with a common codebase.
It is pure Python and requires no dependencies beyond the standard
library.

It is, in short, a lightweight dependency.


.. CyToolz
   -------

   The ``toolz`` project has been reimplemented in `Cython <http://cython.org>`__.
   The ``cytoolz`` project is a drop-in replacement for the Pure Python
   implementation.
   See `CyToolz GitHub Page <https://github.com/pytoolz/cytoolz/>`__ for more
   details.

See Also
--------

-  `Underscore.js <https://underscorejs.org/>`__: A similar library for
   JavaScript
-  `Enumerable <https://ruby-doc.org/core-2.0.0/Enumerable.html>`__: A
   similar library for Ruby
-  `Clojure <https://clojure.org/>`__: A functional language whose
   standard library has several counterparts in ``toolz``
-  `itertools <https://docs.python.org/2/library/itertools.html>`__: The
   Python standard library for iterator tools
-  `functools <https://docs.python.org/2/library/functools.html>`__: The
   Python standard library for function tools

Contributions Welcome
---------------------

``aiotoolz`` aims to be a repository for utility functions, particularly
those that come from the functional programming and list processing
traditions. We welcome contributions that fall within this scope.

We also try to keep the API small to keep ``aiotoolz`` manageable.  The ideal
contribution is significantly different from existing functions and has
precedent in a few other functional systems.

Please take a look at our
`issue page <https://github.com/pytoolz/toolz/issues>`__
for contribution ideas.

Community
---------

See our ``toolz`` `mailing list <https://groups.google.com/forum/#!forum/pytoolz>`__.
We're friendly.

.. |Build Status| image:: https://travis-ci.org/eabrouwer3/aiotoolz.svg?branch=master
   :target: https://travis-ci.org/eabrouwer3/aiotoolz
.. |Coverage Status| image:: https://coveralls.io/repos/github/eabrouwer3/aiotoolz/badge.svg?branch=master
   :target: https://coveralls.io/github/eabrouwer3/aiotoolz?branch=master
.. |Version Status| image:: https://badge.fury.io/py/aiotoolz.svg
    :target: https://badge.fury.io/py/aiotoolz
 
