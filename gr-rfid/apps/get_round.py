import csv
import sys
import numpy as np

def get_samples_in_round(file_name):

    src = open(file_name, 'r')

    samples = []
    while True:
        rn16 = src.readline()
        if not rn16: break
        
        samples_in_rn16 = rn16.split(' ')
        samples_in_rn16.pop()
        samples.append(samples_in_rn16)

        epc = src.readline()
        samples_in_epc = epc.split(' ' )
        samples_in_epc.pop()
        samples.append(samples_in_epc)

    return samples

if __name__ == '__main__':
    SOURCE_FILE_NAME = sys.argv[1]
    DEST_FILE_NAME = sys.argv[1] + '.csv'

    csv_file = open(DEST_FILE_NAME, 'a')
    csv_wr = csv.writer(csv_file, delimiter=',')

    samples = get_samples_in_round(SOURCE_FILE_NAME)

    for sample in samples:
        csv_wr.writerow(sample)

    csv_file.close()
