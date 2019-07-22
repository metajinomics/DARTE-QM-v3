# DARTE-QM-v3

```
for x in *_R1_*.gz;do python DARTE-QM-v3/src/analyze_darte.py -f $x -r ${x%_R1_*}_R2_001.fastq.gz -p DARTE-QM.v3.primer -g category.tsv;done
```
