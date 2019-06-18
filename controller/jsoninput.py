import json, collections

def convtoarr(fileinput):
    filename = "static/data/"+fileinput+".json"
    if filename:
        with open(filename) as json_data:
            file = json.load(json_data)
    return file