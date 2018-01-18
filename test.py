#!/usr/bin/python

import json
from pprint import pprint

data = json.load(open('climatological-values-legend.json'))

for d in data["campos"]:
    print ' - ' + d["descripcion"]
