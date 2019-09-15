import gzip
from string import maketrans
from itertools import izip
from seq_paired import Seq_paired


class split_gene():
    def __init__(self):
        ""

    def __call__(self, forward, reverse, gene_list, primer):
        print("STEP1: split gene into category")

        # read primer
        primer_f, primer_r = self.read_primer(primer)

        # read category
        category = {}
        category_name = []
        category_num = {}
        for line in open(gene_list,'r'):
            spl = line.strip().split('\t')
            category[spl[2]] = [spl[0], spl[1]]
            if not spl[0] in category_name:
                category_name.append(spl[0])
                category_num[spl[0]] = len(category_name) - 1
        #print(len(category_name))
        #print(category_num['16S'])
        # read file filter seq if not matching primer
        if forward.endswith("gz"):
            r1_open = gzip.open(forward,'r')
        else:
            r1_open = open(forward,'r')
        
        if reverse.endswith("gz"):
            r2_open = gzip.open(reverse,'r')
        else:
            r2_open = open(reverse, 'r')


        tmp_seq_r1 = []
        tmp_seq_r2 = []
        category_objects = [Seq_paired() for i in range(len(category_name))]
        
        for i, one_name in enumerate(category_name):
            category_objects[i].add_name(one_name)


        print(len(category_objects))

        with r1_open as r1_file, r2_open as r2_file:
            for i, (x, y) in enumerate(izip(r1_file, r2_file)):
                if not i % 4 == 3:
                    tmp_seq_r1.append(x.strip())
                    tmp_seq_r2.append(y.strip())
                    continue

                tmp_seq_r1.append(x.strip())
                tmp_seq_r2.append(y.strip())
                
                for item in primer_r.items():
                    if item[0] in tmp_seq_r1[1]:
                        for it in item[1]:
                            if it in tmp_seq_r2[1]:
                                tmp_num = category_num[category[item[1][2:]][0]]
                                category_objects[tmp_num].list_add(tmp_seq_r1, tmp_seq_r2)

                tmp_seq_r1 = []
                tmp_seq_r2 = []


        return category_objects, category_name, category_num

        

    def get_rc(self, seq):
        seq = seq.upper()
        trans = maketrans("AGCT","TCGA")
        seq = seq.translate(trans,'xm')
        seq = seq[::-1]
        return seq

    def read_primer(self, primer):
        primer_f = {}
        primer_r = {}
        name = ""
        for line in open(primer, 'r'):
            if line[:1] == ">":
                name = line.strip()[1:]
            else:
                if "F:" in name:
                    primer_f[self.get_rc(line.strip())] = name
                else:
                    primer_r[line.strip()] = name
                name = ""
        return primer_f, primer_r
