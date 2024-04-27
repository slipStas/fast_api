from typing import Annotated
from fastapi import APIRouter, Depends
from repository import Repository
from schemas import STaskAdd, STaskId

router = APIRouter(prefix="/api", tags=["Таски"])


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await Repository.add_one(task)
    my_resp = STaskId(
        ok=True,
        task_id=task_id
    )
    return my_resp


@router.get("")
async def get_tasks():
    all_tasks = await Repository.get_all()
    return {
        "data": all_tasks
    }
