from app.database.models import async_session
from app.database.models import User, Task
from sqlalchemy import select, update, delete

async def get_tasks():
    async with async_session() as session:
        result = await session.scalars(select(Task))
        for i in result:
            print(i.text)