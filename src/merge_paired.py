import os
import subprocess
from seq_paired import Seq_paired


class Merge_paired():
    def __init__(self):
        ""

    def __call__(self, category_objects, category_name, category_num, forward):
        print("STEP 2: Merge paired end")
        #create folder and write files
        list_files = []
        print(forward.split('_')[0])
        folder_name = forward.split('_')[0] +"_merged"
        try:
            os.mkdir(folder_name)
        except:
            print("folder existed")

        for n, object in enumerate(category_objects):
            r1, r2 = object.get()
            if len(r1) > 0:

                file_name_r1 = folder_name+'/'+ category_name[n] + "_" + forward.split('_')[0] + ".R1.fastq"
                file_name_r2 = folder_name+'/'+ category_name[n] + "_" + forward.split('_')[0] + ".R2.fastq"
                with open(file_name_r1, 'w') as wt_r1, open(file_name_r2, 'w') as wt_r2:
                    list_files.append(file_name_r1)
                    for line in r1:
                        wt_r1.write(line+'\n')

                    for line in r2:
                        wt_r2.write(line + '\n')

                # run pandaseq to merge
                file_name_out = folder_name+'/'+ category_name[n] + "_" + forward.split('_')[0] + ".merged.fastq"
                command = ["/mnt/home/choiji22/software/pandaseq-2.11/pandaseq","-F","-f",file_name_r1,"-r",file_name_r2,"-w",file_name_out]
                print(' '.join(command))

                try:
                    proc = subprocess.call(command) 
                except:
                    print("pandaseq error")
                    


