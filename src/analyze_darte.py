import os
import sys
import argparse

from split_to_each_gene import split_gene
from seq_paired import Seq_paired
from merge_paired import Merge_paired

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--forward', dest='forward', action='store', required=True,
                        help='path to R1 reads in FASTQ format')
    parser.add_argument('-r', '--reverse', dest='reverse', action='store', required=True,
                        help='path to R2 reads in FASTQ format')
    parser.add_argument('-g', '--gene_list', required=True, dest='gene_list', action='store',
            help='list of target gene, category.tsv')
    parser.add_argument('-p', '--primer', required=True, dest='primer', action='store',
            help='list of primer, DARTE-QM.v3.primer')
    args = parser.parse_args()

    print(args.forward)
    print(args.reverse)
    print(args.gene_list)
    print(args.primer)
    #step 1 : split to each gene
    split = split_gene()
    category_objects, category_name, category_num = split(args.forward, args.reverse, args.gene_list, args.primer)
    tot = 0
    folder = args.forward.split('_')[0]
    os.mkdir(folder)
    for obj in category_objects:
        print(obj.get_name())
        r1, r2 = obj.get()
        if len(r1) > 1:
            fwrite = open(folder+'/'+obj.get_name()+"_R1_001.fastq",'w')
            rwrite = open(folder+'/'+obj.get_name()+"_R1_001.fastq",'w')
            fwrite.write('\n'.join(r1))
            rwrite.write('\n'.join(r2))
            fwrite.close()
            rwrite.close()
        tot = tot + len(r1)

    print(tot)


    # step 2 : merge, pandaseq?
    #merge = Merge_paired()
    #merged = merge(category_objects, category_name, category_num, args.forward)

    # step 3 : cluster OTU, cd-hit?


    # step 4 : count table

if __name__ == "__main__":
    main()
