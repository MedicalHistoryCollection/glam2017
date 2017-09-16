import csv, os, sys

input_file = sys.argv[1]
output_file = sys.argv[2]
picture_dir = sys.argv[3]

print('Checking images in file '+input_file+' against directory '+picture_dir)

with open(input_file) as f:
    with open(output_file, 'w') as g:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, reader.fieldnames)
        writer.writeheader()

        with_picture = 0
        without_picture = 0

        for row in reader:
            image_filename = row['Image']

            variations = [
                image_filename,
                str.upper(image_filename),
                # Low-definition files:
                # 'bd.'.join(image_filename.split('.')),
                # 'bdbis.'.join(image_filename.split('.')),
                # 'bisbd.'.join(image_filename.split('.')),
            ]

            found = False

            for v in variations:
                if os.path.exists(os.path.join(picture_dir, v)):
                    print(os.path.join(picture_dir, v))
                    row['Image'] = v
                    found = True

                    break

            if found:
                with_picture += 1
                writer.writerow(row)
            else:
                without_picture += 1

print('Found pictures for ', with_picture, ' rows out of ', with_picture+without_picture)