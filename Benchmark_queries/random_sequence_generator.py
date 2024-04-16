import random
import sys
def main():
    if invalidArguments():
        return
    genDNASequence(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), f"{sys.argv[4]}.fasta")

def invalidArguments():
    if len(sys.argv) != 5:
        print("Invalid argument length: <sequenceNumber> <sequenceLengthStart> <sequenceLengthEnd> <outFilePrefix>")
        return True

    try: 
        int(sys.argv[1])
        int(sys.argv[2])
        int(sys.argv[3])
    except ValueError:
        print("Invalid argument type: <int> <int> <int>")
        return True

    return False


def genDNASequence(sequences, lengthStart, lengthEnd,filePath):
    with open (filePath, "w") as f:
        for i in range(sequences):
            lengh=random.randint(lengthStart, lengthEnd)
            dnaSequence = ['']*lengh
            for j in range(lengh):
                dnaSequence[j]= genDNA(random.randint(0,3))
            dnaTitle = "> Sequence_"+str(i + 1) + "_" + str(sequences)
            f.write(dnaTitle)
            f.write('\n')
            f.write(''.join(dnaSequence))
            f.write('\n')
def genDNA(x):
    return {
        0: 'A',
        1: 'C',
        2: 'G',        3: 'T'
    }[x]

if __name__ == "__main__":
    main()