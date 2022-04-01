import os
filename, format = os.path.splitext('LAB6/dir-and-files/json.json')

if os.path.exists('LAB6/dir-and-files/json.json') and format==".json":     os.remove('LAB6/dir-and-files/json.json')