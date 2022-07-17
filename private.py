from aiogram import types, Router
from db.requests import DataBase as db

private_router = Router()

@private_router.message()
async def otest(msg: types.Message):
    await db().test()
