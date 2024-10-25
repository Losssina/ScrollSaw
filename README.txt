ScrollSaw v1.0
ScrollSaw is a method enabling to reduce the complexity of large paralogue-rich gene family by identifying and preserving the most slowly evolving genes (the rationale described in Elias et al., J Cell Sci 2012; doi:10.1242/jcs.101378). 

Tree-puzzle outputs are required as input data. The basis is a multiple (protein) alignment of all sequences analysed. The source organisms are divided according to their taxonomic classification into two or more (ideally monophyletic) groups and the sequence dataset is divided according to these predefined taxonomic groups. 
The taxonomic groups are represented by a number, the first being 00, the second 01, etc., included as the first two positions in the title of each sequence. From this main large alignment, alignments of all possible pairs of taxonomy-based sequence groups are extracted. For each alignment, the genetic distances are calculated by the Tree-puzzle program.

The input data for the ScrollSaw itself are the outputs from the TreePuzzle program. One file for each alignment. Alignments are named according to the number representing the taxonomic groups, i.e. 00_01.phy.dist for the file containing sequence data from taxonomic groups 00 and 01. 

The number of taxonomic groups is specified on line 41, 17 in the case of this study ((range(17), 2)))

The ScrollSaw script identifies all so-called minimal-distance pairs for each TreePuzzle-calculated distance matrix. 

The output consists of the following files:
- 0001minima.txt, 0002minima.txt etc. - files that contain the minimal-distance pairs and corresponding values for each pair of taxonomic groups
- outputScrollSaw.txt - final file containing sequences that passed ScrollSaw

System requirements
The script was tested with the following setup:
Python version: 3.9.0
Operating system: Windows 10 Enterprise, Version 22H2, OS Build 19045.4651
Dependencies: No external libraries are required, only Python's standard library is used

Please note that the script was only tested under the conditions listed above. It may require further testing to ensure compatibility with other Python versions or operating systems.

Test Dataset
The dataset (ScrollSaw_test_dataset_mafft.fasta) provided contains Arf family genes from three isolates within the Asgard Archaea group. Each taxonomic group is denoted by a number: 00, 01, and 02. These numbers should appear at the beginning of each sequence name to indicate the respective group to which the sequence belongs. The alignment is in FASTA format and was constructed by program on-line MAFFT (version 7) with default setting. Sequence names should not exceed 10 characters in length, as the TreePuzzle program requires the use of PHYLIP format, which has this limitation.

Next step is to create alignments for each possible pair of taxonomic groups and convert them to phylip format. The results for these pairwise alignments have been provided in three files: 00_01.phy, 00_02.phy and 01_02.phy. 

The three pairwise alignments are used as input for the TreePuzzle program. TreePuzzle calculates genetic distances between sequences and generates distance matrices for each alignment. In our study, we used TreePuzzle version 5.3 with the maximum likelihood mapping method and the WAG substitution matrix. The output includes three files named 00_01.phy.dist, 00_02.phy.dist, and 01_02.phy.dist, which are required as input data for the ScrollSaw script.

Installation Guide
No additional installation is required beyond Python itself. To run the script:

1. Install Python (version 3.9.0 or compatible).
2. Download the script file and input files (00_01.phy.dist, 00_02.phy.dist, and 01_02.phy.dist)
3. Specify number of taxonomic groups on line 41, e.g. ((range(17), 2))) for 17 taxonomic groups. If using test dataset, specify the number 3, i.e. ((range(3), 2)))
4. Open a command prompt (or terminal) and run the script by typing:
ScrollSaw.py
Alternatively, type:
python ScrollSaw.py

The result of this test dataset is the file outputScrollSaw.txt, which contains all sequences that passed the ScrollSaw analysis. Additionally, there are three output files 0001minima.txt, 0002minima.txt and 0102minima.txt, which contain the minimal-distance pairs and corresponding values. For verification, these files are included and can be downloaded.
