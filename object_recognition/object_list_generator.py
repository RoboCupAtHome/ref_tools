#! /usr/bin/env python

import os, sys
from collections import OrderedDict

image_dir = sys.argv[1]
images_paths = os.listdir(image_dir)

name2category = OrderedDict()

for image_path  in images_paths:
    elements = os.path.splitext(image_path)[0].split(' - ')
    name = elements[0]
    category = elements[1]
    name2category[name] = (category, image_path)

name2category = OrderedDict(sorted(name2category.iteritems(), key=lambda x: x[0]))

print """<html>
    <style type="text/css">
        table, th, td { border: 1px solid black; border-collapse: collapse; }

    </style>
    <body>
        <table>"""

for number, (name, (category, path)) in enumerate(name2category.iteritems()):
    image_str = '<img src="{}" width="200"/>'.format(image_dir + '/' + path)
    print """<tr>
        <td>{num}</td>
        <td>{image}</td>
        <td>{name} ({category})</td>
    </tr>""".format(num=number+1, image=image_str, name=name, category=category)

print """       </table>
    </body>
</html>"""

