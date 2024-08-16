import json
from pharm import GPC, PSP, Pharmadepot, Aversi
from flask import Flask, render_template, request
import pandas as pd

with open('paths.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_inputs(pharmacy):
    d = data[pharmacy]
    return [d['website'], d['search_box_xpath'], d['photo_xpath'], d['name_xpath'], d['price_xpath'], d['country_xpath'], d['link_xpath']]


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', infos=[])


@app.route('/search', methods=['POST'])
def search():
    word = request.form.get('search_term')
    gp = GPC(*get_inputs('gpc'))
    gpc_infos = gp.show_items(word)
    ps = PSP(*get_inputs('psp'))
    ps_infos = ps.show_items(word)
    ph = Pharmadepot(*get_inputs('pharmadepot'))
    ph_infos = ph.show_items(word)
    av = Aversi(*get_inputs('aversi'))
    av_infos = av.show_items(word)
    items_infos = gpc_infos + ps_infos + ph_infos + av_infos
    # print(items_infos)

    items_infos = sorted(items_infos, key=lambda x: x['Price'])
    return render_template('index.html', infos=items_infos)


if __name__ == '__main__':
    app.run(debug=True)

