# Paprika Exporter

Export Paprika data using the API to yaml

# Introduction

This tool statically generates a list of Paprika recipes in YAML format, with a related folder of images.

# Installation

pip3 install papexp

# Github Action

In order to use the recipes.yml GitHub Action included with the repository you must create repository secrets with your Paprika EMAIL and PASSWORD

# Issues

Make sure to completely delete any recipes from the trash in the Paprika app because it can cause errors when exporting your recipes.

This code places the recipes yaml file in the _data/ directory, and creates it if it does not exist.

This code puts image files into assets/images/recipes, and creates that folder if it does not exist. This is not compatible with the original sstarcher code which used "images/recipes". You may need to relocate these files after retreval if it does not match your required file path.

# Example python code

import papexp
from papexp import core
papexp.core.checkandrun()

# Examples on the web

You can see this code live [here](https://shanestarcher.com/recipes) or on [chrisfnicholson.com][1].

The recipes exporter using Paprika Exporter are [here](https://github.com/sstarcher/sstarcher.github.io/blob/source/_data/recipes.yaml)

The repository for [chrisfnicholson.com][2] incorporates this code to routinely pull new recipes. 

This code is almost entirely the work of [Shane Starcher][3] with additions by [Chris Nicholson][4].



The goal with this package is to make implementation of this code on your website dead simple.

[1]:	https://chrisfnicholson.com/recipes/
[2]:	http://www.github.com/datapolitical/chrisfnicholson.github.io
[3]:	https://github.com/sstarcher
[4]:	https://github.com/datapolitical
