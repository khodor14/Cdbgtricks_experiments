# Cdbtricks_experiments
# Tool installation

## Cdbtricks
  ```
  git clone --recursive https://github.com/khodor14/ccdbgUpdater.git
  cd ccdbgUpdater && mkdir build && cd build
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


