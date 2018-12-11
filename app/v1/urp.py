'''
Created on Apr 30, 2018

@author: QiZhao
'''
from flask import  session, jsonify,Blueprint,request
from snnusdk import Urp
from snnusdk.exceptions import AuthenticationError
from .handle import error_hanlder

urp_bp = Blueprint('urp', __name__)
 
@urp_bp.route("/urp/getCourses",methods=["GET"])
def get_courses():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            u.login()
            dic={}
            dic['data']=u.get_courses()
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
    
@urp_bp.route("/urp/getOldCourses",methods=["GET","POST"])
def  get_old_courses():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            year=request.args.get('year')
            semester=request.args.get('semester')
            u.login()
            dic={}
            dic['data']=u.get_old_courses(year=year,semester=semester)
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except YearNotExistError as e:
            return error_hanlder(e, 200)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401

@urp_bp.route("/urp/getGrade",methods=["GET"])
def get_grade():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            u.login()
            dic={}
            dic['data']=u.get_grade()
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

@urp_bp.route("/urp/getGradeYearList",methods=["GET"])
def get_grade_year_list():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            u.login()
            dic={}
            dic['data']=u.get_grade_year_list()
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except YearNotExistError as e:
            return error_hanlder(e, 200)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401
    
@urp_bp.route("/urp/getAllGrades",methods=["GET","POST"])
def get_all_grades():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            year=request.args.get('year')
            semester=request.args.get('semester')
            u.login()
            dic={}
            dic['data']=u.get_all_grades(year=year,semester=semester)
            dic['status']=200
            dic['msg']='查询成功'
            return jsonify(dic),200
        except AuthenticationError as e:
            return error_hanlder(e,401)
        except YearNotExistError as e:
            return error_hanlder(e, 200)
        except Exception as e:
            return error_hanlder(e,500)    
    else:
        dic={
            'status':401,
            'msg':'请先登录',
            'data':[]
            }
        return jsonify(dic),401

@urp_bp.route("/urp/getGpa",methods=["GET"])
def get_gpa():
    if 'username' in session and 'password' in session:
        u=Urp(session['username'],session['password'])
        try:
            u.login()
            dic={}
            dic['data']=u.get_gpa()
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

@urp_bp.route("/urp/login",methods=["GET","POST"])
def login():
    try:
        user=request.args.get('username')
        pwd=request.args.get('password')
        u=Urp(user,pwd)
        u.login()
        if u.verify:
            session['username'] = user
            session['password'] = pwd
        return jsonify({
                    'status':200,
                    'msg':'登录成功',
                    'data':[]
            }),200
    except AuthenticationError as e:
        return error_hanlder(e,401)
    except Exception as e:
        return error_hanlder(e,500)

 
