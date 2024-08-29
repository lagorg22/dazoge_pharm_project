import json
from pharm import GPC, PSP, Pharmadepot, Aversi
# from fastPharm import GPC, Pharmadepot
from flask import Flask, render_template, request
import concurrent.futures
import functools


with open('paths.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def get_inputs(pharmacy):
    d = data[pharmacy]
    return [d['search_url'], d['photo_xpath'], d['name_xpath'], d['price_xpath'], d['country_xpath'], d['link_xpath']]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', infos=[])


@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('search_term')
    items_infos = []
    partial_get_info = functools.partial(get_info, word=word, items_info=items_infos)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(partial_get_info, [ 'GPC', 'Pharmadepot', 'PSP'])

    items_infos = sorted(items_infos, key=lambda x: x['Price'])

    return render_template('index.html', infos=items_infos)

def get_info(obj, word, items_info):
    o = globals()[obj](*get_inputs(obj.lower()), pharmacy=obj)
    items_info.extend(o.show_items(word))

if __name__ == '__main__':
    app.run(debug=True)
