.. _whats-new-in-2.6:

****************************
  What's New in Python 2.6
****************************

:Author: A.M. Kuchling (amk at amk.ca)

.. $Id$
   Rules for maintenance:

   * Anyone can add text to this document.  Do not spend very much time
   on the wording of your changes, because your text will probably
   get rewritten to some degree.

   * The maintainer will go through Misc/NEWS periodically and add
   changes; it's therefore more important to add your changes to
   Misc/NEWS than to this file.

   * This is not a complete list of every single change; completeness
   is the purpose of Misc/NEWS.  Some changes I consider too small
   or esoteric to include.  If such a change is added to the text,
   I'll just remove it.  (This is another reason you shouldn't spend
   too much time on writing your addition.)

   * If you want to draw your new text to the attention of the
   maintainer, add 'XXX' to the beginning of the paragraph or
   section.

   * It's OK to just add a fragmentary note about a change.  For
   example: "XXX Describe the transmogrify() function added to the
   socket module."  The maintainer will research the change and
   write the necessary text.

   * You can comment out your additions if you like, but it's not
   necessary (especially when a final release is some months away).

   * Credit the author of a patch or bugfix.   Just the name is
   sufficient; the e-mail address isn't necessary.

   * It's helpful to add the bug/patch number in a parenthetical comment.

   XXX Describe the transmogrify() function added to the socket
   module.
   (Contributed by P.Y. Developer; :issue:`12345`.)

   This saves the maintainer some effort going through the SVN logs
   when researching a change.

This article explains the new features in Python 2.6, released on October 1,
2008.  The release schedule is described in :pep:`361`.

The major theme of Python 2.6 is preparing the migration path to
Python 3.0, a major redesign of the language.  Whenever possible,
Python 2.6 incorporates new features and syntax from 3.0 while
remaining compatible with existing code by not removing older features
or syntax.  When it's not possible to do that, Python 2.6 tries to do
what it can, adding compatibility functions in a
:mod:`future_builtins` module and a :option:`!-3` switch to warn about
usages that will become unsupported in 3.0.

Some significant new packages have been added to the standard library,
such as the :mod:`multiprocessing` and :mod:`json` modules, but
there aren't many new features that aren't related to Python 3.0 in
some way.

Python 2.6 also sees a number of improvements and bugfixes throughout
the source.  A search through the change logs finds there were 259
patches applied and 612 bugs fixed between Python 2.5 and 2.6.  Both
figures are likely to be underestimates.

This article doesn't attempt to provide a complete specification of
the new features, but instead provides a convenient overview.  For
full details, you should refer to the documentation for Python 2.6. If
you want to understand the rationale for the design and
implementation, refer to the PEP for a particular new feature.
Whenever possible, "What's New in Python" links to the bug/patch item
for each change.

.. Compare with previous release in 2 - 3 sentences here.
   add hyperlink when the documentation becomes available online.

.. ========================================================================
.. Large, PEP-level features and changes should be described here.
.. ========================================================================

Python 3.0
================

The development cycle for Python versions 2.6 and 3.0 was
synchronized, with the alpha and beta releases for both versions being
made on the same days.  The development of 3.0 has influenced many
features in 2.6.

Python 3.0 is a far-ranging redesign of Python that breaks
compatibility with the 2.x series.  This means that existing Python
code will need some conversion in order to run on
Python 3.0.  However, not all the changes in 3.0 necessarily break
compatibility.  In cases where new features won't cause existing code
to break, they've been backported to 2.6 and are described in this
document in the appropriate place.  Some of the 3.0-derived features
are:

* A :meth:`__complex__` method for converting objects to a complex number.
* Alternate syntax for catching exceptions: ``except TypeError as exc``.
* The addition of :func:`functools.reduce` as a synonym for the built-in
  :func:`reduce` function.

Python 3.0 adds several new built-in functions and changes the
semantics of some existing builtins.  Functions that are new in 3.0
such as :func:`bin` have simply been added to Python 2.6, but existing
builtins haven't been changed; instead, the :mod:`future_builtins`
module has versions with the new 3.0 semantics.  Code written to be
compatible with 3.0 can do ``from future_builtins import hex, map`` as
necessary.

A new command-line switch, :option:`!-3`, enables warnings
about features that will be removed in Python 3.0.  You can run code
with this switch to see how much work will be necessary to port
code to 3.0.  The value of this switch is available
to Python code as the boolean variable :data:`sys.py3kwarning`,
and to C extension code as :c:data:`!Py_Py3kWarningFlag`.

.. seealso::

   The 3\ *xxx* series of PEPs, which contains proposals for Python 3.0.
   :pep:`3000` describes the development process for Python 3.0.
   Start with :pep:`3100` that describes the general goals for Python
   3.0, and then explore the higher-numbered PEPs that propose
   specific features.


Changes to the Development Process
==================================================

While 2.6 was being developed, the Python development process
underwent two significant changes: we switched from SourceForge's
issue tracker to a customized Roundup installation, and the
documentation was converted from LaTeX to reStructuredText.


New Issue Tracker: Roundup
--------------------------------------------------

For a long time, the Python developers had been growing increasingly
annoyed by SourceForge's bug tracker.  SourceForge's hosted solution
doesn't permit much customization; for example, it wasn't possible to
customize the life cycle of issues.

The infrastructure committee of the Python Software Foundation
therefore posted a call for issue trackers, asking volunteers to set
up different products and import some of the bugs and patches from
SourceForge.  Four different trackers were examined: `Jira
<https://www.atlassian.com/software/jira/>`__,
`Launchpad <https://launchpad.net/>`__,
`Roundup <https://roundup.sourceforge.io/>`__, and
`Trac <https://trac.edgewall.org/>`__.
The committee eventually settled on Jira
and Roundup as the two candidates.  Jira is a commercial product that
offers no-cost hosted instances to free-software projects; Roundup
is an open-source project that requires volunteers
to administer it and a server to host it.

After posting a call for volunteers, a new Roundup installation was
set up at https://bugs.python.org.  One installation of Roundup can
host multiple trackers, and this server now also hosts issue trackers
for Jython and for the Python web site.  It will surely find
other uses in the future.  Where possible,
this edition of "What's New in Python" links to the bug/patch
item for each change.

Hosting of the Python bug tracker is kindly provided by
`Upfront Systems <https://upfrontsoftware.co.za>`__
of Stellenbosch, South Africa.  Martin von Löwis put a
lot of effort into importing existing bugs and patches from
SourceForge; his scripts for this import operation are at
``https://svn.python.org/view/tracker/importer/`` and may be useful to
other projects wishing to move from SourceForge to Roundup.

.. seealso::

  https://bugs.python.org
    The Python bug tracker.

  https://bugs.jython.org:
    The Jython bug tracker.

  https://roundup.sourceforge.io/
    Roundup downloads and documentation.

  https://svn.python.org/view/tracker/importer/
    Martin von Löwis's conversion scripts.

New Documentation Format: reStructuredText Using Sphinx
-----------------------------------------------------------

The Python documentation was written using LaTeX since the project
started around 1989.  In the 1980s and early 1990s, most documentation
was printed out for later study, not viewed online. LaTeX was widely
used because it provided attractive printed output while remaining
straightforward to write once the basic rules of the markup were
learned.

Today LaTeX is still used for writing publications destined for
printing, but the landscape for programming tools has shifted.  We no
longer print out reams of documentation; instead, we browse through it
online and HTML has become the most important format to support.
Unfortunately, converting LaTeX to HTML is fairly complicated and Fred
L. Drake Jr., the long-time Python documentation editor, spent a lot
of time maintaining the conversion process.  Occasionally people would
suggest converting the documentation into SGML and later XML, but
performing a good conversion is a major task and no one ever committed
the time required to finish the job.

During the 2.6 development cycle, Georg Brandl put a lot of effort
into building a new toolchain for processing the documentation.  The
resulting package is called Sphinx, and is available from
https://www.sphinx-doc.org/.

Sphinx concentrates on HTML output, producing attractively styled and
modern HTML; printed output is still supported through conversion to
LaTeX.  The input format is reStructuredText, a markup syntax
supporting custom extensions and directives that is commonly used in
the Python community.

Sphinx is a standalone package that can be used for writing, and
almost two dozen other projects
(`listed on the Sphinx web site <https://www.sphinx-doc.org/en/master/examples.html>`__)
have adopted Sphinx as their documentation tool.

.. seealso::

   `Documenting Python <https://devguide.python.org/documenting/>`__
       Describes how to write for Python's documentation.

   `Sphinx <https://www.sphinx-doc.org/>`__
     Documentation and code for the Sphinx toolchain.

   `Docutils <https://docutils.sourceforge.io>`__
     The underlying reStructuredText parser and toolset.


.. _pep-0343:

PEP 343: The 'with' statement
=============================

The previous version, Python 2.5, added the ':keyword:`with`'
statement as an optional feature, to be enabled by a ``from __future__
import with_statement`` directive.  In 2.6 the statement no longer needs to
be specially enabled; this means that :keyword:`!with` is now always a
keyword.  The rest of this section is a copy of the corresponding
section from the "What's New in Python 2.5" document; if you're
familiar with the ':keyword:`!with`' statement
from Python 2.5, you can skip this section.

The ':keyword:`with`' statement clarifies code that previously would use
``try...finally`` blocks to ensure that clean-up code is executed.  In this
section, I'll discuss the statement as it will commonly be used.  In the next
section, I'll examine the implementation details and show how to write objects
for use with this statement.

The ':keyword:`with`' statement is a control-flow structure whose basic
structure is::

   with expression [as variable]:
       with-block

The expression is evaluated, and it should result in an object that supports the
context management protocol (that is, has :meth:`~object.__enter__` and :meth:`~object.__exit__`
methods).

The object's :meth:`~object.__enter__` is called before *with-block* is executed and
therefore can run set-up code. It also may return a value that is bound to the
name *variable*, if given.  (Note carefully that *variable* is *not* assigned
the result of *expression*.)

After execution of the *with-block* is finished, the object's :meth:`~object.__exit__`
method is called, even if the block raised an exception, and can therefore run
clean-up code.

Some standard Python objects now support the context management protocol and can
be used with the ':keyword:`with`' statement. File objects are one example::

   with open('/etc/passwd', 'r') as f:
       for line in f:
           print line
           ... more processing code ...

After this statement has executed, the file object in *f* will have been
automatically closed, even if the :keyword:`for` loop raised an exception
part-way through the block.

.. note::

   In this case, *f* is the same object created by :func:`open`, because
   :meth:`~object.__enter__` returns *self*.

The :mod:`threading` module's locks and condition variables  also support the
':keyword:`with`' statement::

   lock = threading.Lock()
   with lock:
       # Critical section of code
       ...

The lock is acquired before the block is executed and always released once  the
block is complete.

The :func:`localcontext` function in the :mod:`decimal` module makes it easy
to save and restore the current decimal context, which encapsulates the desired
precision and rounding characteristics for computations::

   from decimal import Decimal, Context, localcontext

   # Displays with default precision of 28 digits
   v = Decimal('578')
   print v.sqrt()

   with localcontext(Context(prec=16)):
       # All code in this block uses a precision of 16 digits.
       # The original context is restored on exiting the block.
       print v.sqrt()


.. _new-26-context-managers:

Writing Context Managers
------------------------

Under the hood, the ':keyword:`with`' statement is fairly complicated. Most
people will only use ':keyword:`!with`' in company with existing objects and
don't need to know these details, so you can skip the rest of this section if
you like.  Authors of new objects will need to understand the details of the
underlying implementation and should keep reading.

A high-level explanation of the context management protocol is:

* The expression is evaluated and should result in an object called a "context
  manager".  The context manager must have :meth:`~object.__enter__` and :meth:`~object.__exit__`
  methods.

* The context manager's :meth:`~object.__enter__` method is called.  The value returned
  is assigned to *VAR*.  If no ``as VAR`` clause is present, the value is simply
  discarded.

* The code in *BLOCK* is executed.

* If *BLOCK* raises an exception, the context manager's :meth:`~object.__exit__` method
  is called with three arguments, the exception details (``type, value, traceback``,
  the same values returned by :func:`sys.exc_info`, which can also be ``None``
  if no exception occurred).  The method's return value controls whether an exception
  is re-raised: any false value re-raises the exception, and ``True`` will result
  in suppressing it.  You'll only rarely want to suppress the exception, because
  if you do the author of the code containing the ':keyword:`with`' statement will
  never realize anything went wrong.

* If *BLOCK* didn't raise an exception,  the :meth:`~object.__exit__` method is still
  called, but *type*, *value*, and *traceback* are all ``None``.

Let's think through an example.  I won't present detailed code but will only
sketch the methods necessary for a database that supports transactions.

(For people unfamiliar with database terminology: a set of changes to the
database are grouped into a transaction.  Transactions can be either committed,
meaning that all the changes are written into the database, or rolled back,
meaning that the changes are all discarded and the database is unchanged.  See
any database textbook for more information.)

Let's assume there's an object representing a database connection. Our goal will
be to let the user write code like this::

   db_connection = DatabaseConnection()
   with db_connection as cursor:
       cursor.execute('insert into ...')
       cursor.execute('delete from ...')
       # ... more operations ...

The transaction should be committed if the code in the block runs flawlessly or
rolled back if there's an exception. Here's the basic interface for
:class:`DatabaseConnection` that I'll assume::

   class DatabaseConnection:
       # Database interface
       def cursor(self):
           "Returns a cursor object and starts a new transaction"
       def commit(self):
           "Commits current transaction"
       def rollback(self):
           "Rolls back current transaction"

The :meth:`~object.__enter__` method is pretty easy, having only to start a new
transaction.  For this application the resulting cursor object would be a useful
result, so the method will return it.  The user can then add ``as cursor`` to
their ':keyword:`with`' statement to bind the cursor to a variable name. ::

   class DatabaseConnection:
       ...
       def __enter__(self):
           # Code to start a new transaction
           cursor = self.cursor()
           return cursor

The :meth:`~object.__exit__` method is the most complicated because it's where most of
the work has to be done.  The method has to check if an exception occurred.  If
there was no exception, the transaction is committed.  The transaction is rolled
back if there was an exception.

In the code below, execution will just fall off the end of the function,
returning the default value of ``None``.  ``None`` is false, so the exception
will be re-raised automatically.  If you wished, you could be more explicit and
add a :keyword:`return` statement at the marked location. ::

   class DatabaseConnection:
       ...
       def __exit__(self, type, value, tb):
           if tb is None:
               # No exception, so commit
               self.commit()
           else:
               # Exception occurred, so rollback.
               self.rollback()
               # return False


.. _new-module-contextlib:

The contextlib module
---------------------

The :mod:`contextlib` module provides some functions and a decorator that
are useful when writing objects for use with the ':keyword:`with`' statement.

The decorator is called :func:`contextmanager`, and lets you write a single
generator function instead of defining a new class.  The generator should yield
exactly one value.  The code up to the :keyword:`yield` will be executed as the
:meth:`~object.__enter__` method, and the value yielded will be the method's return
value that will get bound to the variable in the ':keyword:`with`' statement's
:keyword:`!as` clause, if any.  The code after the :keyword:`!yield` will be
executed in the :meth:`~object.__exit__` method.  Any exception raised in the block will
be raised by the :keyword:`!yield` statement.

Using this decorator, our database example from the previous section
could be written as::

   from contextlib import contextmanager

   @contextmanager
   def db_transaction(connection):
       cursor = connection.cursor()
       try:
           yield cursor
       except:
           connection.rollback()
           raise
       else:
           connection.commit()

   db = DatabaseConnection()
   with db_transaction(db) as cursor:
       ...

The :mod:`contextlib` module also has a ``nested(mgr1, mgr2, ...)`` function
that combines a number of context managers so you don't need to write nested
':keyword:`with`' statements.  In this example, the single ':keyword:`!with`'
statement both starts a database transaction and acquires a thread lock::

   lock = threading.Lock()
   with nested (db_transaction(db), lock) as (cursor, locked):
       ...

Finally, the :func:`closing` function returns its argument so that it can be
bound to a variable, and calls the argument's ``.close()`` method at the end
of the block. ::

   import urllib, sys
   from contextlib import closing

   with closing(urllib.urlopen('http://www.yahoo.com')) as f:
       for line in f:
           sys.stdout.write(line)


.. seealso::

   :pep:`343` - The "with" statement
      PEP written by Guido van Rossum and Nick Coghlan; im
