import csv
import numpy as np

def get_avg_count(file_name):
    
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

    return avg

if __name__ == '__main__':

    SOURCE_FILE_NAME = 'time'
    DEST_FILE_NAME = 'time.csv' 
    csv_file = open(DEST_FILE_NAME, 'a')
    csv_wr = csv.writer(csv_file, delimiter=',')

    avg = get_avg_count(SOURCE_FILE_NAME)
    csv_wr.writerow([format(avg, '.2f')])

    csv_file.close()

    
