import csv, sys, re

input_file = sys.argv[1]
output_file = sys.argv[2]

print('Fixing ids in file '+input_file+' and saving into file '+output_file)

fieldnames = [
    'ID',
    'Image',
    'Title',
    'Category',
    'Domain',
    'Description',
    'Documentation',
    'Date',
    'Condition',
    'Creator',
    'Materials',
    'Origin'
]

with open(input_file) as f:
    with open(output_file, 'w') as g:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, fieldnames)
        writer.writeheader()

        for row in reader:
            code = row['ID']

            pattern1 = r"0\.(\d{1,3})" # waxes
            pattern2 = r"\d{1,4}" # older photos
            pattern3 = r"\-(\d{1,4})" # newer photos

            if re.match(pattern1, code):
                # print(code+' matches wax')

                number = re.match(pattern1, code).group(1)

                new_code = 'c.'+number.ljust(3, '0')
                image_name = 'cire-'+number.replace('0', '')+'.jpg'
            elif re.match(pattern2, code):
                # print(code+' matches older photo')

                number = re.match(pattern2, code).group(0)

                new_code = number.rjust(4, '0')
                image_name = new_code+'.jpg'
            elif re.match(pattern3, code):
                # print(code+' matches newer photo')

                number = re.match(pattern3, code).group(1)

                new_code = number.rjust(4, '0')
                image_name = 'IHM-'+new_code+'.jpg'
            else:
                print(code+' does not match anything')
                continue

            row['ID'] = new_code
            row['Image'] = image_name

            writer.writerow(row)

print('Done')