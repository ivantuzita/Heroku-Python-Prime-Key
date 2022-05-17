import flask
from flask import send_from_directory
from random import randint
from sympy import isprime

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():

    initNumber = randint(10000000, 20000000)
    nNumber = randint(5000,15000)

    if initNumber % 2 == 0:
        initNumber += initNumber + 1

    prime1 = 0
    prime2 = 0
    nAnt = initNumber
    nPost = initNumber

    while prime1 != nNumber:
        nAnt -= 2
        if isprime(nAnt):
            prime1 += 1

    while prime2 != nNumber:
        nPost += 2
        if isprime(nPost):
            prime2 += 1

    saida = str(nAnt) + str(nPost)
    return saida

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()