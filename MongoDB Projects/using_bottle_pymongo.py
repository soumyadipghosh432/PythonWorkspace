import sys
import bottle
import pymongo

@bottle.route('/comboApp/<key>')
def index(key):
    conn = pymongo.MongoClient("mongodb://localhost")
    db = conn.myDB
    col = db.myCollection
    dataSet = col.find()
    for x in dataSet:
        if x.get('name') == key:
            return bottle.template('<b>The age of {{person}} is {{age}}', person=key, age=x.get('age'))


bottle.run(host='localhost', port=8888)
