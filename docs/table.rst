
*****
Table
*****

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



