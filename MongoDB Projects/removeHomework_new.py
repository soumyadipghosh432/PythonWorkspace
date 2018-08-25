import pymongo

"""
db.grades.drop()
mongoimport --drop -d students -c grades grades1.json
"""


""" This program removes the lowest graded homework for each student.
    Each student in the collection contains two grades for homework along with other types in an array.
    After this program the grade with higher value will remain.
"""


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.school
col = db.students
unique_ids=set()

try:
    query = {}
    projection = {"_id": 1}
    cursor_ids = col.find(query, projection)
    for x in cursor_ids:
        unique_ids.add(x['_id'])
    #  print(unique_ids)
except Exception as e:
    print("Error : ", type(e), e)

total_deletes = 0

try:
    for x in unique_ids:
        query = {'_id': x}
        doc = col.find_one(query)
        newScores = []
        score1 = {}
        score2 = {}
        sc_1 = 0
        sc_2 = 0
        score_count = 0
        for res in doc['scores']:
            if res['type'] == 'homework':
                if score_count == 0:
                    score1 = res
                    score_count += 1
                    sc_1 = score1.get('score')
                else:
                    score2 = res
                    sc_2 = score2.get('score')
                    if sc_1 > sc_2:
                        newScores.insert(0, score1)
                    else:
                        newScores.insert(0, score2)

            else:
                newScores.insert(0,res)

        doc['scores'] = newScores
        col.replace_one({'_id': x}, doc)


except Exception as e:
    print("Error : ", type(e), e)
