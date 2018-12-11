'''
Created on Dec 11, 2018

@author: QiZhao
'''
from flask import  jsonify,Blueprint,request
from snnusdk import Campus


campus_bp = Blueprint('campus', __name__)

@campus_bp.route("/campus",methods=["GET","POST"])
def login():
    try:
        i=request.args.get('id')
        campus=Campus(id=i)
        return jsonify(campus.get_list()),200
    except Exception as e:
        return  jsonify({
            'success':False,
            'msg':str(e),
            'data':[]
        }),500