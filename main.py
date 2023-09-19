import csv

# Define the input and output file paths
input_file = 'lucianq1.txt'
output_file = 'lucianq1.csv'

# Open the input and output files
with open(input_file, 'r') as txt_file, open(output_file, 'w', newline='') as csv_file:
    # Create a CSV writer with colon as the delimiter
    csv_writer = csv.writer(csv_file, delimiter=':')

    # Read each line from the text file and write it to the CSV file
    for line in txt_file:
        # Split the line by colon (":") and write to the CSV file
        parts = line.strip().split(':')
        csv_writer.writerow(parts)

print(f'Conversion from {input_file} to {output_file} is complete.')
