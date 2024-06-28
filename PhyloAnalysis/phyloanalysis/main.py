def run_phyloanalysis():
    parser = argparse.ArgumentParser(description="Extract representative sequences from a FASTA file based on phylogenetic analysis.")
    parser.add_argument("input_file", 
                        help="Path to the input FASTA file containing sequences to analyze.")
    parser.add_argument("output_file", 
                        help="Path to the output FASTA file where representative sequences will be written.")
    parser.add_argument("--min_clades", type=int, default=3, 
                        help="Minimum number of clades to define (default: 3). The script will attempt to find at least this many clades.")
    parser.add_argument("--max_clades", type=int, default=6, 
                        help="Maximum number of clades to define (default: 6). The script will not exceed this number of clades.")
    parser.add_argument("--distance_method", choices=['identity', 'blastn'], default='identity',
                        help="Method to calculate distances for phylogeny. 'identity' uses simple sequence identity, 'blastn' uses BLAST nucleotide algorithm (default: identity).")
    parser.add_argument("--verbose", action="store_true", 
                        help="Increase output verbosity. If set, the script will print more detailed progress information.")

    args = parser.parse_args()

    # Set up logging based on verbosity
    import logging
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Call the main function with parsed arguments
    main(args.input_file, args.output_file, args.min_clades, args.max_clades, args.distance_method)

if __name__ == "__main__":
    run_phyloanalysis()
