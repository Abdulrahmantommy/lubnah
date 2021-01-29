from peewee import *

# SQLite database using WAL journal mode and 64MB cache.
db = SqliteDatabase('pos.db', pragmas={'journal_mode': 'wal'}) # خاص بقواعد البيانات

class Branch(Model): # كلاس انشاء فرع

    location = CharField() # متغير لانشاء العنوان
    class Meta: # لتنفيذ المتغير
        database = db # استدعاء الداتا بيز
class Ussr(Model): # نفس اللي فوق
    usr = CharField()
    pwd = CharField()
    class Meta:
        database = db

class Supplier(Model):
    name = CharField()
    location = CharField()
    number = IntegerField()
    category = CharField()
    class Meta:
        database = db

db.connect(Model)
db.create_tables([Branch, Ussr, Supplier])