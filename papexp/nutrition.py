import requests
import yaml
import os
import json
import pathlib
from dotenv import load_dotenv
load_dotenv()

# curl -d @recipe.json -H "Content-Type: application/json" "https://api.edamam.com/api/nutrition-details?app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}"

app_id = os.environ['APP_ID']
app_key = os.environ['APP_KEY']
n_headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
n_url = "https://api.edamam.com/api/nutrition-details?app_id=" + app_id + "&app_key=" + app_key

def get_item_nutrition(r):
    recip= r
    rec = dict((k, recip[k]) for k in ('ingredients', 'name', 'servings', 'directions'))
    rec['ingr'] = rec.pop('ingredients')
    rec['title'] = rec.pop('name')
    rec['yield'] = rec.pop('servings')
    rec['prep'] = rec.pop('directions')
    rec_dump=json.dumps(rec)
    c = requests.post(n_url, data=rec_dump, headers=n_headers)
    n_data = c.json()
    return n_data

def get_nutrition_data():
    pathlib.Path('_data').mkdir(parents=True, exist_ok=True)
    with open(r'./_data/recipes.yaml', 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    with open(r'./_data/recipes_nutrition.yaml', 'r') as stream2:
        nutrition_data = yaml.safe_load(stream2)
    for item in data_loaded:
        nuts_uid=item['uid']
        if nutrition_data.get(nuts_uid, 'empty') == 'empty' :
            nutrition_data[nuts_uid]=get_item_nutrition(item)
            print("added - " + item['name'])
        else:
            print("skipped - " + item['name'])
    with open(r'./_data/recipes_nutrition.yaml', 'w') as file:
        yaml.safe_dump(nutrition_data, file)

# url = 'https://api.edamam.com/api/nutrition-details?app_id=${YOUR_APP_ID}&app_key=${YOUR_APP_KEY}'
if __name__ == "__main__":
    get_nutrition_data()
