from flask import Blueprint,make_response
from flask import *
from app import *
from flask_sqlalchemy import SQLAlchemy

from dataBase import *



constructionApi = Blueprint('constructionApi', __name__)


@constructionApi.route('/construction' ,methods=['POST'])
def addConstructionAccountDetails():
    constructionDetailsApi = request.get_json()
    accountNo = constructionDetailsApi["accountNo"]
    name = constructionDetailsApi['name']
    amount = constructionDetailsApi['amount']
    construction=constructionaccount(accountNo=accountNo,name=name,amount=amount)
    db.session.add(construction)
    db.session.commit()
    return make_response("added"),200
    

