chembl_tools
============

A series of scripts to make the most of the (ChEMBL API)[https://github.com/chembl/chembl_webresource_client].

prerequisites
-------------

* python 2.7+ (unfortunately the chembl client doesn't seem to work with python 3+)
* chembl_webresource_client

example
-------

Given a list of compound names, for instance:

    amoxicillin
    oxacillin
    amikacin
    rifampicin
    garbage
    pseudomonic acid

We first retrieve the corresponding ChEMBL IDs:

    >>> src/get_chembl_ids compounds.txt > compounds.tsv
    Found no exact match for "garbage", trying a search
    Found no match for "garbage", skipping
    Found no exact match for "pseudomonic acid", trying a search

We can then retrieve the Uniprot IDs for the targets of each compound in a predefined species:

    >>> src/get_target_ids compounds.tsv --organism "Escherichia coli"
    chembl  target
    CHEMBL1082      Q8GDC1
    CHEMBL1082      P00959
    CHEMBL1082      P62593
    CHEMBL1082      P00811
    CHEMBL1082      P0AD63
    CHEMBL1082      A5HJU3
    CHEMBL1082      Q5U7L7
    CHEMBL177       P0A9A6
    CHEMBL374478    P0A8V2 

Or retrieve similar molecules with a predefined similarity threshold:

    >>> src/get_similar_molecules compounds.tsv --similarity 99
    query   target
    CHEMBL177       CHEMBL3637935
    CHEMBL177       CHEMBL3348834
    CHEMBL177       CHEMBL1625316
    CHEMBL177       CHEMBL1625035
    CHEMBL1082      CHEMBL1433952
    CHEMBL1082      CHEMBL1367635
    CHEMBL1082      CHEMBL1473908
    CHEMBL1082      CHEMBL174
    CHEMBL819       CHEMBL3558540
    
Copyright
---------

    Copyright (C) <2017> EMBL-European Bioinformatics Institute

    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    Neither the institution name nor the name chembl_tools
    can be used to endorse or promote products derived from
    this software without prior written permission.
    For written permission, please contact <marco@ebi.ac.uk>.

    Products derived from this software may not be called chembl_tools
    nor may chembl_tools appear in their names without prior written
    permission of the developers. You should have received a copy
    of the GNU General Public License along with this program.
    If not, see <http://www.gnu.org/licenses/>.
