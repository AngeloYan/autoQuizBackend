#!/usr/bin/py

from imdb import IMDb,IMDbError
import sys

topic = sys.argv[1]
ia = IMDb()
people = ia.search_person(topic)
person = people[0]
pid = person.personID
ia.update(person,info='filmography')
if 'actor' in person.get('filmography')[0]:
    title = 'actor'
else:
    title = 'actress'
for i in person.get('filmography')[0][title]:
    if 'status' in i.keys():
        continue
    latestMovie = i['title']
    break

print(latestMovie)
