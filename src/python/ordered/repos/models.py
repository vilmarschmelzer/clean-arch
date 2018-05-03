from peewee import (
    CharField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase
)

db = SqliteDatabase('requests.db', pragmas=(('foreign_keys', 'on'),))
db.connect()


class Request(Model):
    client = CharField(max_length=100)

    class Meta:
        database = db


class Item(Model):
    request = ForeignKeyField(Request)
    product_id = IntegerField()
    qtd = IntegerField()

    class Meta:
        database = db


# db.create_tables([Item, Request])
