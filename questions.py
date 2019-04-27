#!/usr/bin/py

from imdb import IMDb,IMDbError
import sys
import random


def makeQ(topic):
    ia = IMDb()
    people = ia.search_person(topic)
    person = people[0]
    pid = person.personID
    questions = []
    question = ""
    hold = {}
    ia.update(person,info='filmography')
    # find latest movie
    if 'actor' in person.get('filmography')[0]:
        title = 'actor'
    else:
        title = 'actress'
    for i in person.get('filmography')[0][title]:
        if 'status' in i.keys():
            continue
        latestMovie = i['title']
        break
    print(person['name'])
    question = "What is the latest movie that " + person['name'] + " has acted in?"
    questions.append([question,latestMovie])
    
    # find a random movie and get the plot

    question = "What movie acted by " + person['name'] + " has the following plot?"
    print(person.get('filmography'))
    random.shuffle(questions)
    for i,j in enumerate(questions):
        hold[str(i)] = j
    return hold

#topic = sys.argv[1]
#print(makeQ(topic))