# python both_r1_r2_blastn.py r1.blastn r2.blastn > output
import sys

def main():
    
    #read R1
    r1 = {}
    for line in open(sys.argv[1],'r'):
        spl_line = line.strip().split('\t')
        if int(spl_line[3]) > 100 and float(spl_line[2]) > 97:
            r1[spl_line[0]] = spl_line
    count = {}
    for line in open(sys.argv[2],'r'):
        spl_line = line.strip().split('\t')
        if int(spl_line[3]) > 100 and float(spl_line[2]) > 97:
            if spl_line[0] in r1:
                count[spl_line[1]] = count.get(spl_line[1], 0) + 1

    for item in count.items():
        print('\t'.join([item[0], str(item[1])]))


if __name__ == "__main__":
    main();
