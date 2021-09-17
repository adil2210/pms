from dataBase import *
from app import *
construction=constructionaccount(accountNo="1312",name="badar",amount=8756)
db.session.add(construction)
db.session.commit()