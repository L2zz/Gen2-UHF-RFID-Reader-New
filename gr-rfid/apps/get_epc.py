import sys
import csv
import numpy as np

def get_samples(file_name):

    src = open(file_name, 'r')
    
    samples= []
    while True:
        rn16_line = src.readline()
        if not rn16_line: break
        
        epc_line = src.readline()
        samples_in_epc = epc_line.split(' ')
        samples_in_epc.pop()
        samples.append(samples_in_epc)

    return samples

if __name__ == '__main__':
    SOURCE_FILE_NAME = sys.argv[1]
    DEST_FILE_NAME = sys.argv[1] + '.csv'
    csv_file = open(DEST_FILE_NAME, 'w')
    csv_wr = csv.writer(csv_file, delimiter=',')

    samples = get_samples(SOURCE_FILE_NAME)

    for epc_samples in samples:
        csv_wr.writerow(epc_samples)

    csv_file.close()
