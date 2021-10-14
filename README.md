# Paprika Exporter

Export Paprika data using the API to yaml

# Introduction

This tool statically generates a list of Paprika recipes in YAML format, with a related folder of images. 

# Installation

pip3 install papexp

# Issues

Make sure to completely delete any recipes from the trash in the Paprika app because it can cause errors when exporting your recipes.

# Example python code

import papexp
from papexp import export
export.exportrecipes()

# Examples on the web

You can see this code live [here](https://shanestarcher.com/recipes) or on [chrisfnicholson.com][1].

The recipes exporter using Paprika Exporter are [here](https://github.com/sstarcher/sstarcher.github.io/blob/source/_data/recipes.yaml)

The repository for [chrisfnicholson.com][2] incorporates this code to routinely pull new recipes. 

This code is almost entirely the work of [Shane Starcher][3] with additions by [Chris Nicholson][4].



My goal with this package is to make implementation of his code on your website dead simple.

[1]:	https://chrisfnicholson.com/recipes/
[2]:	http://www.github.com/datapolitical/chrisfnicholson.github.io
[3]:	https://github.com/sstarcher
[4]:	https://github.com/datapolitical
