from peewee import CharField, ForeignKeyField, Model, SqliteDatabase

db = SqliteDatabase('products.db', pragmas=(('foreign_keys', 'on'),))
db.connect()


class Category(Model):
    name = CharField(max_length=100)

    class Meta:
        database = db


class Product(Model):
    name = CharField(max_length=100)
    category = ForeignKeyField(Category)

    class Meta:
        database = db


# db.create_tables([Category, Product])
