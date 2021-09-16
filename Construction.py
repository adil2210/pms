from app import *

def addConstructionAccountDetails():
    constructionDetailsApi = request.get_json()
    accountNo = constructionDetailsApi["accountNo"]
    name = constructionDetailsApi['name']
    amount = constructionDetailsApi['amount']
    
    construction=constructionaccount(name=name,accountNo=accountNo,amount=amount)
    db.session.add(construction)
    db.session.commit()
    return make_response("added"),200
    

