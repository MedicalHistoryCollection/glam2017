from jinja2 import Environment, PackageLoader, select_autoescape
import csv, os.path

env = Environment(
    loader=PackageLoader('scripts', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('carousel_template.html')
data_dir = 'data/'

categories = {}

with open(os.path.join(data_dir, 'categories.txt')) as f:
    for line in f:
        categories[(line.split('\t')[-1].strip('\n'))] = []

for cat in categories.keys():
    photos = []

    photo_dir = os.path.join(data_dir, 'pictures_per_categories', cat)
    if not os.path.isdir(photo_dir):
        continue

    for p in os.listdir(photo_dir):
        photos.append(p)

    categories[cat] = photos

photo_metadata = os.path.join(data_dir, 'pictures_database_existing.csv')
with open(photo_metadata) as f:
    reader = csv.DictReader(f)

# One html page per category
for cat in categories.keys():
    if not categories[cat]:
        continue

    context = {
        'name': '',
        'objects': []
    }
    photos = categories[cat]

    with open(photo_metadata) as f:
        reader = csv.DictReader(f)

        # Loop over objects
        n = 0
        for photo in photos:
            for row in reader:
                if row['Image'] in categories[cat]:
                    if not context['name']:
                        context['name'] = row['Category']

                    object = {}

                    object['rank'] = n
                    object['title'] = row['Title']
                    object['description'] = row['Description']
                    object['image_link'] = '' # Todo: get this from wikimedia
                    object['books'] = []

                    n += 1

                    context['objects'].append(object)

    with open(context['name'] + '.html', 'w') as g:
        print('Rendering template for category', context['name'])

        g.write(template.render(context))

    break



                # For each object, need: rank (from 0), title, description, image link, books

                # For each book, need: rero link, title