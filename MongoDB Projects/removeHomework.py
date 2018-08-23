import pymongo

"""
db.grades.drop()
mongoimport --drop -d students -c grades grades1.json
"""


""" This program removes the lowest graded homework document for each student.
    Each student in the collection contains two grades for homework.
    After this program the grade with higher value will remain.
"""


connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
col = db.grades
unique_ids=set()

try:
    query = {}
    projection = {"student_id": 1, "_id": 0}
    cursor_ids = col.find(query, projection)
    for x in cursor_ids:
        unique_ids.add(x['student_id'])
    #  print(unique_ids)
except Exception as e:
    print("Error : ", type(e), e)

total_deletes = 0

try:
    for x in unique_ids:
        query = {'student_id':x, 'type':'homework'}
        cursor = col.find(query).sort('score', pymongo.ASCENDING)
        low_score = -99.00
        obj = None
        for y in cursor:
            if obj == None:
                obj = y['_id']
                low_score = y['score']
            if y['score'] < low_score:
                obj = y['_id']
                low_score = y['score']
            result = col.delete_one({"student_id": y['student_id'], "score": low_score})
            total_deletes += result.deleted_count

except Exception as e:
    print("Error : ", type(e), e)

print("Total Document deleted : ", total_deletes)