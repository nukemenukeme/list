#!/Users/nukeme/.virtualenvs/list/bin/python
# -*- coding: utf-8 -*-

import requests
import unicodecsv
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import shutil
import time
from slugify import slugify

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
GEN_DIR = os.path.join(BASE_DIR, "generated/")

env = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")))
index_template = env.get_template('index.html.j2')
artist_template = env.get_template('artist.html.j2')

# with open("list.csv", "r") as datafile:
#     data = unicodecsv.DictReader(datafile)
#     html = tpl.render({"data":data,
#                        "time_generated": datetime.now() })
#     with open("generate.html", 'w') as generated:
#         generated.write(html.encode('utf-8'))

# ./
#  +- generated/
#      +-- index.html
#      +-- artist/
#            + -- artist1/
#                   + -- index.html
#            + -- artist2/
#                   + -- index.html

def cleanup():

    """
    Delete directory if exist named "generate" directory.
    """

    if os.path.isdir(GEN_DIR):
        shutil.rmtree(GEN_DIR)

def split_multiline(s):
    ret_arr = []
    lines = s.split
    for line in lines:
        split_line = line.split("|")

    # Name is always first part of split line
        name = split_line[0].strip()

        if (len(split_line) >= 2 and
            len(split_line[1].strip()) > 0):
            url = split_line[1].strip()
        else:
            url = None

        ret_arr.append({"name": name, "url": url})

def split_tags(t):
    ret_tags = []
    lines = t.split("\n")
    for line in lines:
        tag = line.strip()
        ret_tags.append(tag)
    return ret_tags

def process_row(row):
    if row["slug"] == "":
        row["slug"] = slugify(row["name"])
    row["tags"] = split_tags(row["tags"])
    return row

def get_data():
    with open("list.csv", "r") as datafile:
        return_arr = []
        for row in unicodecsv.DictReader(datafile):
            return_arr.append(process_row(row))
        return return_arr

def copy_static():
    from_dir = os.path.join(BASE_DIR, "static/")
    target_dir = os.path.join(GEN_DIR, "static/")
    shutil.copytree(from_dir, target_dir)

def create_output_dir():
    os.mkdir(GEN_DIR)
    os.mkdir(os.path.join(GEN_DIR, "artist"))

def generate_index(data):

    """
    Index page has only artist name. Name linked artist page.
    """

    html = index_template.render({
        "data":data,
        "time_generated": datetime.now()
        })
    index_target = os.path.join(GEN_DIR, "index.html")
    with open(index_target, 'w') as generated:
            generated.write(html.encode('utf-8'))

def create_artist_dir(row):
    slug = row["slug"]
    dir_name = os.path.join(GEN_DIR, "artist", slug)
    os.mkdir(dir_name)

def generate_artist_page(current, prv, nxt):

    """
    Artist page has all information without e-mail address.
    """

    slug = current["slug"]
    dir_name = os.path.join(GEN_DIR, "artist", slug)

    html = artist_template.render({
        "artist":current, "prv":prv, "nxt":nxt
        })
    index_target = os.path.join(dir_name, "index.html")
    with open(index_target, 'w') as generated:
            generated.write(html.encode('utf-8'))

    '''
    {% for artist in data %}
    <h1 class="{{ " ".join(artist.tags) }}">
      <a href="/artist/{{ artist.slug }}/" target="_blank">{{ artist.name }}</a>
    </h1>
    '''

if __name__ == "__main__":
    cleanup()
    create_output_dir()
    copy_static()
    data = get_data()
    print data
    generate_index(data)
    for n in xrange(len(data)):
        try:
            current = data[n]
            # Get preview and current for links
            if n == 0:
                prv = data[-1]
                nxt = data[1]
            elif n == len(data) - 1:
                prv = data[n-1]
                nxt = data[0]
            else:
                prv = data[n-1]
                nxt = data[n+1]
            create_artist_dir(current)
            generate_artist_page(current, prv, nxt)
        except OSError as e:
            print e
