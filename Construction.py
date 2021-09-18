from dataBase import *
from flask import make_response
from flask import *


#simple_page = Blueprint('simple_page', __name__, template_folder='templates')
# apii = Blueprint('constructionApi', __name__,url_prefix='/constructionApi')


@app.route('/addconstruction' ,methods=['POST'])
def addConstructionAccountDetails():
    constructionDetailsApi = request.get_json()
    accountNo = constructionDetailsApi["accountNo"]
    name = constructionDetailsApi['name']
    amount = constructionDetailsApi['amount']
    construction=constructionaccount(accountNo=accountNo,name=name,amount=amount)
    db.session.add(construction)
    db.session.commit()
    return make_response("added"),200
    

