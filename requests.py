from sqlalchemy.ext.asyncio import AsyncSession
from db.models import GroupsDataEntry
from db.base import session


class DataBase:


    def __init__(self):
        self.session = session


    async def test(self):
        entry = GroupsDataEntry()
        entry.group_id = 123
        entry.active_flag = 1

        self.session.add(entry)
        self.session.commit()