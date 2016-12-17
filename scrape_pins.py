# !/usr/bin/env python
# encoding: utf-8

"""
This script assumes the following:
1. There is a pins.json file at the root of your project. Content is:
    ["87194087123", "23786982375", etc]
2. There is a auth.json file at the root of your project. Content is:
    {"access_token": "YOUR_ACCESS_TOKEN"}
"""

import json
import os
from urllib.request import urlopen

project_fp = 'your_project_filepath'
pins_fp = os.path.join(project_fp, 'pins.json')
auth_fp = os.path.join(project_fp,'auth.json')
output_fp = os.path.join(project_fp, 'output.json')

access_token = json.load(open(auth_fp))['access_token']
fields = ['id', 'link', 'note', 'url', 'attribution', 'board', 'color', 'counts',
          'created_at', 'creator', 'image', 'media', 'metadata', 'original_link']
url_params = '?access_token={}&fields={}'.format(access_token, '%2C'.join(fields))

with open(pins_fp) as f:
    pin_ids = json.load(f)

res = []
for i, pid in enumerate(pin_ids):
    print("{}/{}".format(i, len(pin_ids)), end='\r')
    query_url = "https://api.pinterest.com/v1/pins/{}".format(pid) + url_params
    response = urlopen(query_url)
    # TODO: Figure out what to do to get the JSON-formated string in req.
    #       req is bytes at this point, probably need to decode.
    str_response = 'do something here'
    json_result = json.loads(str_response)
    res.append(json_result)

json.dump(res, open(output_fp, 'w'))

