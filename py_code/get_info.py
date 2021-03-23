from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/name',methods=['GET','POST'])
def get_name():
    if request.method == 'POST':
        return 'mother'
    else:
        return "fucker"

@app.route('/userProfile',methods=['GET','POST'])
def get_profile():
    if request.method == 'GET':
        name = request.args.get('name','')
        print(name)
        if(name == 'fucker'):
            return dict(name='fucker',id=100001)
        else:
            return dict(name='mother fucker',id=100001)
    elif request.method=='POST':
        print(request.form)
        print(request.data)
        print(request.json)
        name = request.json.get('name')
        if(name == 'fucker'):
            return dict(name='fucker',id=100001)
        else:
            return dict(name='mother fucker',id=100001)
        
        return '1'



