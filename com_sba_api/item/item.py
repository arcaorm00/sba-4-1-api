from com_sba_api.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DECIMAL, VARCHAR

class Item(Base):

    __tablename__ = "items"
    __table_args__ = {"mysql_collate": "utf8_general_ci"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(String)

engine = create_engine('mysql+mysqlconnector://root:munnin00@127.0.0.1/mariadb?charset=utf8', encoding=True, echo=True)
# Base.metadata.create_all(engine)