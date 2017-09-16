# Take a csv of book metadata and export a csv with only rows containing a particular classification.

import csv, sys, re

input_file = sys.argv[1]
output_file = sys.argv[2]
classification = sys.argv[3]
classifications_found = {}

print('Exporting rows with classifications',classification,'in file',input_file,'and saving into file',output_file)

with open(input_file) as f:
    with open(output_file, 'w') as g:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, reader.fieldnames)
        writer.writeheader()

        for row in reader:
            c = row['Classification']
            if c in [classification, 'D'+classification]:  # D = Généralités
                if c not in classifications_found:
                    classifications_found[c] = 1
                else:
                    classifications_found[c] += 1

                writer.writerow(row)

print(classifications_found)
