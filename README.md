# Paprika Exporter

Export Paprika data using the API to yaml

# Introduction

This tool statically generates a list of Paprika recipes in YAML format, with a related folder of images.

# Installation

pip3 install papexp

# Issues

Make sure to delete recipes from the trash in the app because it can cause errors.

This code places the recipes yaml file in the _data/ directory, and creates it if it does not exist.

This code puts image files into assets/images/recipes, and creates that folder if it does not exist. This is not compatible with the original sstarcher code which used "images/recipes". You may need to relocate these files after retreval if it does not match your required file path.

# Example python code

import papexp
from papexp import core
papexp.core.checkandrun()

# Examples on the web

You can see this live on [chrisfnicholson.com][1]

[@datapolitical/chrisfnicholson.github.io][2] runs this code in its build_jekyll.yml workflow to routinely pull new recipes. An edited version is available as a workflow in this repository.

This code is almost entirely the work of [Shane Starcher][3]. I’m deeply grateful to him for building this.

My goal with this package is to make implementation of his code on your website dead simple.

[1]:	https://chrisfnicholson.com/recipes.html
[2]:	http://www.github.com/datapolitical/chrisfnicholson.github.io
[3]:	https://github.com/sstarcher/paprika-exporter
