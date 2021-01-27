# Flanker

Flanker is a tool for studying the homology of gene-flanking sequences. It will annotate FASTA or Multi-FASTA files for specified genes, then write the flanking sequences to new FASTA files.

# Usage

| Required arguments  | Description |
| --- | --- |
| ```--fasta_file``` | Input .fasta file |
| ```--gene``` **OR** ```--list_of_genes``` | Single gene to be found **OR** line-seperated list of genes|

| Optional arguments | Description | Default|
| --- | --- | --- |
| ```--help``` | Displays help information then closes Flanker | ```False``` |
| ```--flank``` | Choose which side(s) of the gene to extract (left/right/both)| ```both``` |
| ```--window``` | Flank length on either side of gene | ```1000``` |
| ```--wstop``` **AND** ```--wstep``` | For iterating: terminal flank length **AND** step size, ```--window``` becomes initial flank length | ```None``` |
| ```--circ``` | Add if your sequence is circularised | ```False``` |
| ```--include_gene``` | Add if you want the gene included in the output .fasta | ```False``` |
| ```--database``` | Specify the database Abricate will use to find the gene(s) | ```resfinder``` |

# Dependencies

The following Python packages are required for ```flanker.py```:

- [argparse](https://docs.python.org/3/library/argparse.html)
- [biopython](https://biopython.org)
- [numpy](https://numpy.org)
- [pandas](https://pandas.pydata.org)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [sys](https://docs.python.org/3/library/sys.html)

