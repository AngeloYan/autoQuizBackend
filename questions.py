#!/usr/bin/py

from imdb import IMDb,IMDbError
import sys
import random
import json

def makeQ(topic):
    ia = IMDb()
    people = ia.search_person(topic)
    print(ia.get_movie_infoset())
    person = people[0]
    pid = person.personID
    questions = []
    question = ""
    hold = {}
    ia.update(person,info='filmography')
    # find latest movie
    #print(person.get('filmography'))
    title = 'actress'
    counter = 0
    for i in person.get('filmography'):
        if 'actor' in i:
            title = 'actor'
            break
        counter += 1
    films = person.get('filmography')[counter][title]
    for i in films:
        if 'status' in i.keys():
            continue
        latestMovie = i['title']
        break
    question = "What is the latest movie that " + person['name'] + " has acted in?"
    answers = []
    answers.append(latestMovie)
    while len(answers) < 4:
        x = random.choice(films)['title']
        if x not in answers:
            answers.append(x)
    questions.append([question,answers])
    # find a random movie and get the plot
    question = "What movie acted by " + person['name'] + " has the following plot?"
    movie = films[random.randint(4,len(films)-1)]   
    ia.update(movie,info='plot')
    question = "What is the movie starring " + person['name'] + " featuring this plot: " + movie['plot'][0].split('.')[0]
    answers = []
    answers.append(movie['title'])
    while len(answers) < 4:
        x = random.choice(films)['title']
        if x not in answers:
            answers.append(x)
    questions.append([question,answers])
    
    # shuffle and turn into json
    random.shuffle(questions)
    for i,j in enumerate(questions):
        hold[str(i)] = j
    return json.dumps(hold)

topic = sys.argv[1]
print(makeQ(topic))
