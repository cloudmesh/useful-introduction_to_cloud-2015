#! /usr/bin/env python

from __future__ import print_function

import os
#from cloudmesh_common.util import dotdict
from cloudmesh.util.youtube import youtube
#from cloudmesh_base.Shell import grep
from sh import grep
from pprint import pprint

         
# video = youtube('CwHFaluDgzc')
# pprint (video.entry)
# import sys
# sys.exit()
    
result =  grep('-r', ':youtube:', 'docs/source/.').split("\n")[:-1]

print ("Generating the index for the following videos")
print (70 *"=")
pprint (result)
print (70 *"=")

errors = {}
videos = {}
for line in result:
    filename = line.split(":")[0].replace("/./", "/") 
    
    id = str(line.split(":youtube:")[1].replace("`",""))
    video = youtube(id, filename)
    videos[video.title] = video

f = open('docs/source/index_videos.rst', 'w')
print (".. _videos:", file=f)
print (file=f)
print ( 70 * "*", file=f)
print ("Videos", file=f)
print ( 70 * "*", file=f)
print (file=f)
print ("Table", file=f)
print ( 70 * "=", file=f)
print (file=f)
print (".. csv-table:: Videos", file=f)
print ("   :header: Status, Title, Page, Youtube ID", file=f)
print ("   :widths: 10, 60, 20, 10", file=f)
print (file=f)



for id in sorted(videos):
    video = videos[id]
    data = {
        'basename': video.filename.replace("docs/source/",""),
        'filename': video.filename.replace("docs/source/","").replace(".rst", ".html"),
        'url': video.url,
        'id': video.id,                
        'title': video.title,
        'updated': video.updated,
        'content' : video.content,
        'found': video.found
        }
    print ("   {found}, `{title} <{url}>`__, `{basename} <{filename}>`__, `{id} <{url}>`__".format(**data), file=f)

print (file=f)
print (file=f)
print (".. _videos_detail:", file=f)
print (file=f)

print ("Details", file=f)
print ( 70 * "=", file=f)
print (file=f)

for id in sorted(videos):
    video = videos[id]
    data = {
        'basename': video.filename.replace("docs/source/",""),
        'filename': video.filename.replace("docs/source/","").replace(".rst", ".html"),
        'url': video.url,
        'id': video.id,                
        'title': video.title,
        'updated': video.updated,
        'content' : video.content,
        'found': video.found
        }
    print (video, file=f)    
f.close()

    
