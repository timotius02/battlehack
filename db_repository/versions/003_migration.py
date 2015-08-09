from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('pwdhash', VARCHAR(length=54)),
    Column('username', VARCHAR(length=120)),
)

FoodbankUsers = Table('FoodbankUsers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=120)),
    Column('pwdhash', String(length=54)),
)

GroceryUsers = Table('GroceryUsers', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=120)),
    Column('pwdhash', String(length=54)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].drop()
    post_meta.tables['FoodbankUsers'].create()
    post_meta.tables['GroceryUsers'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].create()
    post_meta.tables['FoodbankUsers'].drop()
    post_meta.tables['GroceryUsers'].drop()
