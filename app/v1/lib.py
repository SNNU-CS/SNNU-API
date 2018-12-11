'''
Created on Dec 11, 2018

@author: QiZhao
'''
from flask import  session, jsonify,Blueprint,request
from snnusdk import Library,get_borrow_info
from .handle import error_hanlder
import snnusdk

lib_bp = Blueprint('lib', __name__)

@lib_bp.route("/lib/getInfo",methods=["GET"])
def get_info():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic={}
            dic['data']=lib.get_info()
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401

@lib_bp.route("/lib/getBorrowingBooks",methods=["GET"])
def get_borrowing_books():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic={}
            dic['data']=lib.get_borrowing_books()
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401

@lib_bp.route("/lib/getReservationBooks",methods=["GET"])
def get_reservation_books():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic={}
            dic['data']=lib.get_reservation_books()
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401
    
@lib_bp.route("/lib/getCash",methods=["GET"])
def get_cash():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic={}
            dic['data']=lib.get_cash()
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401

@lib_bp.route("/lib/lockLibCard",methods=["GET"])
def lock_lib_card():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic=lib.lock_lib_card()
            dic['status']=200
#             dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError or UnauthorizedError as e:
            return jsonify({
                    'success':False,
                    'msg':str(e),
                    'status':401
                    }),401
        except Exception as e:
            return jsonify({
                    'success':False,
                    'msg':str(e),
                    'status':500
                }),500
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401
    
@lib_bp.route("/lib/unlockLibCard",methods=["GET"])
def unlock_lib_card():
    if 'username2' in session and 'password2' in session:
        try:
            lib=Library(session['username2'],session['password2'])
            dic=lib.unlock_lib_card()
            dic['status']=200
#             dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError or UnauthorizedError as e:
            return jsonify({
                    'success':False,
                    'msg':str(e),
                    'status':401
                    }),401
        except Exception as e:
            return jsonify({
                    'success':False,
                    'msg':str(e),
                    'status':500
                }),500
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401
    
@lib_bp.route("/lib/login",methods=["GET"])
def login():
    try:
        user=request.args.get('username2')
        pwd=request.args.get('password2')
        lib=Library(user,pwd)
        if lib.verify:
            session['username2'] = '41612164'
            session['password2'] = 'zq201651'
        return jsonify({
                    'status':200,
                    'msg':'登录成功',
                    'data':[]
            }),200
    except AuthenticationError as e:
        return error_hanlder(e,401)
    except Exception as e:
        return error_hanlder(e,500)
    
@lib_bp.route("/lib/getBorrowInfo",methods=["GET"])  
def get_borrow_info():
    try:
        dic=snnusdk.libiary.get_borrow_info()
        print(type(dic))
        dic['status']=200
        return jsonify(dic),200
    except Exception as e:
        return error_hanlder(e,500)
        