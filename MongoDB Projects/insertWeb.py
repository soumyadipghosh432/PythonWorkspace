import json
import pymongo
import urllib.request as urllib

conn = pymongo.MongoClient("mongodb://localhost")
db = conn.citibyke
stories = db.stations

#  Drop existing stories collection
stories.drop()

#  Get weburl for JSON
""" ============================================================================
    https://cran.r-project.org/web/packages/jsonlite/vignettes/json-apis.html 
    for more URLs with JSON endpoint 
============================================================================ """
webUrl = urllib.urlopen("https://feeds.citibikenyc.com/stations/stations.json")

#  Parse JSON in python object
parsed = json.loads(webUrl.read())

check = 0

for item in parsed['stationBeanList']:
    stories.insert_one(item)

