#!/Users/nukeme/.virtualenvs/list/bin/python
# -*- coding: utf-8 -*-

import requests
import unicodecsv
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import shutil

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

def create_output_dir():
    pass

def generate_index(data):
    u"""
    nameにartist_pageのリンクを貼る
    表示されるのはnameのみ
    """
    html = index_template.render({
        "data":data,
        "time_generated": datetime.now()
        })
    with open("index.html", 'w') as generated:
             generated.write(html.encode('utf-8'))
    pass

def generate_artist_page(row):
    u"""
    個別ページでは、name以下の情報を全て載せる
    """
    pass

if __name__ == "__main__":
    pass
