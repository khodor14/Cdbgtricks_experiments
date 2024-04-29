# Update experiments

## Human genomes
### Run the experiments
```
python bench_script.py path_to_cdbgtricks Bifrost path_to_ggcat human_genomes_directory/ 100 human_experiments
```
### Extract memory and disk
To extract the memory and disk for Cdbgtricks:
```
bash extractor_mem.sh GB ccdbgtricks_mem_disk_ >> cdbgtricks_mem_disk.txt
```
To extract the memory and disk for Bifrost:
```
bash extractor_mem.sh GB bifrost_memory_ >> bifrost_mem_disk.txt
```
To extract the memory and disk for GGCAT:
```
bash extractor_mem.sh GB ggcat_mem_ >> ggcat_mem_disk.txt
```

## E. coli genomes
### Run the experiments
```
python bench_script.py path_to_cdbgtricks Bifrost path_to_ggcat human_ecoli_directory/ 7055 ecoli_experiments
```
### Extract memory and disk
To extract the memory and disk for Cdbgtricks:
```
bash extractor_mem.sh KB ccdbgtricks_mem_disk_ >> cdbgtricks_mem_disk.txt
```
To extract the memory and disk for Bifrost:
```
bash extractor_mem.sh KB bifrost_memory_ >> bifrost_mem_disk.txt
```
To extract the memory and disk for GGCAT:
```
bash extractor_mem.sh KB ggcat_mem_ >> ggcat_mem_disk.txt
```

