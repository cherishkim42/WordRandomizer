'''Flask quickstart. File is not named "flask.py" to prevent conflicting with Flask itself'''
# Much of this code is taken, with explicit permission from the author(s), from this link: http://flask.pocoo.org/docs/1.0/quickstart/

# import sys, random
import markov_nthorder
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    random_chain = markov_nthorder.main()
    return "RANDOMIZED BIBLICAL TEXT: " + random_chain
