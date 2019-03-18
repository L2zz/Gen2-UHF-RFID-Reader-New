import sys
import csv
import numpy as np

def get_value_from_epc(file_name):

    src = open(file_name, 'r')
    
    values= []
    while True:
        rn16_line = src.readline()
        if not rn16_line: break
        
        epc_line = src.readline()
        value_in_epc = epc_line.split(' ')
        value_in_epc.pop()
        values.append(value_in_epc)

    return values

if __name__ == '__main__':
    SOURCE_FILE_NAME = sys.argv[1]
    DEST_FILE_NAME = sys.argv[1] + '.csv'
    csv_file = open(DEST_FILE_NAME, 'a')
    csv_wr = csv.writer(csv_file, delimiter=',')

    values = get_value_from_epc(SOURCE_FILE_NAME)

    for val in values:
        csv_wr.writerow(val)

    csv_file.close()
