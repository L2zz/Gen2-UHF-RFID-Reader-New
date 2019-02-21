import sys
import csv
import numpy as np

def get_avg(file_name):
    
    src = open(file_name, 'r')

    count = 0
    avg = 0.0
    while True:
        line = src.readline()
        if not line: break
        avg += float(line)
        count += 1
    avg /= count
    avg *= 1000000

    return avg, count

if __name__ == '__main__':

    SOURCE_FILE_NAME = 'time/time'
    DEST_FILE_NAME = 'time/csv/' + sys.argv[1] + '.csv' 
    csv_file = open(DEST_FILE_NAME, 'a')
    csv_wr = csv.writer(csv_file, delimiter=',')

    avg,count = get_avg(SOURCE_FILE_NAME)
    csv_wr.writerow([format(avg, '.2f'), count])

    csv_file.close()

    
