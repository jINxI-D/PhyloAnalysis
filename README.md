# PhyloAnalysis# PhyloAnalysis

PhyloAnalysis is a command-line tool for phylogenetic analysis and representative sequence extraction from FASTA files. It calculates phylogenetic relationships between sequences, defines clades, and extracts representative sequences for each clade.

## Installation

You can install PhyloAnalysis using pip:
pip install PhyloAnalysis



## Usage

After installation, you can use PhyloAnalysis from the command line:
PhyloAnalysis input_file output_file [options]



### Arguments:

- `input_file`: Path to the input FASTA file containing sequences to analyze.
- `output_file`: Path to the output FASTA file where representative sequences will be written.

### Options:

- `--min_clades`: Minimum number of clades to define (default: 3).
- `--max_clades`: Maximum number of clades to define (default: 6).
- `--distance_method`: Method to calculate distances for phylogeny. Choose between 'identity' (default) or 'blastn'.
- `--verbose`: Increase output verbosity.

### Example:
PhyloAnalysis input.fasta output.fasta --min_clades 4 --max_clades 8 --distance_method blastn --verbose



## Features

- Phylogenetic tree construction using UPGMA method
- Flexible clade definition based on user-specified criteria
- Representative sequence extraction for each clade
- Support for different distance calculation methods (identity and BLAST)
- Verbose output option for detailed progress information

## Requirements

- Python 3.6 or higher
- BioPython
- NumPy

## Contributing

Contributions to PhyloAnalysis are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please contact Jinxi at jinxi001@e.ntu.edu.sg.

## Acknowledgments

- BioPython team for their excellent library
