# Remove donor names from 'origin' column of object metadata, and find geolocationsl

import csv, sys, re, requests

api_key = "AIzaSyCQ8YLJ3J5CcGUBB9t9SdL-bSJRrbD_3po"

input_file = sys.argv[1]
output_file = sys.argv[2]

print('Fixing origins in file '+input_file+' and saving into file '+output_file)

ignore = [
    'Achat',
    'A compléter',
    '\v',
]

geocoded_locs = {}


def geocode(loc):
    if loc in geocoded_locs.keys():
        return geocoded_locs[loc]

    variations = [
        loc,
        loc.split(' ')[-1],
    ]

    for v in variations:
        print("Geocoding", v)

        r = requests.get("https://maps.googleapis.com/maps/api/geocode/json",
                         params={"address": v,
                                 "key": api_key})
        try:
            lat = r.json()["results"][0]["geometry"]["location"]["lat"]
            lng = r.json()["results"][0]["geometry"]["location"]["lng"]

            geocoded_locs[loc] = [lat, lng]

            return [lat, lng]
        except:
            geocoded_locs[loc] = None

            print("Unable to geocode " + v)

    return ['', '']


with open(input_file) as f:
    with open(output_file, 'w') as g:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        fieldnames.extend(['Lat', 'Lng'])
        writer = csv.DictWriter(g, fieldnames)
        writer.writeheader()

        for row in reader:
            origin = row['Origin']

            if not origin or origin in ignore:
                row['Origin'] = row['Lat'] = row['Lng'] = ''
                writer.writerow(row)

                continue

            name_pattern = r"((Dr|Mme)[\w+\s\-\.]+|Collections privées)?(, )?(.*)"
            m = re.search(name_pattern, origin)

            if not m:
                print(origin)
                continue

            donor = m.group(1) if m.group(1) else ''
            location = m.group(4).strip(' \x0b').split('\x0b')[-1]

            row['Origin'] = 'Collections privées, '+location if donor else origin
            row['Lat'] = row['Lng'] = ''

            if location:
                coords = geocode(location)
                [row['Lat'], row['Lng']] = coords

            writer.writerow(row)

print('Done')