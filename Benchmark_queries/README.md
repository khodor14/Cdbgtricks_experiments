# Query experiments
## General set up
Cdbgtricks and Fulgor use temporary files during the creation of indices. So it is necessay to increase the number of files that can be opened simultaneously.
```
ulimit -n 2048
```
## Construction of graphs
### Prepare fof.txt for human genomes
```
find human_genomes/*.fa > human_genomes.txt
head -10 human_genomes.txt > human_10_genomes.txt
rm human_genomes.txt
```
### Construct a Cdbg for human genomes with Bifrost
```
Bifrost build -r human_10_genomes.txt -k 31 -t 32 -o human_graph -f -n
```
The output will be written to human_graph.fasta. The index of the graph is written to human_graph.bfi.
### Prepare the fof.txt for ecoli genomes
```
find ecoli/*.gz > ecoli_genomes.txt
```
### Construct a Cdbg for ecoli genomes with Bifrost
```
Bifrost build -r ecoli_genomes.txt -k 31 -t 32 -o ecoli_graph -f -n
```
The output will be written to ecoli_graph.fasta. The index of the graph is written to ecoli_graph.bfi.
## Indexing the graphs with Cdbgtricks
```
(time ./script.sh path/to/Cdbgtricks_binary index -ig human_graph.fasta -k 31 -m 9 -s 5000 -msb 1 -it -o human_cdbgtricks) |& tee human_cdbgtricks_build_index.txt
```
The output is written to human_cdbgtricks_index.bin
```
(time ./script.sh path/to/Cdbgtricks_binary index -ig ecoli_graph.fasta -k 31 -m 9 -s 5000 -msb 1 -it -o ecoli_cdbgtricks) |& tee ecoli_cdbgtricks_build_index.txt
```
The output is written to ecoli_cdbgtricks_index.bin
## Creating Fulgor indices
```
(time ./script.sh path/to/Fulgor_binary build -l human_10_genomes.txt -k 31 -m 9 -o human_index )|& tee human_fulgor_build.txt"
```
The output is written to human_index.fur
```
(time ./script.sh path/to/Fulgor_binary build -l ecoli_genomes.txt -k 31 -m 9 -o ecoli_index )|& tee ecoli_fulgor_build.txt"
```
The output is written to ecoli_index.fur
## Generating random sequences
To generate random sequences execute ```random_sequence_generator.py```
```
python random_sequence_generator.py 1000000 500 1000 random_queries
```
This will generate one million random sequences of length between 500 and 1000 bases. The output is written to random_queries.fasta
## Querying the random sequences
### Query with Bifrost
```
(time ./script.sh Bifrost query -g human_graph.fasta -I human_graph.bfi -k 31 -q random_queries.fasta -e 1 -o human_random_bifrost)|& tee human_random_bifrost_query.txt
```
The output is written to human_random_bifrost.tsv. The memory, disk and time are written to human_random_bifrost_query.txt.
```
(time ./script.sh Bifrost query -g ecoli_graph.fasta -I ecoli_graph.bfi -k 31 -q random_queries.fasta -e 1 -o ecoli_random_bifrost)|& tee ecoli_random_bifrost_query.txt
```
The output is written to ecoli_random_bifrost.tsv. The memory, disk and time are written to ecoli_random_bifrost_query.txt.
### Query with Cdbgtricks
```
( time ./script.sh path/to/Cdbgtricks_binary query -ig humam_graph.fasta -k 31 -it -li human_cdbgtricks_build_index.bin -qr random_queries.fasta -r 1 -o human_random_cdbgtricks)|& tee human_random_cdbgtricks.txt
```
The output is written to human_random_cdbgtricks.tsv. The memory, disk and time are written to human_random_cdbgtricks.txt
```
( time ./script.sh path/to/Cdbgtricks_binary query -ig ecoli_graph.fasta -k 31 -it -li ecoli_cdbgtricks_index.bin -qr random_queries.fasta -r 1 -o ecoli_random_cdbgtricks)|& tee ecoli_random_cdbgtricks.txt
```
The outputs is written to ecoli_random_cdbgtricks.tsv. The memory, disk and time are written to ecoli_random_cdbgtricks.txt
### Query with Fulgor
```
(time ./script.sh path/to/Fulgor_binary pseudoalign -i human_index.fur -q random_queries.fasta --threshold 1 -o human_random_fulgor)| & tee human_random_fulgor_align.txt
```
The output is written to human_random_fulgor.tsv. The memory, disk and time are written to human_random_fulgor_align.txt
```
(time ./script.sh path/to/Fulgor_binary pseudoalign -i ecoli_index.fur -q random_queries.fasta  --threshold 1 -o ecoli_random_fulgor)| & tee ecoli_random_fulgor_align.txt
```
The output is written to ecoli_random_fulgor.tsv. The memory, disk and time are written to ecoli_random_fulgor_align.txt

## Generating positive queries
### From human genomes graph
```
python extract_positive_queries.py humam_graph.fasta 31 750000000 positive_queries_human
```
The output is written to positive_queries_human.fasta.
### From ecoli genomes graph
```
python extract_positive_queries.py ecoli_graph.fasta 31 750000000 positive_queries_ecoli
```
## Querying the positive sequences
### Query with Bifrost
```
(time ./script.sh Bifrost query -g human_graph.fasta -I human_graph.bfi -k 31 -q positive_queries_human.fasta -e 1 -o human_positive_bifrost)|& tee human_positive_bifrost_query.txt
```
The output is written to human_positive_bifrost.tsv. The memory, disk and time are written to human_positive_bifrost_query.txt.
```
(time ./script.sh Bifrost query -g ecoli_graph.fasta -I ecoli_graph.bfi -k 31 -q positive_queries_ecoli.fasta -e 1 -o ecoli_positive_bifrost)|& tee ecoli_positive_bifrost_query.txt
```
The output is written to ecoli_positive_bifrost.tsv. The memory, disk and time are written to ecoli_positive_bifrost_query.txt.
### Query with Cdbgtricks
```
( time ./script.sh path/to/Cdbgtricks_binary query -ig humam_graph.fasta -k 31 -it -li human_cdbgtricks_build_index.bin -qr positive_queries_human.fasta -r 1 -o human_positive_cdbgtricks)|& tee human_positive_cdbgtricks.txt
```
The output is written to human_positive_cdbgtricks.tsv. The memory, disk and time are written to human_positive_cdbgtricks.txt
```
( time ./script.sh path/to/Cdbgtricks_binary query -ig ecoli_graph.fasta -k 31 -it -li ecoli_cdbgtricks_index.bin -qr positive_queries_ecoli.fasta -r 1 -o ecoli_positive_cdbgtricks)|& tee ecoli_positive_cdbgtricks.txt
```
The outputs is written to ecoli_positive_cdbgtricks.tsv. The memory, disk and time are written to ecoli_positive_cdbgtricks.txt
### Query with Fulgor
```
(time ./script.sh path/to/Fulgor_binary pseudoalign -i human_index.fur -q positive_queries_human.fasta --threshold 1 -o human_positive_fulgor)| & tee human_positive_fulgor_align.txt
```
The output is written to human_positive_fulgor.tsv. The memory, disk and time are written to human_positive_fulgor_align.txt
```
(time ./script.sh path/to/Fulgor_binary pseudoalign -i ecoli_index.fur -q positive_queries_ecoli.fasta  --threshold 1 -o ecoli_positive_fulgor)| & tee ecoli_positive_fulgor_align.txt
```
The output is written to ecoli_positive_fulgor.tsv. The memory, disk and time are written to ecoli_positive_fulgor_align.txt
