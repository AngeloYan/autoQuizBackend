#!/usr/bin/py

from imdb import IMDb,IMDbError
import sys
import random
import json
import re

def makeQ(topic):
    countries = ["Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic","Chad","Chile","China","Colombia","Comoros","Congo, Democratic Republic of the","Congo, Republic of the","Costa Rica","Côte d’Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor (Timor-Leste)","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, North","Korea, South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia, Federated States of","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka","Sudan","Sudan, South","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","USA","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]
    ia = IMDb()
    people = ia.search_person(topic)
    #print(ia.get_movie_infoset())
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
        if 'actress' in i:
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
            answers.append(x.strip())
    for i in range(4):
        answers[i] = re.sub(r"\(.*\)","",answers[i])
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
            answers.append(x.strip())
    for i in range(4):
        answers[i] = re.sub(r"\(.*\)","",answers[i])
    questions.append([question,answers])
    # get a random movie and get a random location from it
    movie = films[random.randint(4,len(films)-1)]
    ia.update(movie,info='locations')
    counts = 0
    while not movie.get('locations'):
        movie = films[random.randint(4,len(films)-1)]
        ia.update(movie,info='locations')
        counts+=1
        if counts > 5:
            break
    if movie.get('locations'):
        country = random.choice(movie.get('locations'))
        m = country.split(',')
        country = m[-1].split(':')[0].strip()
        question = "Which one of these countries are a filming location for " + person['name'] + "'s film " + movie['title'] + "?"
        answers = []
        answers.append(country)
        while len(answers) < 4:
            x = random.choice(countries)
            if x not in answers:
                answers.append(x.strip())
        for i in range(4):
            answers[i] = re.sub(r"\(.*\)","",answers[i]).strip(')')
        questions.append([question,answers])
    # shuffle and turn into json
    random.shuffle(questions)
    for i,j in enumerate(questions):
        hold[str(i)] = j
    return json.dumps(hold)

topic = sys.argv[1]
print(makeQ(topic))
