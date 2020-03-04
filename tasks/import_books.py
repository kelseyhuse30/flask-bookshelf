#!/usr/bin/env python

import os
import re
import sys
import csv
sys.path.insert(1, '/Users/kelseyhuse/flask-bookshelf')
print(sys.path)
from datetime import datetime 
from books import add_books

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def import_books():
    book_list = []
    with open('./goodreads_library_export.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            shelf = row[18]
            if shelf == "read":
                date_read = datetime.strptime(row[14], '%Y/%m/%d') if len(row[14]) > 1 else None
                book_list.append({
                    'id': row[0],
                    'title': row[1],
                    'author': row[2],
                    'rating': row[7],
                    'read': date_read,
                    'isbn': row[5].replace("=","").replace('"', "")
                })
    add_books(book_list)


if __name__ == '__main__':
    import_books()
