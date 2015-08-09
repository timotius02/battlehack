from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
GroceryUsers = Table('GroceryUsers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=120)),
    Column('pwdhash', VARCHAR(length=54)),
)

products = Table('products', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('expiration', DATETIME),
    Column('quantity', INTEGER),
    Column('name', VARCHAR(length=64)),
    Column('price', FLOAT),
    Column('groceryUser_id', INTEGER),
)

groceryuser = Table('groceryuser', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=120)),
    Column('pwdhash', String(length=54)),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('expiration', DateTime),
    Column('quantity', Integer),
    Column('name', String(length=64)),
    Column('price', Float),
    Column('groceryUser_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['GroceryUsers'].drop()
    pre_meta.tables['products'].drop()
    post_meta.tables['groceryuser'].create()
    post_meta.tables['product'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['GroceryUsers'].create()
    pre_meta.tables['products'].create()
    post_meta.tables['groceryuser'].drop()
    post_meta.tables['product'].drop()
