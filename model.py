from pydantic import BaseModel

class Sms(BaseModel):
    merchant:str
    amount:str
    date:str

class SmsList(BaseModel):
    smsList:list[Sms]