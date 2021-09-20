import dataBase
from flask import make_response
from flask import *
import app

constructionAmount = Blueprint('constructionAmountApi', __name__)
constructionAddPlot= Blueprint('constructionAddPlotApi', __name__)
constructionAddSupplier=Blueprint('constructionAddSupplierApi',__name__)

# add account for construction start up
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
    
# add plot for construction
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
    structure = addPlotApi['structure']
    material = addPlotApi['material']
    totalAmount=plotSqFeet*ratePerSqFeet
    addPlot=dataBase.constructionaddplot(societyName=societyName,plotNo=plotNo,plotOwnerName=plotOwnerName,phoneNo=phoneNo,amount=totalAmount,
                                              streetLocation=streetLocation,categories=categories,totalStories=totalStories,plotSqFeet=plotSqFeet,totalPlotSize=totalPlotSize,ratePerSqFeet=ratePerSqFeet,structure=structure,material=material)
    app.db.session.add(addPlot)
    app.db.session.commit()
    return make_response("added"),200

# add supplier account
@constructionAddSupplier.route('/addSupplier',methods=['Post'])
def addSupplier():
    addSupplierApi=request.get_json()
    name=addSupplierApi['name']
    contact=addSupplierApi['contact']
    cnic=addSupplierApi['cnic']
    address=addSupplierApi['address']
    filer=addSupplierApi['filer']
    supplierAdd=dataBase.constructionaddsupplier(name=name,contact=contact,cnic=cnic,address=address,filer=filer)
    app.db.session.add(supplierAdd)
    app.db.session.execute()
    return make_response("added"),200
    
