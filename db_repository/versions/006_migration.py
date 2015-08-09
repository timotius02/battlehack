from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
FoodbankUsers = Table('FoodbankUsers', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=120)),
    Column('pwdhash', VARCHAR(length=54)),
)

foodbankuser = Table('foodbankuser', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=120)),
    Column('pwdhash', String(length=54)),
)

transaction = Table('transaction', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_number', Integer),
    Column('delivery', DateTime),
    Column('quantity', Integer),
    Column('name', String(length=64)),
    Column('price', Float),
    Column('status', String(length=64)),
    Column('foodbankUser_id', Integer),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('item_number', Integer),
    Column('expiration', DateTime),
    Column('quantity', Integer),
    Column('name', String(length=64)),
    Column('price', Float),
    Column('sale', Boolean),
    Column('groceryUser_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['FoodbankUsers'].drop()
    post_meta.tables['foodbankuser'].create()
    post_meta.tables['transaction'].create()
    post_meta.tables['product'].columns['item_number'].create()
    post_meta.tables['product'].columns['sale'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['FoodbankUsers'].create()
    post_meta.tables['foodbankuser'].drop()
    post_meta.tables['transaction'].drop()
    post_meta.tables['product'].columns['item_number'].drop()
    post_meta.tables['product'].columns['sale'].drop()
