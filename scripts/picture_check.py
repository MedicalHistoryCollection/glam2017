import csv, os, sys, re

input_file = sys.argv[1]
output_file = sys.argv[2]
picture_dir = sys.argv[3]

print('Checking images in file '+input_file+' against directory '+picture_dir)

with open(input_file) as f:
    with open(output_file, 'w') as g:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, reader.fieldnames)
        writer.writeheader()

        for row in reader:
            image_filename = row['Image']

            variations = [
                image_filename,
                'bd.'.join(image_filename.split('.')),
                'bdbis.'.join(image_filename.split('.')),
                'bisbd.'.join(image_filename.split('.')),
            ]

            found = False

            for v in variations:
                if os.path.exists(os.path.join(picture_dir, v)):
                    print(os.path.join(picture_dir, v))
                    row['Image'] = v
                    found = True

                    break

            if found:
                writer.writerow(row)

print('Done')