'''
Created on Apr 30, 2018

@author: QiZhao
'''

from flask import Flask,request
from app.v1.urp import urp_bp
from app.v1.room import room_bp
from app.v1.lib import lib_bp
from app.v1.campus import campus_bp

app = Flask(__name__)
app.secret_key = 'please-generate-a-random-secret_key'
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(urp_bp, url_prefix='/api/v1')
app.register_blueprint(room_bp,url_prefix='/api/v1')
app.register_blueprint(lib_bp,url_prefix='/api/v1')
app.register_blueprint(campus_bp,url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(host='localhost',port='5001',debug=True)
