import sys

def main():
    count = {}
    file_name = []
    for one_file in sys.argv[1:]:
        sample_name = one_file.split('_')[0]
        file_name.append(sample_name)
        for line in open(one_file,'r'):
            spl = line.strip().split('\t')
            temp = count.get(spl[0],{})
            temp[sample_name] = spl[1]
            count[spl[0]] = temp

    print("gene" + '\t' + '\t'.join(file_name))
    
    for item in count.items():
        result = [item[0]]
        for one_file in file_name:
            if one_file in item[1]:
                result.append(item[1][one_file])
            else:
                result.append("0")
        print('\t'.join(result))

if __name__ == "__main__":
    main()
