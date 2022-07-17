from sqlalchemy import Integer, Column, Boolean

from base import Base


class GroupsDataEntry(Base):
    __tablename__ = 'groups_data'

    group_id = Column(Integer, primary_key = True)
    active_flag = Column(Boolean)
