import dataBase
from flask import make_response
from flask import *
import app

#simple_page = Blueprint('simple_page', __name__, template_folder='templates')
constructionAmount = Blueprint('constructionAmountApi', __name__)
constructionAddPlot= Blueprint('constructionAddPlotApi', __name__)

@constructionAmount.route('/constructionAmount' ,methods=['POST'])
def addConstructionAccountDetails():
    constructionDetailsApi = request.get_json()
    accountNo = constructionDetailsApi["accountNo"]
    name = constructionDetailsApi['name']
    amount = constructionDetailsApi['amount']
    construction=dataBase.constructionaccount(accountNo=accountNo,name=name,amount=amount)
    app.db.session.add(construction)
    app.db.session.commit()
    return make_response("added"),200
    
@constructionAddPlot.route('/addPlot' ,methods=['POST'])
def addPlot():
    addPlotApi = request.get_json()
    societyName = addPlotApi["societyName"]
    plotNo = addPlotApi['plotNo']
    plotOwnerName = addPlotApi['plotOwnerName']
    phoneNo = addPlotApi['phoneNo']
    streetLocation = addPlotApi['streetLocation']
    categories = addPlotApi['categories']
    totalStories = addPlotApi['totalStories']
    plotSqFeet = addPlotApi['plotSqFeet']
    totalPlotSize = addPlotApi['totalPlotSize']
    ratePerSqFeet = addPlotApi['ratePerSqFeet']
    amount = addPlotApi['amount']
    structure = addPlotApi['structure']
    material = addPlotApi['material']
    
    addPlot=dataBase.constructionaddplot(societyName=societyName,plotNo=plotNo,plotOwnerName=plotOwnerName,phoneNo=phoneNo,amount=amount,
                                              streetLocation=streetLocation,categories=categories,totalStories=totalStories,plotSqFeet=plotSqFeet,totalPlotSize=totalPlotSize,ratePerSqFeet=ratePerSqFeet,structure=structure,material=material)
    app.db.add(addPlot)
    app.db.session.commit()
    return make_response("added"),200

