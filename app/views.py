from app import app, db
from app.models import Joke
from flask import render_template, url_for, request, make_response, jsonify
from random import randint



@app.get('/')
def index():
    return render_template("jokes.html")


@app.post('/insert')
def insert():
    """ This function inserts the jokes into the database."""

    question = request.form['joke-question']
    answer = request.form['joke-response']

    entry = Joke(question=question, answer=answer)
    db.session.add(entry)
    db.session.commit()

    return make_response(jsonify([{"response":"success"}]), 200)


@app.get('/random_joke')
def random_joke():
    num_jokes = Joke.query.count()
    num = randint(1, num_jokes)
    joke = Joke.query.filter_by(id=num).first()
    # [
    #     {'id':1, 'question':'What’s the best thing about Switzerland?', 'answer':'I don’t know, but the flag is a big plus'},
    #     {'id':2, 'question':'Hear about the new restaurant called Karma?', 'answer':'There’s no menu: You get what you deserve.'},
    #     {'id':3, 'question':'Did you hear about the claustrophobic astronaut?', 'answer':'He just needed a little space.'},
    #     {'id':4, 'question':'How do you drown a hipster?', 'answer':'Throw him in the mainstream'},
    #     {'id':5, 'question':'What do you call a fake noodle?”', 'answer':'An impasta.'},
    # ]

    return make_response(jsonify([{"question": joke.question, "answer": joke.answer}]), 200)
    # return make_response(jsonify([{"question": "wanna hear a joke?", "answer": "Look in the mirror"}]), 200)

@app.get('/jokes/<int:joke_id>')
def jokes(joke_id):
    joke = Joke.query.filter_by(id=joke_id).first()
    
    return make_response(jsonify([{"question": joke.question, "answer": joke.answer}]), 200)
