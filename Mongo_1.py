import pymongo
import json
from pprint import pprint
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.metflix
movies = db.movies
users = db.users
print('ok')
db.movies.drop()
db.users.drop()
metflix = client["metflix"]
rocky = {"title": "Rocky", "year": 1976}
movies.insert_one(rocky)
items = movies.find({"title": "Rocky"})
for item in items:
    print(item)

moi = {"nom": "Chigot", "Prenom": "Julien"}


users.insert_one(moi)
users = users.find({"nom": "Chigot"})
for user in users:
    print(user)

movieslist = [
    { "_id": "tt0075148", "title": "Rocky", "year": 1976 },
    { "_id": "tt0073195", "title": "Jaws", "year": 1975 },
    { "_id": "tt0082694", "title": "Mad Max 2", "year": 1981 },
    { "_id": "tt0082971", "title": "Raiders", "year": 1981 }
]
try:
    movies.insert_many(movieslist)
except:
    print("Erreur Insertion")

movies1981 = movies.find({"year": 1981})
print('Film de 1981')
for movie in movies1981:
    print(movie)

allmovies = movies.find()
print("Tout les films")
for movie in allmovies:
    print(movie)

Jaws = movies.find_one({"title": "Jaws"})
print('Film Jaws')
print(Jaws)

db2 = client.movies_artist
movies2 = db2.movies
artist = db2.artist
movies_artist = client["movies_artist"]
with open('movies.json') as f:
    file_data = json.load(f)
with open('movies_suite.json') as f2:
    file_data2 = json.load(f2)
with open('artists.json') as f3:
    file_data3 = json.load(f3)
movies2.drop()
artist.drop()
movies2.insert_many(file_data)
movies2.insert_many(file_data2)
artist.insert_many(file_data3)
# testartist = artist.find()
# for artist in testartist:
#     pprint(artist)
# testjson = movies2.find()
# for movies in testjson:
#     pprint(movies)


movies2.find({"year": 1997, "actors.role": "Jack Dawson"} )

for x in movies2.find({},{ "_id": 0, "title": 1 }).limit(12).sort("title", 1):
  pprint(x)
for x in movies2.find({},{ "_id": 0, "title": 1 }).limit(12).sort("title", -1):
  pprint(x)

v1979 = movies2.find({"year": 1979},{ "_id": 0, "title": 1, "year":1 }).count()
print(v1979)

for x in movies2.find({"$or" : [{"year": 1997}, {"actors._id": "artist:147"}] }).limit(3):
    pprint(x)

for x in movies2.find({"$and" : [{"year": 1997}, {"actors.role": "Jack Dawson"}]} ):
    pprint(x)
for x in movies2.find({"year": 1997, "actors.role": "Jack Dawson"} ):
    pprint(x)

for x in movies2.find({"director._id":"artist:4"}, {"country":0, "summary":0, "genre":0}).sort("year", -1):
    pprint(x)
for x in movies2.find({"director._id":"artist:4", "actors.role":"Maximus"}, {"country":0, "summary":0, "genre":0}).sort("year", -1):
    pprint(x)
critere_recherche = {"director._id":"artist:4", "actors.role":"Maximus"}
projection = {"country":0, "summary":0, "genre":0}
tri = '("year", -1)'
for x in movies2.find(critere_recherche, projection).sort(tri):
    pprint(x)
for x in movies2.find( {"year": { "$gte": 2000, "$lte": 2005 }}):
    pprint(x)

for x in movies2.find({"actors._id": {"$in": ["artist:34","artist:98","artist:1"]}}, {"title":1, "year":1, "actors":1}).sort([("year", 1), ("title", 1)]):
    pprint(x)
for x in movies2.find({"actors._id": {"$all": ["artist:23","artist:147"]}}):
    pprint(x)
for x in movies2.find({"actors._id": {"$nin": ["artist:34", "artist:98", "artist:1"]}}, {"title":1, "year":1, "actors":1}).sort([("year", -1), ("title", -1)]).limit(5):
    pprint(x)
print(movies2.count({"actors": {"$exists": False}}))
print(movies2.count({"actors": []}))
for x  in movies2.find({"actors": []}, {"_id" : 0, "title": 1, "actors" : 1} ):
    pprint(x)
# eastwood = artist.findOne({"first_name": "Clint", "last_name": "Eastwood"})
# for x in movies2.find({"director._id": eastwood['_id']}, {"title": 1, "director._id" : 1}):
#     pprint(x)
# for x in movies2.find({"title": {'$regex': 'RE'}}, {"actors": "null", "summary": 0}):
#     pprint(x)
for x in movies2.find ({"actors._id": "artist:147"}, {"title": 1, "actors": 1} ):
    pprint(x)
for x in movies2.find ({"actors._id": "artist:147"}, {"actors": 0, "summary": 0} ):
    pprint(x)