from sqlalchemy import MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger, Boolean

from db.base import Base, engine


class GroupsDataEntry(Base):
    __tablename__ = 'groups_data'

    group_id = Column(Integer, primary_key = True)
    active_flag = Column(Boolean)


Base.metadata.create_all(engine)