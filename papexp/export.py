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

def check_and_run():
    with open(r'./_data/recipes_status.json', 'rb') as file:
        old_data = file.read()
    c.request('GET', '/api/v1/sync/status/', headers=headers)
    res = c.getresponse()
    new_data = res.read()
    if new_data != old_data:
        with open(r'./_data/recipes_status.json', 'wb') as file:
            file.write(new_data)
        export_recipes()

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
        #! https://gist.github.com/mattdsteele/7386ec363badfdeaad05a418b9a1f30a
        print(recipe['name'])
        if recipe['photo_large']:
            recipe['photo'] = recipe['photo_large']
            addr = recipe['photo_large'][:-4]
            c.request('GET', "/api/v1/sync/photo/"+addr+"/", headers=headers)
            res = c.getresponse()
            data = res.read()
            photoData = json.loads(data)['result']
            recipe['photo_url'] = photoData['photo_url']


        if recipe['photo'] and recipe['photo_url'] and recipe['photo_url'].startswith('http://uploads.paprikaapp.com.s3.amazonaws.com'):
        #!if recipe['photo_url']:
            resp = requests.get(recipe['photo_url'], stream=True)
            local_file = open('assets/images/recipes/'+recipe['photo'], 'wb')
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, local_file)
            recipe['image_url'] = 'images/recipes/'+recipe['photo']


        del recipe['photo_url']
        del recipe['photo']
        del recipe['hash']
        del recipe['photo_hash']
        del recipe['photo_large']

        recipe['photos'] = []

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

    #! this gets all photos
    c.request('GET', '/api/v1/sync/photos/', headers=headers)
    res = c.getresponse()
    data = res.read()
    photos = json.loads(data)['result']
    for item in json.loads(data)['result']:
        c.request('GET', '/api/v1/sync/photo/'+item['uid']+'/', headers=headers)
        res = c.getresponse()
        data = res.read()
        photo = json.loads(data)['result']
        rec = [x for x in recipes if x['uid'] == photo['recipe_uid']]
        #! create newphoto dict with uid and filenamd
        newphoto = {}
        photo_name = photo['name']
        newphoto[photo_name] = 'images/recipes/'+photo['filename']
        rec[0]['photos'].append(newphoto)
        resp = requests.get(photo['photo_url'], stream=True)
        local_file = open('assets/images/recipes/'+photo['filename'], 'wb')
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)

    with open(r'./_data/recipes.yaml', 'w') as file:
        yaml.safe_dump(recipes, file)

if __name__ == "__main__":
    check_and_run()
