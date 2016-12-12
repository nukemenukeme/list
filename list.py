#!/Users/nukeme/.virtualenvs/list/bin/python

import requests
import unicodecsv
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
tpl = env.get_template('template.html')

with open("list.csv", "r") as datafile:
    data = unicodecsv.DictReader(datafile)
    html = tpl.render({"data":data,
                       "time_generated": datetime.now() })
    with  open("generate.html", 'w') as generated:
        generated.write(html.encode('utf-8'))


def get_data():
    pass

def process_data():
    pass

def create_output_dir():
    pass

def generate_index(data):
    pass

def generate_artist_page(row):
    pass

if __name__ == "__main__":
    pass
