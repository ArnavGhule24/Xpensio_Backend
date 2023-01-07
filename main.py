from fastapi import FastAPI
from firebase_admin import firestore
import firebase
from model import Sms
from category import cat



db = firestore.client()

app = FastAPI()


@app.get('/categories')
async def categories(email:str):
    return cat(email)

@app.post('/postsms')
async def postsms(email:str,sms:list[Sms]):
    i=1
    for item in sms:
        data = {
            "merchant":item.merchant,
            "amount":item.amount,
            "date":item.date
        }
        db.collection(email).document("Message List").collection("List").document('List'+str(i)).set(data)
        i=i+1

