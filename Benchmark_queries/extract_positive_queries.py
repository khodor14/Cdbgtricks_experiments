import sys
from Bio import SeqIO
def main():
    if invalidArguments():
        return
    read_and_extract(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
def read_and_extract(path_to_graph,length_kmer,num_k_mer,out_prefix):
    num_k_mer_so_far=0
    with open(f"{out_prefix}.fasta","w") as out_f:
        for record in SeqIO.parse(path_to_graph, "fasta"):
            out_f.write(f"> {record.id}\n")
            out_f.write(f"{str(record.seq)}\n")
            num_k_mer_so_far=num_k_mer_so_far+len(record)-length_kmer+1
            if num_k_mer_so_far>=num_k_mer:
                break
def invalidArguments():
    if len(sys.argv) != 5:
        print("Invalid argument length: <graph file> <k-mer length> <num k-mers> <outFilePrefix>")
        return True

    try: 
        int(sys.argv[2])
        int(sys.argv[3])
    except ValueError:
        print("Invalid argument type: <k-mer length: int> <num k-mers: int>")
        return True

    return False


if __name__ == "__main__":
    print('Hello')
    main()