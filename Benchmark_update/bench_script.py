import os
import timeit
import sys
cdbgtricks_bin="tobedefined"
Bifrost_bin="tobedefined"
ggcat_bin="tobedefined"
input_directory="tobedefined"
all_genomes="tobedefined"
kmersize=31
def cdbgtricks_index(command):
    command=f"{cdbgtricks_bin} {command}"
    print("ccdbgupdater index")
    os.system(command)
    
def cdbgtricks_convert(n):
    command=f"{cdbgtricks_bin} convert -it -ob -ig bifrost_graph.fasta -o updated_ccdbg_bin_{n}_graph"

    print("ccdbgupdater convert")
    os.system(command)
def convert_to_fasta(n):
    command=f"{cdbgtricks_bin} convert -ib -of -ig updated_ccdbg_bin_{i}_graph.bin -o bifrost_graph"    
    print(f"ccdbgupdater convert to fasta {n}")
    os.system(command)
def cdbgtricks_update(arguments):
    print("ccdbgupdater update")
    command=f"./script.sh {cdbgtricks_bin} update {arguments}"
    start=timeit.default_timer()
    os.system(command)
    end=timeit.default_timer()
    t=end-start
    print(f"time to update in ccdbgupdater is {t}")
    return t
def Bifrost_build(n):
    command=f"{Bifrost_bin} build"
    print("bifrost build")
    with open("Bifrost_list.txt","w") as f:
        for i in range(n):
            f.write(f"{all_genomes[i]}\n")
    command+=f" -r Bifrost_list.txt"
    command+=f" -k {kmersize} -o bifrost_graph -t 32 -f -n"   
    os.system(command)
    os.system("rm Bifrost_list.txt")
def Bifros_build_bfg(n):
    command=f"{Bifrost_bin} build"
    print("bifrost build with bifrost index")
    with open("Bifrost_list.txt","w") as f:
        for i in range(n):
            f.write(f"{all_genomes[i]}\n")
    command+=f" -r Bifrost_list.txt"
    command+=f" -k {kmersize} -o bifrost_build_1 -t 32 -b -n"   
    os.system(command)
    os.system("rm Bifrost_list.txt")
def Bifrost_update(n):
    print(f"Bifrost update {n}")
    command=f"./script.sh {Bifrost_bin} update -g bifrost_build_{n-1}.bfg -t 32 -r {all_genomes[n-1]} -k {kmersize} -I bifrost_build_{n-1}.bfi -b -o bifrost_build_{n} >> bifrost_memory_{n-1}.txt"
    start=timeit.default_timer()
    os.system(command)
    end=timeit.default_timer()
    os.system("rm bifrost_updated.fasta")
    t=end-start
    print(f"time to update in Bifrost for {n} is {t}")
    return t

def ggcat_build(n):
    print(f"ggcat update {n}")
    command=f"./script.sh {ggcat_bin} build -k {kmersize} -j 32 -s 1"
    with open("ggcat_list.txt","w") as f:
        for i in range(n):
            f.write(f"{all_genomes[i]}\n")
    
    command+=f" -l ggcat_list.txt -o ggcat_{n} >> ggcat_mem_{n-1}.txt"

    start=timeit.default_timer()
    os.system(command)
    end=timeit.default_timer()
    os.system(f"rm ggcat_{n}")
    os.system(f"ggcat_{n}.stats.log")
    t=end-start
    print(f"time to build in ggcat for {n} is {t}")
    os.system("rm ggcat_list.txt")
    return t
def help():
    print("python benchmarck_ccdbg.py path_to_ccdbgupdater_binary path_to_Bifrost_binary path_to_ggcat_binary path_to_directory_of_genomes number_of_genomes output_fname")
if __name__=="__main__":

    if len(sys.argv)<7:
        help() #show help
        exit(0)

    ccdbgupdated_bin=sys.argv[1]
    Bifrost_bin=sys.argv[2]
    input_directory=sys.argv[4]
    ggcat_bin=sys.argv[3]
    number_genomes=int(sys.argv[5])
    output_fname=sys.argv[6]
    all_genomes=[os.path.abspath(os.path.join(input_directory, p)) for p in os.listdir(input_directory)][:number_genomes]
    times_cdbgtricks_binary=dict()
    times_bifrost_update=dict()
    times_ggcat_build=dict()
    Bifrost_build(1)
    Bifros_build_bfg(1)
    cdbgtricks_convert(1)
    os.system("mv bifrost_graph.fasta bifrost_graph.fa")
    cdbgtricks_index(f"index -k {kmersize} -ig bifrost_graph.fa -m 11 -s 5000 -msb 4 -o updated_ccdbg_bin_1 -it")
    for i in range(2,len(all_genomes)+1,1):
        times_cdbgtricks_binary[i-1]=cdbgtricks_update(f"-k {kmersize} -ig bifrost_graph.fa -m 11 -s 5000 -msb 4 --input_genome {all_genomes[i-1]} -lgb updated_ccdbg_bin_{i-1}_graph.bin -ogb -u -li updated_ccdbg_bin_{i-1}_index.bin -oi -o updated_ccdbg_bin_{i} >> ccdbgtricks_mem_disk_{i-1}.txt") # ccdbgupdater_binary_mode_{i}.txt")
        if(not os.path.isfile(f"updated_ccdbg_bin_{i}_graph.bin")):
            break
        os.system("rm bifrost_graph.fa")
        os.system(f"rm updated_ccdbg_bin_{i-1}_graph.bin")
        os.system(f"rm updated_ccdbg_bin_{i-1}_index.bin")
        convert_to_fasta(i)
        os.system(f"rm updated_ccdbg_bin_{i}.txt")
        times_ggcat_build[i-1]=times_ggcat_build[i]
        times_bifrost_update[i-1]=Bifrost_update(i)
        if(i>2):
            os.system(f"rm bifrost_build_{i-1}.bfg")
            os.system(f"rm bifrost_build_{i-1}.bfi")
    with open(f"{output_fname}_cdbgtricks.txt","w") as outfile:
        outfile.write("genomes,time\n")
        for k,v in times_cdbgtricks_binary.items():
            outfile.write(f"{k},{v}\n")
    with open(f"{output_fname}_bifrost.txt","w") as outfile:
        outfile.write("genomes,time\n")
        for k,v in times_bifrost_update.items():
            outfile.write(f"{k},{v}\n")
    with open(f"{output_fname}_ggcat.txt","w") as outfile:
        outfile.write("genomes,time\n")
        for k,v in times_ggcat_build.items():
            outfile.write(f"{k},{v}\n")
    print("Done benchmarck")
