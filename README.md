# Cdbtricks_experiments
# Tool installation

## Cdbtricks
Refer to [Cdbgtricks](https://github.com/khodor14/Cdbgtricks) repository for details on how to install it. 
## Bifrost
  ```
  conda install -c bioconda bifrost
  ```
## GGCAT
To install GGCAT, you can refer to the [repository](https://github.com/algbio/ggcat)
Note that the version used is [this](https://github.com/algbio/ggcat/commit/840d7f333a8fa62b982403c50aeaca6bb8d6cd51)
## Fulgor
To install Fulgor, you can check the [repository](https://github.com/jermp/fulgor)
Note that the version used is [this](https://github.com/jermp/fulgor/commit/5ac5699dfb258ef21a987688b8f75fc27b6ecaf8)


# Downloading the datasets
## Human genomes
```
curl --cookie zenodo-cookies.txt "https://zenodo.org/records/7506049/files/human-dataset-part1.tar.xz?download=1" --output human_genomes1.tar.xz
curl --cookie zenodo-cookies.txt "https://zenodo.org/records/7506425/files/human-dataset-part2.tar.xz?download=1" --output human_genomes2.tar.xz
mkdir human_genomes
```
Then extract the files:

```
tar -xf human_genomes1.tar.xz -C human_genomes
tar -xf human_genomes2.tar.xz -C human_genomes
rm human_genomes1.tar.xz
rm human_genomes2.tar.xz
```
The fasta files are in the human_genomes directory
## E. coli genomes
```
mkdir ecoli
bash ecoli_downloads.sh
```
# Setup for memory and disk measurement

The script ```script.sh``` measure the disk and memory usage. You need to set ```_user``` to your username.
