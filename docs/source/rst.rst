=====================================================
reStructuredText
=====================================================

:Cheatcheat:
   * http://github.com/ralsina/rst-cheatsheet/raw/master/rst-cheatsheet.pdf
   * http://docutils.sourceforge.net/docs/ref/rst/directives.html

Important extensions:

* http://sphinx-doc.org/ext/todo.html

.. todo::

   add missing details about rst here.

Sections
----------------------------------------------------------------------   

RST allows to specify a number of sections. You can do this with the
various underlines::

      *********************
      Chapter
      *********************
      Section
      =====================
      Subsection
      ---------------------
      Subsubsection
      ^^^^^^^^^^^^^^^^^^^^^
      Paragraph
      ~~~~~~~~~~~~~~~~~~~~~

Exceltable
----------------------------------------------------------------------

we have integrated Excel table from
http://pythonhosted.org//sphinxcontrib-exceltable/ intou our sphinx
allowing the definition of more elaborate tables specified in
excel. Howere the most convenient way may be to use list-tables. The
documentation to list tables can be found at
http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table

Autorun
----------------------------------------------------------------------

Autorun is an extension for Sphinx_ that can execute the code from a
runblock directive and attach the output of the execution to the document. 

For example::

    .. runblock:: pycon
        
        >>> for i in range(3):
        ...    print i

Produces

.. runblock:: pycon
        
    >>> for i in range(3):
    ...    print i


Another example::

    .. runblock:: console

        $ date

Produces

.. runblock:: console

   $ date 

However, when it comes to excersises we do preferthe use of ipython
notebooks as this allows us to present them also to users as self
contained excersises.

Todo
----------------------------------------------------------------------
 
   ::
      
      .. todo:: an example

   .. todo:: an example
