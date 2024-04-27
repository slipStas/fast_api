from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class Repository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def get_all(cls) -> list[STask]:
        async with new_session() as sesion:
            query = select(TaskOrm)
            result = await sesion.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]

            return task_schemas
