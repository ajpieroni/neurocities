import csv

# in
input_file_tracking_data = './Dojo/_tracking_data_trial_1.txt'
output_file_tracking_data = 'tracking_data.csv'
import csv

# CSV header
header = ['seconds', 'point x', 'point y', 'point z', 'position x', 'position y', 'position z', 'flag']

# list to store the data rows
data_rows = []

#input
with open(input_file_tracking_data, 'r') as file:
    # skip header
    next(file)

    for line in file:
        values = line.strip().split('\t')
        data_rows.append(values)

with open(output_file_tracking_data, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    # header
    writer.writerow(header)
    
    # rows
    writer.writerows(data_rows)

printf("Export done.")