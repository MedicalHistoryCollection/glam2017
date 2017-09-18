import math
from jinja2 import Environment, PackageLoader, select_autoescape
import csv, os.path
import hashlib

env = Environment(
    loader=PackageLoader('scripts', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('carousel_template.html')

data_dir = 'data/'
html_dir = 'front/html/'
categories_file = 'categories.txt'  # Map of object categories to book classifications
photos_dir = 'photos_selection_by_category'  # Folder of photos selected for the website by IUHMS data owners
books_dir = 'books_selection_by_category'  # Folder of metadata for books selected for the website by IUHMS data owners
photos_file = 'pictures_database_existing.csv'  # Metadata file for objects where we know the photos exist

renovaud_link = "https://renouvaud.hosted.exlibrisgroup.com/primo_library/libweb/action/search.do;?fn=search&ct=search&initialSearch=true&mode=Basic&tab=default_tab&indx=1&dum=true&srt=rank&vid=41BCULIB_VU1&frbg=&tb=t&vl%28freeText0%29={}&scp.scps=scope%3A%2841BCU_BHL%29%2Cscope%3A%2841BCU_SERVAL%29%2Cscope%3A%2841BCU_RERODOC%29%2Cscope%3A%2841BCULAUSA_LIB%29%2CEbscoLocal%2Cprimo_central_multiple_fe"


def get_books(books, rank, books_per_object):
    """
    Get a list of books with renovaud links
    """
    book_slice = books[rank * books_per_object:rank * books_per_object + books_per_object]

    for book in book_slice:
        search_term = book['isbn'] if book['isbn'] != 'none' else book['title']

        book['renovaud_link'] = renovaud_link.format(search_term.replace(' ', '%20'))

    return book_slice


def get_wikimedia_link(row):
    """
    Get the image url for a photo uploaded to wikimedia
    """
    f = '.'.join(row['Image'].strip('0').split('.')[0:-1]) + '.jpg'
    filename = row['Title'].replace(' ', '_') + '_-_' + f

    m = hashlib.md5()
    m.update(filename.encode('utf-8'))
    md5 = m.hexdigest()

    base_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/'
    subdirs = md5[0] + '/' + md5[0:2] + '/'
    size = '/800px-'

    return base_url + subdirs + filename + size + filename


categories = {}

with open(os.path.join(data_dir, categories_file)) as f:
    for line in f:
        categories[line.split('\t')[-1].strip('\n')] = {
            'name': line.split('\t')[0],
            'photos': [],
            'books': []
        }

for cat in categories.keys():
    # Get filenames of selected photos for each category
    photos = []

    photo_dir = os.path.join(data_dir, photos_dir, cat)
    if not os.path.isdir(photo_dir):
        continue

    for p in os.listdir(photo_dir):
        photos.append(p)

    categories[cat]['photos'] = photos

    # Get book metadata for each category
    books = []

    categories_with_books = os.listdir(os.path.join(data_dir, books_dir))
    if not cat + '.csv' in categories_with_books:
        continue

    books_metadata = os.path.join(data_dir, books_dir, cat + '.csv')

    with open(books_metadata) as b:
        reader = csv.DictReader(b)
        for row in reader:
            books.append(
                {
                    'title': row['Title'],
                    'isbn': row['ISBN'],
                    'renovaud_link': ''
                }
            )

    categories[cat]['books'] = books

photo_metadata = os.path.join(data_dir, photos_file)

# One html page per category
for cat in categories.keys():
    if not categories[cat]['photos']:
        continue

    context = {
        'name': categories[cat]['name'],
        'objects': []
    }
    photos = categories[cat]['photos']
    books = categories[cat]['books']

    # Get necessary metadata for the category objects and books
    with open(photo_metadata) as f:
        reader = csv.DictReader(f)
        n = 0
        books_per_object = math.floor(len(books) / len(photos))

        for row in reader:
            if not row['Image'] in photos:
                continue

            obj = {
                'rank': n,
                'title': row['Title'],
                'description': row['Description'],
                'image_link': get_wikimedia_link(row),
                'books': get_books(books, n, books_per_object)
            }

            context['objects'].append(obj)
            n += 1

    # Actually render the html pages
    if not os.path.isdir(html_dir):
        os.mkdir(html_dir)

    with open(os.path.join(html_dir, context['name'] + '.html'), 'w') as g:
        print('Rendering template for category', context['name'])

        g.write(template.render(context))

print('Done')
