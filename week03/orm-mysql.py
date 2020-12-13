# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


# class Info_table(Base):
#     __tablename__ = 'info'
#     itemid = Column(Integer(), primary_key=True)
#     name = Column(String(50), index=True)
#     age = Column(Integer())
#     birthday = Column(String(50))
#     sex = Column(Integer(), server_default='1')  # 1男 2女
#     created_on = Column(DateTime(), nullable=False, server_default=func.now())
#     updated_on = Column(DateTime(), nullable=False,
#                         server_default=func.now(), onupdate=func.now())


# # # 实例一个引擎
# dburl = "mysql+pymysql://root:root@127.0.0.1:3306/testdb?charset=utf8mb4"
# engine = create_engine(dburl, echo=True, encoding="utf-8")
# Base.metadata.create_all(engine)


db = pymysql.connect("127.0.0.1","root","root","testdb",cursorclass=pymysql.cursors.DictCursor)

# try:

#     # %s是占位符
#     with db.cursor() as cursor:
#         sql = 'INSERT INTO info (name,age,birthday,sex) VALUES (%s, %s,%s,%s)'
#         value = ("peng", 22,'1999-03-16',1)
#         cursor.execute(sql, value)
#     db.commit()

# except Exception as e:
#     print(f"insert error {e}")

# finally:
#     # 关闭数据库连接
#     db.close()
#     print(cursor.rowcount)

try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'SELECT * FROM info'
        cursor.execute(sql)
        res = cursor.fetchall()
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(res)