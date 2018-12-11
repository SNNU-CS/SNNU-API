'''
Created on Dec 11, 2018

@author: QiZhao
'''
from flask import jsonify,Blueprint,request
from snnusdk import Room
from snnusdk.exceptions import BuildingNotFoundError,RoomNotFoundError
from .handle import error_hanlder

room_bp = Blueprint('room', __name__)

@room_bp.route("/room/query_all",methods=["POST","GET"])
def query_all():
    building=request.args.get('building')
    week=request.args.get('week')
        
    try:
        room=Room(building=building,week=week)
        data=room.query_all()
        dic={}
        dic['status']=200
        dic['msg']='成功'
        dic['data']=data
        return jsonify(dic),200
    except BuildingNotFoundError as e:
        return error_hanlder(e, 200)
    except Exception as e:
        return error_hanlder(e, 500)
    
@room_bp.route("/room/get_all_rooms",methods=["POST","GET"])
def get_all_rooms():
    building=request.args.get('building')
    week=request.args.get('week')
    
    try:
        room=Room(building=building,week=week)
        data=room.get_all_rooms()
        dic={}
        dic['status']=200
        dic['msg']='成功'
        dic['data']=data
        return jsonify(dic),200
    except Exception as e:
        return error_hanlder(e, 500)
    
@room_bp.route("/room/get_all_rooms",methods=["POST","GET"])
def query_one_room():
    building=request.args.get('building')
    week=request.args.get('week')
    room=request.args.get('room')
    
    try:
        room=Room(building=building,week=week)
        data=room.query_one_room(room)
        dic={}
        dic['status']=200
        dic['msg']='成功'
        dic['data']=data
    except RoomNotFoundError as e:
        return error_hanlder(e, 200)
    except Exception as e:
        return error_hanlder(e, 500)