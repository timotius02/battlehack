from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
users = Table('users', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('social_id', VARCHAR(length=64), nullable=False),
    Column('nickname', VARCHAR(length=64), nullable=False),
    Column('email', VARCHAR(length=120)),
)

users = Table('users', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=120)),
    Column('pwdhash', String(length=54)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].columns['email'].drop()
    pre_meta.tables['users'].columns['nickname'].drop()
    pre_meta.tables['users'].columns['social_id'].drop()
    post_meta.tables['users'].columns['pwdhash'].create()
    post_meta.tables['users'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['users'].columns['email'].create()
    pre_meta.tables['users'].columns['nickname'].create()
    pre_meta.tables['users'].columns['social_id'].create()
    post_meta.tables['users'].columns['pwdhash'].drop()
    post_meta.tables['users'].columns['username'].drop()
