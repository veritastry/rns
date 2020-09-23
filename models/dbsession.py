# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_CFG
# 连接数据库的数据

# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    DB_CFG['user'], DB_CFG['pass'], DB_CFG['host'], DB_CFG['port'],
    DB_CFG['db'])

# engine
engine = create_engine(DB_URI, echo=False)
# sessionmaker生成一个session类
Session = sessionmaker(bind=engine)
dbSession = Session()
Base = declarative_base(engine)
