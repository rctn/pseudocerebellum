.. _table_loebner_fig2a:


Cells and connections in cat
----------------------------

The following table provides counts of cells and connections in the cat cerebellum.
The first two columns (*Source cell* and *Cell count*) are respectively a cell type
and the count (number) of cells of that type.  The values in the rest of the table
give the number of connections from the Source cell to Target cells.  These are
specified as a pair of numbers: FO,FI.  FO is fan-out (number of target cells each
source cell contacts) and FI is fan-in (number of source cells going to each target
cell).  Data is from Figure 2 in :cite:`LoebnerEE-1989`.


.. tblrender:: table_loebner_fig2a
   :expanded_col_title: "Cell count or Target cell"
   :ct_offset: 2
   :description:
      Values are either a Cell count, or FO,FI where FO is *fan-out* (number of target cells
      each source cell contacts) and FI is *fan-in* (number of source cells going to each
      target cell).
   :gridLayout:
      +-------------+----------+------------------------------------------------------------------+
      |             |          |  Target cell                                                     |
      | Source      | Cell     +------------+------------+------------+-------------+-------------+
      | cell        | count    | basket     | golgi      | granule    | purkinje    | stellate    |
      +=============+==========+============+============+============+=============+=============+
      | basket      |          |      -     |            |            |             |             |
      +-------------+----------+------------+------------+------------+-------------+-------------+
      | golgi       |          |            |            |            |             |             |
      +-------------+----------+------------+------------+------------+-------------+-------------+
      | granule     |          |            |            |      -     |             |             |
      +-------------+----------+------------+------------+------------+-------------+-------------+
      | purkinje    |          |            |            |            |      -      |             |
      +-------------+----------+------------+------------+------------+-------------+-------------+
      | stellate    |          |            |            |            |             |      -      |
      +-------------+----------+------------+------------+------------+-------------+-------------+






The table above was made using the `sphinxcontrib-filltableref <http://sphinxcontrib-filltableref.readthedocs.org/en/latest/>`_.
Sphinx extension.  See that link for documentation about the extension.


---

*Original version of Cells and connections in cat table*


The following version of the table was a prototype created using straight html.
Using html made it difficult to write and does not allow specifying the data on different pages as is done using the
`sphinxcontrib-filltableref <http://sphinxcontrib-filltableref.readthedocs.org/en/latest/>`_
Sphinx extension.  This prototype is being kept on the page (at least temporarily) to allow viewing
the difference in the methods for creating the tables (html method, vs Sphinx extension method).  To see the
differences in the methods click on the "Page source" link on the lower right.  That will show the
source of the page ("rst" code).


Each row in the following table lists source cells on the left and destination cells on the top.
The first column with numeric values gives the number of source cells.
The other entries gives FO, FI.  FO is fan-out (number of target cells each source contacts)
and FI is fan-in (number source cells going to each target).
All values are for the cat.

.. |data_table| raw:: html

   <table class="fifo_data">
   <tr><th>from_cell</th><th># cells</th><th>basket</th><th>golgi</th><th>granule</th><th>purkinje</th><th>stellate</th></tr>
   <tr><th><a class="reference internal" href="data/basket.html">basket</a></th>
       <td>7.5x10^6</td> <!-- # basket cells -->
       <td>-</td> <!-- basket to basket -->
       <td>&nbsp;</td>  <!-- basket to golgi -->
       <td>&nbsp;</td>  <!-- basket to granule -->
       <td>9, 7.5x10^6</td> <!-- basket to purkinje -->
       <td>&nbsp;</td>  <!-- basket to stellate -->
   </tr>
   <tr><th><a class="reference internal" href="data/golgi.html">golgi</a></th>
       <td>4.2x10^5</td> <!-- # golgi cells -->
       <td>?, ?</td>  <!-- golgi to basket -->
       <td>-</td>  <!-- golgi to golgi -->
       <td>5.2x10^3, ?</td> <!-- golgi to granule -->
       <td>&nbsp;</td> <!-- golgi to purkinje -->
       <td>&nbsp</td> <!-- golgi to sellate -->
   </tr>
   <tr><th><a class="reference internal" href="data/granule.html">granule</a></th>
       <td>2.2x10^9</td> <!-- # granule cells -->
       <td>?,3.7x10^3</td> <!-- granule to basket --> 
       <td><a class="reference internal" href="data/granule.html">?, 5.2x10^3</a></td> <!-- granule to golgi --> 
       <td>-</td> <!-- granule to granule -->
       <td>200x10^3, 8.5x10^4</td> <!-- granule to purkinje -->
       <td>?, 3.6x10^3</td> <!-- granule to stellate -->
   </tr>
   <tr><th><a class="reference internal" href="data/purkinje.html">purkinje</th>
       <td>1.3x10^6</td> <!-- # purkinje cells -->
       <td>&nbsp;</td> <!-- purkinje to basket -->
       <td>&nbsp;</td>  <!-- purkinje to golgi -->
       <td>&nbsp;</td>  <!-- purkinje to granule -->
       <td>-</td>  <!-- purkinje to purkinje -->
       <td>&nbsp;</td> <!-- purkinje to stellate -->
   </tr>
   <tr><th><a class="reference internal" href="data/stellate.html">stellate</th>
       <td>2.1x10^7</td>
       <td>&nbsp;</td> <!-- stellate to basket -->
       <td>&nbsp;</td> <!-- stellate to golgi -->
       <td>&nbsp;</td> <!-- stellate to granule -->
       <td>3, 26</td> <!-- stellate to purkinge -->
       <td>-</td> <!-- stellate to stellate -->
   </tr>
   </table>


|data_table|
