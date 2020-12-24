#!/usr/bin/env python3

import json
import os
import shutil
from base64 import b64encode
from http.client import HTTPSConnection

import yaml

import requests
from dotenv import load_dotenv
load_dotenv()

email = os.environ['EMAIL']
password = os.environ['PASSWORD']

c = HTTPSConnection("www.paprikaapp.com")

userAndPass = b64encode(bytes(email+":"+password, 'utf-8')).decode("ascii")
headers = { 'Authorization' : 'Basic %s' %  userAndPass }

def export_recipes():
    c.request('GET', '/api/v1/sync/categories/', headers=headers)
    res = c.getresponse()
    data = res.read()
    categories = {}
    for item in json.loads(data)['result']:
        categories[item['uid']] = item['name']

    c.request('GET', '/api/v1/sync/recipes/', headers=headers)
    res = c.getresponse()
    data = res.read()

    recipes = []
    for item in json.loads(data)['result']:
        c.request('GET', '/api/v1/sync/recipe/'+item['uid']+'/', headers=headers)
        res = c.getresponse()
        data = res.read()
        recipe = json.loads(data)['result']
        print(recipe['name'])
        if recipe['photo_url'] and recipe['photo_url'].startswith('http://uploads.paprikaapp.com.s3.amazonaws.com'):
            if not recipe['image_url']:
                recipe['image_url'] = '/images/recipes/'+recipe['photo']
            resp = requests.get(recipe['photo_url'], stream=True)
            local_file = open('images/'+recipe['photo'], 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)


        del recipe['photo_url']
        del recipe['photo']
        del recipe['hash']
        del recipe['photo_hash']
        del recipe['photo_large']

        if recipe['directions']:
            directions = recipe['directions'].split('\n')
            recipe['directions'] = []
            for direction in directions:
                if direction != '':
                    recipe['directions'].append(direction)

        if recipe['ingredients']:
            ingredients = recipe['ingredients'].split('\n')
            recipe['ingredients'] = []
            for ingredient in ingredients:
                if ingredient != '':
                    recipe['ingredients'].append(ingredient)

        if recipe['categories']:
            categoryList = []
            for category in recipe['categories']:
                categoryList.append(categories[category])
            recipe['categories'] = categoryList

        recipes.append(recipe)
    with open(r'./_data/recipes.yaml', 'w') as file:
        yaml.safe_dump(recipes, file)

if __name__ == "__main__":
    export_recipes()
