from flask import Flask
from flask import render_template, send_file, send_from_directory
from flask import Response, request, jsonify
import json
import hashlib
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/senha',methods=["GET"])
def senha():
    senha = request.args.get('senha')
    print('password : {z}'.format(z=senha))
    return insertPassword(senha)

def insertPassword(password):
    d = {"password":createHash(password)}
    with open('storage.json','w') as JsonFile:
        json.dump(d,JsonFile)
    print('inserted password...')
    return '<p>Done!</p>'

def createHash(insert):
    k = hashlib.sha256()
    h = ' '.join(list(map(str,insert)))
    k.update(h.encode('utf-8'))
    d = k.hexdigest()
    print('created hash...')
    return d

if __name__ == '__main__':
    app.run("192.168.100.36" ,port=5000)
