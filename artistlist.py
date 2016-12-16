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

env = Environment(loader=FileSystemLoader(BASE_DIR))
index_template = env.get_template('templates/index.tmpl')
artist_template = env.get_template('templates/artist.tmpl')

# with open("list.csv", "r") as datafile:
#     data = unicodecsv.DictReader(datafile)
#     html = tpl.render({"data":data,
#                        "time_generated": datetime.now() })
#     with open("generate.html", 'w') as generated:
#         generated.write(html.encode('utf-8'))


#
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
    generateというフォルダが存在するなら、全てを消す
    """
    if os.path.isdir(GEN_DIR):
        shutil.rmtree(GEN_DIR)

def process_row(row):
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
    u"""
    nameにartist_pageのリンクを貼る
    表示されるのはnameのみ
    """
    html = index_template.render({
        "data":data,
        "time_generated": datetime.now()
        })
    index_target = os.path.join(GEN_DIR, "index.html")
    with open(index_target, 'w') as generated:
            generated.write(html.encode('utf-8'))

def create_artist_dir(row):

    if row["slug"] != "":
        slug = row["slug"]
    else:
        slug = slugify(row["name"])

    dir_name = os.path.join(GEN_DIR, "artist", slug)
    os.mkdir(dir_name)

def generate_artist_page(row):
    u"""
    個別ページでは、name以下の情報を全て載せる
    """
    pass

if __name__ == "__main__":
    cleanup()
    create_output_dir()
    copy_static()
    data = get_data()
    generate_index(data)
    for row in data:
        try:
            create_artist_dir(row)
        except OSError as e:
            print e
