from datetime import datetime
from pymongo import MongoClient
from django.db import models

con = MongoClient('mongodb://localhost:27017/')
db = con.get_database("teste_clinica")
colecao = db.get_collection('Pacientes')
print(list(colecao.find({})))