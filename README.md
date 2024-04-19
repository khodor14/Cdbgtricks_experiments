# Cdbtricks_experiments
# Tool installation

## Cdbtricks
  ```
  git clone --recursive https://github.com/khodor14/Cdbgtricks.git
  cd Cdbgtricks && mkdir build && cd build
  cmake -S ../ -B .
  make
  ```
## kmtricks
Cdbtricks relies on kmtricks to find the set of new k-mers. To intall kmtricks
* From [Bioconda](https://bioconda.github.io):

* From [Bioconda](https://bioconda.github.io):

  ```
  conda install -c conda-forge -c tlemane kmtricks (latest version)
  ```
## Bifrost
  ```
  conda install -c bioconda bifrost
  ```
## GGCAT
GGCAT is implemented in rust. Therefore, rust toolchain is required:
### Rust installation
  ```
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
  rustup toolchain install stable
  ```
### GGCAT installation 
  ```
  git clone https://github.com/algbio/ggcat --recursive
  cd ggcat/
  cargo install --path crates/cmdline/ --locked
  ```
the binary is automatically copied to ```$HOME/.cargo/bin```

To launch the tool directly from the command line, the above directory should be added to the $PATH variable.
## Fulgor

### intalling zlib
```
sudo apt-get install zlib1g
```
### Fulgor installation
```
git clone https://github.com/jermp/fulgor.git
git submodule update --init --recursive
mkdir build
cd build
cmake ..
make -j
```

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
