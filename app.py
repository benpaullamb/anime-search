from dotenv import load_dotenv
from flask import Flask
import requests
import json
from pathlib import Path

load_dotenv()

app = Flask(__name__, static_url_path='', static_folder='./front-end/dist')

@app.route('/')
def index():
  html = Path('./front-end/dist/index.html')
  return html.read_text()

@app.route('/anime/search/<name>')
def anime_search(name):
  search_params = {
    'filter[text]': name
  }
  res = requests.get('https://kitsu.io/api/edge/anime', params=search_params)
  
  return json.dumps(res.json(), indent=2)