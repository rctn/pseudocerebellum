************
Mossy Fibers
************

Overview
========

Adapted from: https://en.wikipedia.org/wiki/Mossy_fiber_(cerebellum):

   Mossy fibers are one of the major inputs to cerebellum. There are many
   sources of this pathway, the largest of which is the cerebral cortex,
   which sends input to the cerebellum via the pontocerebellar
   pathway. Other contributors include the vestibular nerve and nuclei,
   the spinal cord, the reticular formation, and feedback from deep
   cerebellar nuclei. Axons enter the cerebellum via the middle and
   inferior cerebellar peduncles, where some branch to make contact with
   deep cerebellar nuclei. They ascend into the white matter of the
   cerebellum, where each axon branches to innervate granule cells in
   several cerebellar folia.

   See :ref:`microcircuit` for a diagram of mossy fibers.

Quantity
========   

In cat:

   So far, I have not found an explicit estimate of the total number of mossy fibers in cat.
   Instead, the numerical values provided are based on the divergence and convergence between
   cell types within a folium.  The unknown factor is the number of folia which are innervated
   by each mossy fiber.  Statements related to the quantity are below.

   Following from :cite:`ItoM-1984`, page 86:

   Mossy fiber-Purkinje cell ratio within the folia is 4:1 :cite:`PalkovitsM+2-1972`.
   If each mossy fiber afferent innervates two folis by branching in the white matter, there
   will be **2.4 x 10^6** mossy fibers in the whole cat cerebellum (a total number of Purkinje cells
   is assumed to be 1.2 x 10^6; :cite:`PalkovitsM+2-1971a`.  However, this is an overestimate
   if the mossy fibers branch more abundantly.


   "According to earlier data :cite:`PalkovitsM+2-1971b` the granule cell-glomerulus ratio is
   27-28:1, the mossy fiber-granule cell ratio is therefore 1:460."
   :cite:`PalkovitsM+2-1972`.  

   The granular layer contributed to 29.09% of the total cerebellar
   volume, their absolute number being *2.2 x 10^9*. :cite:`PalkovitsM+2-1971b` p. 29.

   The above two would mean 4.78 x 10^6 mossy fibers (2.2 x 10^9 granule cells / 460);

Structure
=========

   "Within a folium, a mossy fiber branches along the plane perpendicular to the long axis of the folium.
   Therefore, the cascade arborization of mossy fibers (Cajal, 1911) tends to be parallel with the
   dendritic arborization of Purkinje cells."  :cite:`ItoM-1984`, p. 87.


Connection to glomeruli
=======================


Divergence
----------

   "One mossy fiber breaks up (within a given folium) into about 16-17 mossy
   rosettes" (which glomeruli form around).  :cite:`PalkovitsM+2-1972`.
   From :cite:`ItoM-1984`, page 86:
   "If each mossy fiber afferent innervates two folis by branching in the white matter, ..."
   (Comment:: Would this mean about 32 glomeruli per mossy fiber)?


Convergence
-----------

   1?  (Comment: I think each glomeruli is associated with just one mossy fiber rosette.  However,
   in a table of properties used for a computational model (:cite:`DAngeloE+11-2016` Table 2)
   it says that both the convergence and divergence from mossy fibers to glomeruli is
   "not known" (row 2 of Table 2)). 


Connection to grannule cells
============================


Divergence
----------

Cat:
  1.7 x 10^3 (from :cite:`LoebnerEE-1989`, fig 2).

  From :cite:`PalkovitsM+2-1972`, p. 26:
  "Four mossy fibers entering a folium give rise to 16 rosettes
  each, hence a total of 64 glomeruli. Since one glomerulus has synaptic contacts with
  an average of 28 granule cells, the total number of granule cells reached by the 4 mossy
  fibers will be 1,792. Each granule cell is presumed to pick up excitatory impulses from
  4 glomeruli belonging to different mossy fibers by as many dendrites."

  but also, from the same paper, page 28:
  "The granule cells have
  4.17 dendrites, on average; *the average mossy rosette is contacted by 112 granule
  dendrites*. The number of postsynaptic units (dendrite digits) is 10.2/dendrite and
  1,142/glomerulus."

  At first, this seems contradictory, (28 granule cells vs 112 granule dendrites per glomerulus).
  As described in the section of Golomeruli to grannule connection :ref:`glomeruli_to_grannule`
  I think the fan out is 1,792 per mossy fiber (as given in :cite:`LoebnerEE-1989`, fig 2).

   
Convergence
-----------

Cat:
  
   4 (from :cite:`LoebnerEE-1989`, fig 2); 4.17 (from :cite:`PalkovitsM+2-1972`, p. 28).


Connection to Golgi cells
=========================

Divergence
----------

Cat:

   Unknown (:cite:`LoebnerEE-1989`, fig 2).

Convergence
-----------

Cat:

   Unknown (:cite:`LoebnerEE-1989`, fig 2).


Connection to DCN (Deep Cerebellar Nuclei)
==========================================

Divergence
----------

Cat:

   Unknown (:cite:`LoebnerEE-1989`, fig 2).

Convergence
-----------

Cat:

   Unknown (:cite:`LoebnerEE-1989`, fig 2).


.. comment tbldata:: table_loebner_fig2a
   :id_prefix: r

   Source cell  | Target cell  | Value              | Reference
   granule      | Cell count   | 2.2x10^9           | LoebnerEE-1989
   granule      | basket       | ?, 3.7x10^3        | LoebnerEE-1989
   granule      | golgi        | ?, 5.2x10^3        | LoebnerEE-1989
   granule      | purkinje     | 200x10^3, 8.5x10^4 | LoebnerEE-1989
   granule      | stellate     | ?, 3.6x10^3        | LoebnerEE-1989



.. footbibliography::



