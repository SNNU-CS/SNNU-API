'''
Created on Dec 11, 2018

@author: QiZhao
'''
from flask import jsonify

def error_hanlder(e,status):
    dic={
            'status':status,
            'msg':str(e),
            'data':[]
        }
    return jsonify(dic),status