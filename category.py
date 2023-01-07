from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials



db=firestore.client()

def cat(email:str):
    sumFood=0
    sumTravel=0
    sumEcom=0
    sumGrocery=0
    sumOther=0
    amount=0
    smsData=db.collection(email).document("Message List").collection("Monthly List").get()
    for data in smsData:
        sms=data.to_dict()
        amount=float(sms.get('amount'))
        merchant=sms.get('merchant')
        food = ['zomato','swiggy','eatsure','eatclub','dominos','pizzahut','ovenstory','mcdonalds','burger king','mojo pizza','fasoos','kaggis','kfc']
        travel = ['makemytrip','goibibo','easemytrip','indigo','airasia','spicejet','airindia','gofirst','ola','uber','rapido']
        ecommerce = ['snapdeal','amazon','flipkart','myntra']
        grocery = ['dunzo','blinkit','grofers','bigbasket','big basket','dmart','jio mart','jiomart']
        

        if merchant.lower() in food:
            sumFood = sumFood + amount
        elif merchant.lower() in travel:
            sumTravel = sumTravel + amount
        elif merchant.lower() in ecommerce:
            sumEcom = sumEcom + amount
        elif merchant.lower() in grocery:
            sumGrocery = sumGrocery + amount
        else:
            sumOther = sumOther + amount

    db.collection(email).document('Categories').collection('Category').document("Category").set({"Food":sumFood,"Travel":sumTravel,"ECommerce":sumEcom,"Other":sumOther})
    return {"Food":sumFood,"Travel":sumTravel,"ECommerce":sumEcom,"Grocery":sumGrocery,"Other":sumOther}