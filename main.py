from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("database was drop!")
    await create_tables()
    print("create database!")
    yield
    print("shutdown...")


class Task(BaseModel):
    name: str
    description: str | None


app = FastAPI(lifespan=lifespan)


@app.get("/task")
def get_tasks():
    task = Task(name="video", description="make a short video for Tik-Tok")
    return task
#
# def main():
#     print("main function is now")
#
#
# if __name__ == "__main__":
#     main()
#     print("this is for new branch")
